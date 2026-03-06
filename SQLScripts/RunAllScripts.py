import mysql.connector
import os

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pwnnoob21!",
            database="dv1633"
            )

scripts = os.listdir()
for script in scripts:
    if(script.endswith(".sql")):
        if (script == "CreateTables.sql"):
            with open(script, encoding="utf-8") as f:
                mycursor = mydb.cursor()
                statement = ""
                for line in f:
                    line = line.strip()

                    if not line or line.startswith("--"):
                        continue

                    statement += line + " "

                    if line.endswith(";"):
                        print("Executing:", statement)
                        mycursor.execute(statement)
                        statement = ""

                mydb.commit()

                mycursor.close()
        else:
            with open(script, encoding="utf-8") as f:
                mycursor = mydb.cursor()
                mycursor.execute(f.read())

                mydb.commit()

                mycursor.close()

mydb.close()
            