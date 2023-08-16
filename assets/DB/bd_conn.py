import pandas as pd
import pymysql.cursors
from pymysql import err, Error, InterfaceError
import mysql.connector
from mysql.connector import pooling
from pandas import read_sql


class DbConn:

    # def __init__(self):
    #     self.poll_conn = pooling.MySQLConnectionPool(pool_name="zerdance_pool",
    #                                                 pool_size=2,
    #                                                 pool_reset_session=True,
    #                                                 host='50.87.237.60',
    #                                                 user='zerdance_Yochai',
    #                                                 password='Yochai@123456',
    #                                                 database='zerdance_general')

    # Connect to the database
    def get_query(self,query):
        print("trying to connect...")
        try:
            # pool_conn = pooling.MySQLConnectionPool(pool_name="zerdance_pool",
            #                                         pool_size=2,
            #                                         pool_reset_session=True,
            #                                         host='50.87.237.60',
            #                                         user='zerdance_Yochai',
            #                                         password='Yochai@123456',
            #                                         database='zerdance_general')
            connection = mysql.connector.connect(host='50.87.237.60',
                                                 user='zerdance_Yochai',
                                                 password='Yochai@123456',
                                                 database='zerdance_general')
            print(f"connecting succeeded. ")
            cur = connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
            return result

        except InterfaceError as e:
            print(f"got InterfaceError : {e}")

        except Error as e:
            print(f"got general error: {e}")

    def get_query_results(self, query=str):
        """
        retrieve query results from the DB
        :param query: str -> plan sql query
        :return: list-> of the results
        """
        cur = self.poll_conn.get_connection().cursor()
        with cur as db:
            db.execute(query)
            result = db.fetchall()
            return result
