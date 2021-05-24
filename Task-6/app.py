"""
A service that accesses the data and returns count of advertisements the user has seen.
"""
import logging

import mysql.connector
from flask import Flask
from flask import jsonify
from flask_restful import Api
from flask_restful import Resource
from mysql.connector import Error

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    """
    Homepage
    :return: Server is up!
    """
    return 'Server is up!', 200


def get_db():
    """
    Connect to Mysql
    """
    try:
        return mysql.connector.connect(user='user',
                                       password='password',
                                       host='db',
                                       database='database'
                                       )
    except Error as e:
        logger.info(e)


class UserAggregate(Resource):
    """
    Provides Aggregated results for a user
    """

    def __init__(self) -> None:
        self.db = get_db()

    def get(self, userid):
        """
        API returns the amount of advertisements.
        :return: Ads count of a user
        """
        cursor = self.db.cursor()
        cursor.execute(f'select count(*) from `adition` where userid={userid};')
        result = {'seen_ads': cursor.fetchone()[0]}
        return jsonify(result)

    def post(self):
        """
        Yet not Implemented!
        """
        pass

    def put(self):
        """
        Yet not Implemented!
        """
        pass

    def delete(self):
        """
        Yet not Implemented!
        """
        pass


api.add_resource(UserAggregate, '/ads/user/<int:userid>')
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    app.run(port=8080, host='0.0.0.0')
