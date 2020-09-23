from src.app import app
from flask import request, Response
from src.helpers.json_response import asJsonResponse
import re
from src.database import db
from bson.json_util import dumps
import numpy as np


@app.route("/lab/create/<labname>")
def createLab(labname):
    res = db.labs.insert_one({"name_lab": labname}).inserted_id
    return dumps(res)

@app.route("/lab/<lab_name>/meme")
def randomMeme(lab_name):
    res = db.labs.aggregate([
        { "$match":  {"name_lab": lab_name}},
        { "$sample": {"size": 1} }, 
        { "$project": {"img" : 1, "_id": 0}}
      ])
    return dumps(res)





