# Importing Required Libraries
import os #Used for interacting with the operating system
from box.exceptions import BoxValueError #An exception from the box library, which handles structured data as objects.
import yaml #A library for parsing and writing YAML files.
from cnnClassifier import logger #A logging utility specific to the cnnClassifier project
import json #Used for handling JSON data.
import joblib #For saving and loading Python objects efficiently
from ensure import ensure_annotations #A decorator to ensure function arguments are of the correct type.
from box import config_box #A tool to convert dictionaries to objects
from pathlib import Path #Provides an object-oriented approach to handling file paths.
from typing import Any #Used for type hinting, indicating that any type is acceptable.
import base64 #Used for encoding and decoding binary data.


#Function to Read YAML Files
@ensure_annotations# Ensures that the function's arguments and return values match the specified types.
def read_yaml(path_to_yaml:Path) -> config_box: #"read_yaml" This function reads a YAML file
    # "path_to_yaml" (Path): Expects a Path object pointing to the YAML file.

    """read the yaml file and return 

    Args:
        path_to_yaml(str):path like input

    Raises:
        ValueError:if yaml file is empty
        e: empty file 
    
    Return:
        ConfigBox:ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file) #Safely loads the content of the YAML file into a Python dictionary.
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")#Logs a message indicating that the YAML file was loaded successfully.
            return config_box(content) #Logs a message indicating that the YAML file was loaded successfully.
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

# Function to Save Data as JSON
@ensure_annotations 
def save_json(path: Path, data: dict): #"save_json": This function saves a Python dictionary as a JSON file at the specified path.
    #"path (Path)": The path where the JSON file will be saved.
    #"data (dict)": The dictionary that needs to be saved as JSON.
    
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to saved in json file 
    """
    #"json.dump": Dumps the dictionary into a JSON file with an indentation of 4 spaces.
    with open(path, "w") as f:
        json.dump(data , f, indent=4)

    

    #logger.info: Logs a message indicating where the JSON file was saved.
    logger,info(f"json file  saved at : {path}")