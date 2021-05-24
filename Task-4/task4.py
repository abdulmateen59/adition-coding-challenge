"""
Dump out of HDFS is missing some entries (that are in the dump out of
MySQL). The logs differ in format so they cannot be compared directly.
- Find the missing entries and explain us how you did so.
- Find a pattern that will make it easier for us to identify the source of the problem.
"""
import logging

from pyspark import SparkConf
from pyspark import SparkContext
from pyspark import sql
from pyspark.sql.functions import expr

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    conf = SparkConf().setAppName("Comparing_log_files").setMaster('local')
    sc = SparkContext(conf=conf)
    sqlContext = sql.SQLContext(sc)

    hadoop = sqlContext.read.options(header=True).csv('../resources/hadoop.csv')
    mysql = sqlContext.read.options(header=True, delimiter='	').csv('../resources/mysql.csv')
    logger.info(f'Total number of rows in hadoop csv = {hadoop.count()}')
    logger.info(f'Total number of rows in hadoop csv = {mysql.count()}')

    logger.info('Hadoop & Mysql Content Type count...')
    mysql.groupBy('wp_type').count().show()
    hadoop.groupBy('content_type').count().show()

    logger.info('Arranging Hadoop & Mysql screen_res where content type is Javascript...')
    hadoop.filter(hadoop['content_type'] == 'JAVASCRIPT').groupBy('berowser', 'screen_resolution').count().show()
    mysql.filter(mysql['wp_type'] == 2).groupBy('browser', 'screen_res').count().show()

    # Reducing size of dataframe using above analysis
    mysql_ids = mysql.filter((mysql.browser == 6)
                             | (mysql.browser == 12)
                             | (mysql.browser == 0)
                             | (mysql.browser == 8)).select('id')
    hadoop = hadoop.withColumnRenamed('(id', 'id')
    hadoop = hadoop.withColumn('id', expr('substring(id, 2, length(id))'))
    hadoop_ids = hadoop.filter((hadoop.berowser == 6)
                               | (hadoop.berowser == 12)
                               | (hadoop.berowser == 0)
                               | (hadoop.berowser == 8)).select('id')
    user_id = mysql_ids.subtract(hadoop_ids)
    logger.info(f'Found {mysql_ids.subtract(hadoop_ids).count()} missing records')
    missing_records = mysql.join(user_id, mysql['id'] == user_id['id'], how='inner')
    missing_records.show()

    missing_records_including_mysql = mysql.join(user_id, mysql['id'] == user_id['id'], how='left')
    missing_records.groupBy('browser', 'screen_res').count().show()
    missing_records_including_mysql.groupBy('browser', 'screen_res').count().show()
