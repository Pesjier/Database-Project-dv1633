import mysql.connector

def get_sql_database():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwnnoob21!",
    database = "dv1633"
    )
    return mydb