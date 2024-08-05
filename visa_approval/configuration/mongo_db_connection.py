import sys

from visa_approval.exception import visa_approvalException
from visa_approval.logger import logging

import os
from visa_approval.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

# using this package you can avoid timeout issues of mongodb
ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                # read the MONGODB_URL from the Environment variable
                mongo_db_url = os.getenv(MONGODB_URL_KEY)
                # check url exist or not
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                # make the connection
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise visa_approvalException(e,sys)