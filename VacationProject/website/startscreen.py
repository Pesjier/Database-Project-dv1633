from flask import Blueprint
from flask import render_template, request, redirect, url_for
import mysql.connector

from .country import country

startscreen = Blueprint("startscreen", __name__)

@startscreen.route("/")
def homepage():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwnnoob21!",
    database = "dv1633"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM countries")
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return render_template("display_all_countries.html", results = to_return)

@startscreen.route("/go_to_country", methods = ["POST"])
def go_to_country():
    return redirect(url_for(country.homepage))
