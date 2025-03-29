from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load the .env file
client = MongoClient(os.getenv("MONGODB_URI"))  # Grab the URI from .env
db = client["elan_db"]
collection = db["test_collection"]
collection.insert_one({"test": "Mongo works!"})
print(collection.find_one())