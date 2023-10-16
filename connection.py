import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            database='bd_certus',                             
            user='root',                                      
            password='72806558'
            )
        self.cursor=self.connection.cursor()