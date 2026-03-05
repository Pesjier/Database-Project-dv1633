from flask import Blueprint
from flask import render_template, request, redirect, url_for

from .database_connect import get_sql_database

country = Blueprint("country", __name__)

@country.route("/", methods = ["POST"])
def homepage():  
    country_id = request.form["c_id"]

    #NAME
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_country_name"

    mycursor.execute(f"SELECT {functionname}(%s)", (country_id,))
    to_return = mycursor.fetchall()
    country_name = to_return[0][0]

    mycursor.close()
    mydb.close()

    #ACTIVITY TYPE RATINGS
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_country_activity_type_ratings"

    mycursor.execute(f"call {functionname}(%s)", (country_id,))
    to_return = mycursor.fetchall()
    type_ratings = to_return

    mycursor.close()
    mydb.close()

    #TOP ACTIVITIES
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_country_top_activities"

    mycursor.execute(f"call {functionname}(%s, %s, %s, %s)", (country_id, 0, 0, 20,))
    to_return = mycursor.fetchall()
    activity_ratings = to_return

    mycursor.close()
    mydb.close()

    #TOP CITIES
    mydb = get_sql_database()
    mycursor = mydb.cursor()
    
    functionname = "get_country_top_cities"

    mycursor.execute(f"call {functionname}(%s, %s, %s, %s)", (country_id, 0, 0, 20,))
    to_return = mycursor.fetchall()
    city_ratings = to_return

    mycursor.close()
    mydb.close()

    return render_template("display_country_screen.html", name = country_name, city_ratings = city_ratings, activity_ratings = activity_ratings, type_ratings = type_ratings)