from visa_approval.configuration.mongo_db_connection import MongoDBClient
from visa_approval.constants import DATABASE_NAME
from visa_approval.exception import visa_approvalException
import pandas as pd
import sys
from typing import Optional
import numpy as np



class VisaApprovalData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            # calling to connection creation class and connection will be created
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise visa_approvalException(e,sys)
        

    # convert database data into data frame
    def export_collection_as_dataframe(self,collection_name:str,database_name:Optional[str]=None)->pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return pd.DataFrame of collection
            """
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            raise visa_approvalException(e,sys)