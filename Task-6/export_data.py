"""
Creates a database with a table and dumps mysql.csv data into it.
"""
import csv
import logging
import os

import mysql.connector
from mysql.connector import errorcode
from tqdm import tqdm

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    try:
        db = mysql.connector.connect(user='user',
                                     password='password',
                                     host='db',
                                     database='database',
                                     autocommit=True
                                     )
        cursor = db.cursor()
        create_table = """DROP TABLE IF EXISTS `adition`;
                       CREATE TABLE `adition` (id VARCHAR(255), logtype VARCHAR(255), wp_type VARCHAR(255),
                       campaign_id VARCHAR(255), banner_id VARCHAR(255), werbeplatz_id VARCHAR(255),
                       peer_ip VARCHAR(255), userid VARCHAR(255), timestamp VARCHAR(255), proxy_ip VARCHAR(255),
                       time TIMESTAMP, network VARCHAR(255), browser VARCHAR(255), os VARCHAR(255),
                       screen_res VARCHAR(255), country VARCHAR(255), state VARCHAR(255), delivered_as VARCHAR(255),
                       city VARCHAR(255), connection VARCHAR(255), fvers VARCHAR(255), gk VARCHAR(255),
                       mdev VARCHAR(255), subreq VARCHAR(255), server_id VARCHAR(255), svz_id VARCHAR(255),
                       fraud_action VARCHAR(255), fraud_detection_results VARCHAR(255), used_batch_media VARCHAR(255));
                        """
        for result in cursor.execute(create_table, multi=True):
            pass

        with open(f'{os.getcwd()}/resources/mysql.csv') as csv_file:
            reader = csv.DictReader(csv_file, delimiter='	')
            fieldnames = reader.fieldnames
            for row in tqdm(reader, desc='Please wait feeding data to mysql db...', total=32978):
                row['time'] = f"'{row['time']}'"
                if not row['svz_id'].isnumeric() and not row['svz_id'].isdigit():
                    row['svz_id'] = '000'
                query = f"INSERT INTO adition ({str(', '.join(fieldnames))}) VALUES ({(', '.join(row.values()))})"
                cursor.execute(query)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logger.info("Invalid username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logger.info("Invalid database")
        else:
            logger.info(err)
    else:
        db.close()
