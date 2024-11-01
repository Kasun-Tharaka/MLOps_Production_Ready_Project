import os
import sys

from pandas import DataFrame
from sklearn.model_selection import train_test_split

from visa_approval.entity.config_entity import DataIngestionConfig # configurations going return the all the paths
from visa_approval.entity.artifact_entity import DataIngestionArtifact # artifact provides return type
from visa_approval.exception import visa_approvalException
from visa_approval.logger import logging
from visa_approval.data_access.visa_approval_data import VisaApprovalData # convert into dataframe


class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        """
        :param data_ingestion_config: configuration for data ingestion
        """
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise visa_approvalException(e,sys)
        

    
    def export_data_into_feature_store(self)->DataFrame:
        """
        This method exports data from mongodb to csv file
        
        data is returned as artifact of data ingestion components
        Write an exception log and then raise an exception
        """
        try:
            logging.info(f"Exporting data from mongodb")
            # getting the visa data from mongodb
            usvisa_data = VisaApprovalData()
            dataframe = usvisa_data.export_collection_as_dataframe(collection_name=
                                                                   self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            #create a directry 
            feature_store_file_path  = self.data_ingestion_config.feature_store_file_path
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            # save the data inside directry as csv format
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe

        except Exception as e:
            raise visa_approvalException(e,sys)
        

    def split_data_as_train_test(self,dataframe: DataFrame) ->None:
        """
        This method splits the dataframe into train set and test set based on split ratio 
        
        Output: Folder is created in s3 bucket
        Write an exception log and then raise an exception
        """
        logging.info("Entered split_data_as_train_test method of Data_Ingestion class")

        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )
            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            logging.info(f"Exporting train and test file path.")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info(f"Exported train and test file path.")
        except Exception as e:
            raise visa_approvalException(e, sys) from e
        


    
    # combine above two methods to complete data ingersion.
    def initiate_data_ingestion(self) ->DataIngestionArtifact:
        """
        This method initiates the data ingestion components of training pipeline 
        
        train set and test set are returned as the artifacts of data ingestion components
        Write an exception log and then raise an exception
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            dataframe = self.export_data_into_feature_store()

            logging.info("Got the data from mongodb")

            self.split_data_as_train_test(dataframe)

            logging.info("Performed train test split on the dataset")

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )

            # save the splited data into different files to return.
            data_ingestion_artifact = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                            test_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise visa_approvalException(e, sys) from e