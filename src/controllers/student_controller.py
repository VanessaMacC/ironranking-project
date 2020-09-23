from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps


 
@app.route('/') 
def welcome():
    return {
        "status": "OK",
        "message": "Welcome to vanesukiapi"
    }

@app.route("/student/create/<studentname>")
def createStudent(studentname):
    db.pull.insert_one(
        {"user_id": f"{studentname}"}
    )
    return "yaestaría"

@app.route("/student/all")
def alllStudent():
    res = db.pull.distinct("user_name")
    return dumps(res)

