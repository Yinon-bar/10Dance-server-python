import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from assets.DB.bd_conn import DbConn



blp = Blueprint("attendance","attendance",description="Operations on attendance")

@blp.route("/get_all")
class Attendance(MethodView):

    # def __init__(self):
    #     self.client = DbConn.get_conn()

    def get(self):
        query = "show tables from zerdance_general "
        return DbConn.get_query_results(query=query)




