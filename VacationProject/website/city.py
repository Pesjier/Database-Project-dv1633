from flask import Blueprint, request, render_template, redirect, url_for
from .database_connect import get_sql_database

city = Blueprint("city", __name__)

@city.route("/", methods = ["POST"])
def homepage():  
    city_id = request.form["c_id"]

    #NAME
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_city_name"

    mycursor.execute(f"SELECT {functionname}(%s)", (city_id,))
    to_return = mycursor.fetchall()
    city_name = to_return[0][0]

    mycursor.close()
    mydb.close()

    #CITY COUNTRY
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_country_of_city"

    mycursor.execute(f"SELECT {functionname}(%s)", (city_id,))
    to_return = mycursor.fetchall()
    country_ID = to_return[0][0]

    mycursor.close()
    mydb.close()

    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_country_name"

    mycursor.execute(f"SELECT {functionname}(%s)", (country_ID,))
    to_return = mycursor.fetchall()
    country_name = to_return[0][0]

    mycursor.close()
    mydb.close()

    #ACTIVITY TYPE RATINGS
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_city_activity_type_ratings"

    mycursor.execute(f"call {functionname}(%s)", (city_id,))
    to_return = mycursor.fetchall()
    type_ratings = to_return

    mycursor.close()
    mydb.close()

    #TOP ACTIVITIES
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    functionname = "get_city_top_activities"

    mycursor.execute(f"call {functionname}(%s, %s, %s, %s)", (city_id, 0, 0, 20,))
    to_return = mycursor.fetchall()
    activity_ratings = to_return

    mycursor.close()
    mydb.close()

    return render_template("display_city_screen.html", name = city_name, country = country_ID, countryName = country_name,  activity_ratings = activity_ratings, type_ratings = type_ratings)