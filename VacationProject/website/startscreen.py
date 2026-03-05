from flask import Blueprint
from flask import render_template, request, redirect, url_for
from .database_connect import get_sql_database

from .country import country

startscreen = Blueprint("startscreen", __name__)

@startscreen.route("/")
def homepage():
    mydb = get_sql_database()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM countries")
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return render_template("display_all_countries.html", results = to_return)
