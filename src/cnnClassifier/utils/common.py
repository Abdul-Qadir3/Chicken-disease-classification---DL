import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> config_box:
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
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return config_box(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to saved in json file 
    """
    with open(path, "w") as f:
        json.dump(data , f, indent=4)

    logger,info(f"json file  saved at : {path}")