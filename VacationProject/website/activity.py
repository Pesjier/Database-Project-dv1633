from flask import Blueprint, request, render_template, redirect, url_for
from .database_connect import get_sql_database


activities = Blueprint("activities", __name__)

def addact_id(act_id, functionname):
    mydb = get_sql_database()
    mycursor = mydb.cursor()
    mycursor.execute(f"call {functionname}(%s)", (act_id,))
    to_return = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return to_return

#startup for ../activities
@activities.route("/", methods = ["GET"])
def selectpage():
    return render_template("actid_button.html")

# user select what to see(procedure) and the act_id  
@activities.route("/choose", methods = ["POST"])
def choose():
    act_id = (request.form["act_id"])
    print("ACT ID:", act_id)
    results1 = addact_id(act_id, "get_activitytype")
    results2 = addact_id(act_id, "get_city_avg_ratae_count_users")
    results3 = addact_id(act_id, "get_country_avg_ratae_count_users")
    results4 = addact_id(act_id, "getavg_rate_count")
    results5 = addact_id(act_id, "getactivityname")
    vac_id = act_id
    result6 = addact_id(vac_id, "get_username_rate")
    print(result6[0])

    return render_template("act_type_display.html", results1 = results1, results2 = results2, results3 = results3, results4 = results4, name_act = results5[0][0], 
    country = results5[0][1], city = results5[0][2], result6 = result6)
