from flask import Blueprint

activitytype = Blueprint("activitytype", __name__)

@activitytype.route("/")
def activitytype_preview():
    return "<p1>activitytype_preview<p1>"