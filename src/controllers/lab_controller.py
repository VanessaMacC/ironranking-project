from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import numpy as np
import pymongo
import time
from datetime import datetime


@app.route("/lab/create/", defaults={"labname": None})
@app.route("/lab/create/<labname>")
def createLab(labname):

    # Devuelve status code 400 BAD REQUEST si no se especifica un nombre para el lab
    if labname == None:
        return {
            "status": "Error HTTP 400 (Bad Request)",
            "message": "Empty student name, please specify one"
        }
    # Devuelve el nombre del nuevo
    else:
        data = {"name_lab": labname}
        newLab = db.pull.insert_one(data)
        inserted_lab = db.labs.insert_one({"name_lab": labname}).inserted_id
        res = f"Lab {labname} has been created into pull data base", inserted_lab
    return dumps(res)


@app.route("/lab/<lab_name>/meme")
def randomMeme(lab_name):
    # Devuelve un meme random 
    res = db.labs.aggregate([
        {"$match":  {"name_lab": lab_name}},
        {"$sample": {"size": 1}},
        {"$project": {"img": 1, "_id": 0}}
    ])
    return dumps(res)

@app.route("/lab/<name_lab>/search")
def lab_analysis(name_lab):
    # Devuelve datos estadísticos de las pull, total de abiertas y cerradas, 
    # porcentajes de cada una, lista de memes únicos y tiempos de correción por lab
    opened_pr = db.pull.find(
        {"$and": [{"name_lab": f"{name_lab}"}, {"state": "open"}]}).count()
    closed_pr = db.pull.find(
        {"$and": [{"name_lab": f"{name_lab}"}, {"state": "closed"}]}).count()
    img = db.pull.find({"name_lab": f"{name_lab}"}).distinct("img")
    grade_time = db.pull.find({"name_lab": f"{name_lab}"}, {"created":1, "closed":1})
    grade_time_list=[]
    for x in grade_time:
        close_time = datetime.fromisoformat(x["closed"].replace('Z',''))
        open_time = datetime.fromisoformat(x["created"].replace('Z',''))
        grade_time_list.append((close_time-open_time).total_seconds())
    res = {'-El numero de PR abiertas es:': opened_pr,
           '-El numero de PR cerradas es:': closed_pr,
           '-El porcentaje de PR abiertas es:': f'{round(opened_pr/(opened_pr+closed_pr)*100)}%',
           '-El porcentaje de PR cerradas es:': f'{round(closed_pr/(opened_pr+closed_pr)*100) }%',
           '-La lista de memes únicos es': img,
           '-El tiempo máximo de correción de este lab es': (f'{str(round(max(grade_time_list)/3600,2))}h'),
           '-El tiempo mínimo de correción de este lab es': (f'{str(round(min(grade_time_list)/3600,2))}h'),
           '-El promedio de tiempo de correción de este lab es': (f'{str(round(np.mean(grade_time_list)/3600,2))}h')
           }
    return dumps(res)
