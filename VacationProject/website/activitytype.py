from flask import Blueprint
from flask import render_template, request, redirect, url_for

from .database_connect import get_sql_database

activitytype = Blueprint("activitytype", __name__)

@activitytype.route("/", methods = ["POST"])
def homepage():  
    type = request.form["type"]

    #TOP CITY RATINGS
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_type_top_cities"

    mycursor.execute(f"call {functionname}(%s)", (type,))
    to_return = mycursor.fetchall()
    city_ratings = to_return

    mycursor.close()
    mydb.close()

    #TOP COUNTRY RATINGS
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_type_top_countries"

    mycursor.execute(f"call {functionname}(%s)", (type,))
    to_return = mycursor.fetchall()
    country_ratings = to_return

    mycursor.close()
    mydb.close()

    return render_template("display_activitytype_screen.html", name = type, country_ratings = country_ratings, city_ratings = city_ratings)