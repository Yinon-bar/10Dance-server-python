import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from assets.DB.bd_conn import DbConn
import mysql.connector



blp = Blueprint("attendance","attendance",description="Operations on attendance")

@blp.route("/get_all")
class GelAllAttendance(MethodView):

    # def __init__(self):
    #     self.client = DbConn.get_conn()

    def get(self):
        query = "show tables from zerdance_general "
        results =  DbConn().get_query_results(query=query)
        unpack_result = [d['Tables_in_zerdance_general'] for d in results]
        return unpack_result


@blp.route("/get_all_from_table/<string:table_name>")
class GetFromTable(MethodView):

    def get(self,table_name:str):
        query = f"""select    
                         fName,
                        lName
                    from {table_name}"""

        # connection = mysql.connector.connect(host='50.87.237.60',
        #                                      user='zerdance_Yochai',
        #                                      password='Yochai@123456',
        #                                      database='zerdance_general')
        #
        # mycoursor = connection.cursor()
        #
        # mycoursor.execute("select fName,lName from attendees")
        #
        # my_result = mycoursor.fetchall()
        #
        # print(my_result)

        results = DbConn().get_query(query=query)
        print(results)
        return results

