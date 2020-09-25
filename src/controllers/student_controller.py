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

@app.route("/student/create/", defaults = {"studentname": None})
@app.route("/student/create/<studentname>")
def createStudent(studentname):

    # Set status code 400 BAD REQUEST
    if studentname == None:
        return {
            "status": "Error HTTP 400 (Bad Request)",
            "message": "Empty student name, please specify one"
        }
    # Al introducir el endpoint arriba indicado, la función se encarga de crear un nuevo estudiante dentro de la db
    data = {"user_name": studentname}
    newStudent = db.pull.insert_one(data)
    return f"User {studentname} has been created into pull data base"

@app.route("/student/all")
def allStudent():
    # Devuelve un listado de todos los estudiantes
    res = db.pull.distinct("user_name")
    return dumps(res)


