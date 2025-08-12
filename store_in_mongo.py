from pymongo import MongoClient
from datetime import datetime
import os

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")  # Change if using cloud MongoDB
db = client["code_logs"]
collection = db["push_history"]

# Get latest commit hash and message
commit_msg = os.popen('git log -1 --pretty=%B').read().strip()
commit_hash = os.popen('git log -1 --pretty=%H').read().strip()

# Insert record into MongoDB
collection.insert_one({
    "commit_hash": commit_hash,
    "commit_message": commit_msg,
    "pushed_at": datetime.now()
})

print("Push details stored in MongoDB!")
