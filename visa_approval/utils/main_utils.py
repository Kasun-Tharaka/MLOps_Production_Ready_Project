import os
import sys
import numpy as np
import dill
import yaml
from pandas import DataFrame
from visa_approval.logger import logging
from visa_approval.exception import visa_approvalException



def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise visa_approvalException(e, sys) from e



def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise visa_approvalException(e, sys) from e



def load_object(file_path :str) -> object:
    logging.info("called load_object method of utils")

    try:
        with open(file_path, 'rb') as file_obj:
            obj = dill.load(file_obj)
        logging.info('Executed load_object method of utils')
        
        return obj
    except Exception as e:
        raise visa_approvalException(e, sys) from e
    


def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise visa_approvalException(e, sys) from e
    


def load_numpy_array_data(file_path: str) -> np.array:
    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise visa_approvalException(e, sys) from e
    


def save_object(file_path: str, obj: object) -> None:
    logging.info("called save_object method of utils")
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info('Executed save_object of utils')
    except Exception as e:
        raise visa_approvalException(e, sys) from e



def drop_columns(df : DataFrame, cols: list) -> DataFrame:
    logging.info('called drop_columns method of utils')
    try:
        df = df.drop(columns=cols, axis=1)
        logging.info('executed drop_columns method of utils')

        return df
    except Exception as e:
        raise visa_approvalException(e, sys) from e