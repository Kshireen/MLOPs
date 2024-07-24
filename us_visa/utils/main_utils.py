import os 
import sys

import dill
import yaml
import numpy as np
from pandas import DataFrame

from us_visa.logger import logging
from us_visa.exception import USvisaException


def read_yaml_file(file_path:str) -> dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path) as yaml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise USvisaException(e, sys) from e
    

def write_yaml_file(file_path: str, content: object, replace: bool =False) -> None:
    """
    Write yaml file from a dictionary
    file-path =str
    content = dict
    bool = false
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok = true)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Successfully write yaml file")

    except Exception as e:
        raise USvisaException(e, sys) from e
    


def load_object(file_path:str)-> object:
    """
    file_path: str
    """
    try:
        with open(file_path, "rb") as file:
            logging.info("Load object successfully")
            return dill.load(file)
    except Exception as e:
        raise USvisaException(e, sys) from e


def save_nummpy_array_data(file_path: str, array: np.ndarray) -> None:
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.ndarray data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise USvisaException(e, sys) from e
    



def load_numpy_array_data(file_path: str) -> np.ndarray:
    """
    Load numpy array data from file
    file_path: str location of file to load
    return: np.ndarray data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            logging.info("Load numpy array data successfully")
            return np.load(file_obj, allow_pickle=True)
    except Exception as e:
        raise USvisaException(e, sys) from e
    



def save_object(file_path:str, obj: object) -> None:
    """
    Save object to file
    file_path: str location of file to save
    obj: object to save
    """
    try:
        logging.info("Save object successfully")
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise USvisaException(e, sys) from e
    


def drop_columns(df: DataFrame, columns: list) -> DataFrame:
    """
    Drop columns from a pandas DataFrame
    df: DataFrame to drop columns from
    columns: list of columns to drop
    return: DataFrame with columns dropped
    """
    try:
        df = df.drop(columns=columns, axis=1)
        logging.info("Drop columns successfully")

        return df
    except Exception as e:
        raise USvisaException(e, sys) from e    
    
    
