from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Connessione al vecchio database
client_old = MongoClient(os.getenv('DB_FROM'))
client_new = MongoClient(os.getenv('DB_TO'))

databases = ['sample']

for database in databases:
    db_old = client_old[database]
    print(f"Database {database}")
    for collection in db_old.list_collection_names():
        print(f"\tCopying {collection}...")
        collection_old = db_old[collection]
        db_new = client_new[database]
        collection_new = db_new[collection]
        for document in collection_old.find():
            collection_new.insert_one(document)
        print("\tDone")
