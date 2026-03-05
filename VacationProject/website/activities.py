from flask import Blueprint, request, render_template, redirect, url_for
import mysql.connector

activities = Blueprint("activities", __name__)

def addact_id(act_id, functionname):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pwnnoob21!",
    database = "dv1633"
    )

    mycursor = mydb.cursor()
    mycursor.execute(f"call {functionname}(%s)", (act_id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

#startup for ../activities
@activities.route("/", methods = ["GET"])
def selectpage():
    return render_template("selectact_id.html")

# user select what to see(procedure) and the act_id  
@activities.route("/choose", methods = ["POST"])
def choose():
    act_id = (request.form["act_id"])
    choices = (request.form["choices"])
    print("choices:", choices)
    print("ACT ID:", act_id)
    if choices == "1":
        results = addact_id(act_id, "get_activitytype")
        name = "get_activitytype"
        return render_template("display.html", results = results, name  = name)
    elif choices == "2":
        results = addact_id(act_id, "get_cities_avg_rate")
        name = "get_cities_avg_rate"
        return render_template("display.html", results = results, name = name )
    elif choices =="3":
        results = addact_id(act_id, "get_countries_avg_rate")
        name = "get_countries_avg_rate"
        return render_template("display.html", results = results, name = name)
    elif choices == "4":
        results = addact_id(act_id, "getactivityname")
        name = "getactivityname"
        return render_template("display.html", results = results, name = name) 
    else:
        results = addact_id(act_id, "getavg_rate_count")
        name = "getavg_rate_count"
        return render_template("display.html", results = results, name = name)
    
#.../activities/ratings give the user and their ratings
@activities.route("/ratings", methods = ["GET", "POST"])
def ratings():
    if request.method == "POST":
        vac_id = request.form["vac_id"]
        print("vacid: ", vac_id)
        results = addact_id(vac_id, "get_username_rate")
        name = "get_username_rate"
        return render_template("display.html", results = results, name = name)
    
    return render_template("selectvac_id.html")