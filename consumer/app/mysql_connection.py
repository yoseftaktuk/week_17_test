import mysql.connector
import os


class MysqlManager:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST','mysql'),
            user=os.getenv('MYSQL_USER','appuser'),
            password=os.getenv('MYSQL_PASSWORD','apppass'),
            database=os.getenv('MYSQL_DATABASE','users'),
        )   
        except mysql.connector.Error as err:
            raise err  
        self.cruser = self.connection.cursor()
         