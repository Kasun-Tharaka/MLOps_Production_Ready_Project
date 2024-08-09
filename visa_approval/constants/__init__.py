import os
from datetime import date

DATABASE_NAME = "VISA_APPROVAL"
COLLECTION_NAME = "visa_data"
MONGODB_URL_KEY = "MONGODB_URL" # setup this as system variable for more secure access

PIPELINE_NAME: str = "visa_approval"
ARTIFACT_DIR: str = "artifact"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

FILE_NAME: str = "EasyVisa.csv"
MODEL_FILE_NAME = "model.pkl"

# when data validation created,
TARGET_COLUMN = 'case_status'
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
SCHEMA_FILE_PATH = os.path.join('config', 'schema.yaml')


# Data Ingestion constants
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion" # inside artifacts this will be centered
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store" # inside artifacts this will be centered
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


# Data Validation constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"