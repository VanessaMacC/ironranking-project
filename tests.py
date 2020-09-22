import re
import requests
from dotenv import load_dotenv
import os
import json
load_dotenv()

def get_comment(comment, apiKey=os.getenv("GITHUB_APIKEY")):
    headers = {"Authorization": f"Bearer {apiKey}"}
    res = requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/issues/{comment}/comments',headers=headers)
    comment = res.json()
    #print(f"Request comment to {res.url}")
    return comment

def lab_shared(comment):
    try:
        return re.findall('@\w*-?\w+',comment[0]['body'])
    except:
        return None

def get_img(comment):
    try:
        try:
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            z = z[1].split("'")
            return z[0]
        except:
            z = re.findall(r'https:.*jpg|.*png|.*jpeg',comment[0]['body'])
            z = str(z).split('(')
            return z[0]
    except:
        return None    

def get_gh_data(x, apiKey=os.getenv("GITHUB_APIKEY")):
    headers = {"Authorization": f"Bearer {apiKey}"}
    res = requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls/{x}',headers=headers)
    print(f"Request data to {res.url}")
    data = res.json()
    comment=get_comment(x)
    try:
        return{
            'lab_id':data['id'],
            'user_id':data['user']['id'],
            'user_name':data['user']['login'],
            'name_lab':data['title'].replace(" ", "").split("]")[0].strip("["),
            'state':data['state'],
            'created':data['created_at'],
            'closed':data['closed_at'],
            'instructor':comment[0]['user']['login'],
            'lab_shared':lab_shared(comment),
            'img':get_img(comment)   
    }
    except:
        return {'lab_id': None}
    
def last_pull(apiKey=os.getenv("GITHUB_APIKEY"), query_params={}):
    headers = {"Authorization": f"Bearer {apiKey}"}
    res = requests.get(f'https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls',headers=headers)
    data = res.json()
    return data

lastpull=last_pull(query_params={"per_page":2})
last=lastpull[0]['number']
last

data = [get_gh_data(i) for i in range(1,(last+1))]

import pandas as pd
jsn = pd.DataFrame(data)
jsn.to_json('pull.json',orient="records")