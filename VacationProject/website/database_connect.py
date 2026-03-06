import mysql.connector

def get_sql_database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laura123",
    database = "mysqlproject"
    )
    return mydb