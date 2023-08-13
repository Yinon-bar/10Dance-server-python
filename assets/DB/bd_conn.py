import pymysql.cursors
from pymysql import err,Error,InterfaceError

class DbConn:
    # Connect to the database
    def get_conn(self):
        print("trying to connect...")
        try:
            connection = pymysql.connect(host='50.87.237.60',
                                         user='zerdance_Yochai',
                                         password='Yochai@123456',
                                         database='zerdance_general',
                                         cursorclass=pymysql.cursors.DictCursor)
            print(f"connecting succeeded. ")
            return connection.cursor()

        except InterfaceError as e:
            print(f"got InterfaceError : {e}")

        except Error as e:
            print(f"got general error: {e}")



    def get_query_results(self,query=str):
        with self.get_conn() as db:
            db.execute(query=query)
            rows = db.fetchall()
            for row in rows:
                print(f'{row[0]} {row[1]} {row[2]}')

            return rows