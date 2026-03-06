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

# user select what to see(procedure) and the act_id  
@activities.route("/", methods = ["POST"])
def choose():
    act_id = request.form["act_id"]
    print("ACT ID:", act_id)
    results1 = addact_id(act_id, "get_activitytype")
    print(results1)
    results4 = addact_id(act_id, "getavg_rate_count")
    print(results4)
    results5 = addact_id(act_id, "getactivityname")
    print(results5)

    result6 = addact_id(act_id, "get_username_rate_id")
    print(result6[0])

    return render_template("act_type_display.html", results1 = results1[0][0], results4 = results4[0][0], name_act = results5[0][0], 
    country = results5[0][1], city = results5[0][2], result6 = result6)
