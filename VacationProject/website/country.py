from flask import Blueprint
from flask import render_template, request, redirect, url_for
import mysql.connector

country = Blueprint("country", __name__)

@country.route("/", methods = ["POST"])
def homepage():  
    country_id = request.form["c_id"]
    return render_template("base.html", message = str(country_id))





