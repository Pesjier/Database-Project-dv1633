from flask import Blueprint
from flask import render_template, request, redirect, url_for
import mysql.connector

country = Blueprint("country", __name__)

message = "Hello"


@country.route("/")
def homepage():

    return render_template("base.html", message = message)





