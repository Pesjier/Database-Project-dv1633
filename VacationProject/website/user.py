from flask import Blueprint, request, render_template, redirect, url_for
import mysql.connector

def function_query(id, query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laura123",
    database = "mysqlproject"
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"select {query}(%s)", (id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

def procedure_qeury(id, query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laura123",
    database = "mysqlproject"
    )

    mycursor = mydb.cursor()

    mycursor.execute(f"call {query}(%s)", (id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

user = Blueprint("user", __name__)
@user.route("/", methods = ["GET"])
def homepage():
    return render_template("user_button.html")

@user.route("/choose", methods = ["POST"])
def choose():
    user_id = (request.form["user_id"])
    print("user_id", user_id)
    #country_id = function_query(user_id)
    countryname = "croatia"  # hardcoded ska hämta from country countryname
    name =function_query(user_id, "get_user_name")
    results2 = procedure_qeury(user_id, "get_user_vacation_average_rating")
    return render_template("user_display.html", name = name[0][0], countryname = countryname, results2 = results2)