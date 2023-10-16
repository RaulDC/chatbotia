import mysql.connector

class DataBase:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='bbdyxtq2xayjozsfil1n-mysql.services.clever-cloud.com',
            database='bbdyxtq2xayjozsfil1n',                             
            user='u4wtydnovodwvldv',                                      
            password='oNdjuw7Jl28J3A26x0U3'
            )
        self.cursor=self.connection.cursor()