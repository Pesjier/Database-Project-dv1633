from flask import Blueprint, request, render_template, redirect, url_for
from .database_connect import get_sql_database

def function_query(id, query):
    mydb = get_sql_database()

    mycursor = mydb.cursor()

    mycursor.execute(f"select {query}(%s)", (id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

def procedure_qeury(id, query):
    mydb = get_sql_database()

    mycursor = mydb.cursor()

    mycursor.execute(f"call {query}(%s)", (id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

user = Blueprint("user", __name__)

@user.route("/", methods = ["GET", "POST"])
def homepage():
    user_id = (request.form["user_id"])
    print("user_id", user_id)
    name =function_query(user_id, "get_user_name")
    results2 = procedure_qeury(user_id, "get_user_vacation_average_rating")
    return render_template("user_display.html", name = name[0][0], results2 = results2)