import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print("Mongo URL:", MONGO_DB_URL)

ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def cv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)

            # Convert CSV → JSON (list of records)
            records = list(json.loads(data.to_json(orient="records")))
            print(f"✅ Total records extracted: {len(records)}")
            return records

        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            if not records:
                raise ValueError("No records to insert in MongoDB!")

            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)

            print(f"✅ {len(records)} records inserted successfully into '{database}.{collection}'")
            return len(records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)

# ---------------- MAIN ----------------
if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "Deepak"
    COLLECTION = "NetworkData"

    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_convertor(file_path=FILE_PATH)

    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print("Total records inserted:", no_of_records)
