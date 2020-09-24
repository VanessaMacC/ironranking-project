from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import numpy as np
import pymongo
import dateutil

@app.route("/lab/create/", defaults = {"labname": None})
@app.route("/lab/create/<labname>")
def createLab(labname):

    # Set status code to 400 BAD REQUEST
    if labname == None:
        return {
            "status": "Error HTTP 400 (Bad Request)",
            "message": "Empty student name, please specify one"
        }   
    else:
        data = {"name_lab": labname}
        newLab = db.pull.insert_one(data)
        return f"Lab {labname} has been created into pull data base"

    #res = db.labs.insert_one({"name_lab": labname}).inserted_id
    #return dumps(res)    

@app.route("/lab/<lab_name>/meme")
def randomMeme(lab_name):
    res = db.labs.aggregate([
        {"$match":  {"name_lab": lab_name}},
        {"$sample": {"size": 1}},
        {"$project": {"img": 1, "_id": 0}}
    ])
    return dumps(res)

@app.route("/lab/<name_lab>/search")
def allOpenClose(name_lab):
    opened_pr = db.pull.find({"$and": [{"name_lab":f"{name_lab}"},{"state": "open"}]}).count()
    closed_pr = db.pull.find({"$and": [{"name_lab":f"{name_lab}"},{"state": "closed"}]}).count()
    img = db.pull.find({"name_lab":f"{name_lab}"}).distinct("img")
    #openToDate = db.pull.aggregatedb.collection.aggregate([{"$project":{"created":{"$dateFromString":{"dateString":"$created"}}}
    #{"$project": {"timeDiff": {"$divide":[{"$subtract": ["$endDate.date", "$startDate.date"]}, 1000 * 60 * 60]}}}])
    res = {'-El numero de PR abiertas es:': opened_pr,
           '-El numero de PR cerradas es:': closed_pr,
           '-El porcentaje de PR abiertas es:':f'{round(opened_pr/(opened_pr+closed_pr)*100)}%',
           '-El porcentaje de PR cerradas es:': f'{round(closed_pr/(opened_pr+closed_pr)*100) }%',
           '-La lista de memes únicos es': img,
           #'-El tiempo de corrección es': date_diff,
           }
    return dumps(res)



