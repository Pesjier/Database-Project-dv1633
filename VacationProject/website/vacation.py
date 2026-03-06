from flask import Blueprint, request, render_template, redirect, url_for
from .database_connect import get_sql_database

vacation = Blueprint("vacation", __name__)


@vacation.route("/", methods = ["POST"])
def homepage():
    vac_id = request.form["vac_id"]

    mydb = get_sql_database()
    mycursor = mydb.cursor()
    functionname = "get_vacation_end"
    mycursor.execute(f"select {functionname}(%s)", (vac_id,))
    end_vacation = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    mydb = get_sql_database()
    mycursor = mydb.cursor()
    functionname = "get_vacation_start"
    mycursor.execute(f"select {functionname}(%s)", (vac_id,))
    start_vacation = mycursor.fetchall()

    mycursor.close()
    mydb.close()


    mydb = get_sql_database()
    mycursor = mydb.cursor()
    functionname = "get_vacation_ratings"
    mycursor.execute(f"call {functionname}(%s)", (vac_id,))
    rate_act_name_id = mycursor.fetchall()

    mycursor.close()
    mydb.close()


    return render_template("vacation_display.html", start = start_vacation[0][0], end = end_vacation[0][0], results = rate_act_name_id)