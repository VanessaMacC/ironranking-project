from pymongo import MongoClient
from config import DBURL

client = MongoClient(DBURL)
db = client.get_database()


