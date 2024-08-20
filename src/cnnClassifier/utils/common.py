# Importing Required Libraries
import os  # Used for interacting with the operating system, such as file and directory operations.
from box.exceptions import BoxValueError  # An exception from the box library, which handles structured data as objects.
import yaml  # A library for parsing and writing YAML files, often used for configuration files.
from cnnClassifier import logger  # A logging utility specific to the cnnClassifier project, used to log messages.
import json  # Used for handling JSON data, allowing for reading, writing, and manipulating JSON files.
import joblib  # For saving and loading Python objects efficiently, often used for model persistence.
from ensure import ensure_annotations  # A decorator to ensure function arguments are of the correct type.
from box import config_box  # A tool to convert dictionaries to objects, allowing attribute-style access.
from pathlib import Path  # Provides an object-oriented approach to handling file paths, making them easier to work with.
from typing import Any  # Used for type hinting, indicating that any type is acceptable for certain function parameters.
import base64  # Used for encoding and decoding binary data, often for image or file handling.

# Function to Read YAML Files
@ensure_annotations  # Ensures that the function's arguments and return values match the specified types.
def read_yaml(path_to_yaml: Path) -> config_box:
    """
    This function reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs while reading the file.

    Returns:
        ConfigBox: The content of the YAML file, accessible as object attributes.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Safely loads the content of the YAML file into a Python dictionary.
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Logs a message indicating successful loading.
            return config_box(content)  # Converts the dictionary into a ConfigBox object and returns it.
    except BoxValueError:
        raise ValueError("YAML file is empty")  # Raises an error if the YAML file is empty.
    except Exception as e:
        raise e  # Re-raises any other exceptions that occur.

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# Function to Save Data as JSON
@ensure_annotations  # Ensures type correctness for function parameters and return values.
def save_json(path: Path, data: dict):
    """
    This function saves a Python dictionary as a JSON file.

    Args:
        path (Path): The path where the JSON file will be saved.
        data (dict): The dictionary that needs to be saved as JSON.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Dumps the dictionary into a JSON file with an indentation of 4 spaces.
    logger.info(f"JSON file saved at: {path}")  # Logs a message indicating where the JSON file was saved.

# Function to Load Data from a JSON File
@ensure_annotations
def load_json(path: Path) -> config_box:
    """
    This function loads data from a JSON file and returns it as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The JSON data as object attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)  # Loads the JSON content from the file.
    logger.info(f"JSON file loaded successfully from: {path}")  # Logs a success message.
    return config_box(content)  # Converts the dictionary to a ConfigBox object and returns it.

# Function to Save Data as a Binary File
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    This function saves any Python object as a binary file.

    Args:
        data (Any): The data to be saved as a binary file.
        path (Path): The path to the binary file.
    """
    joblib.dump(value=data, filename=path)  # Saves the data as a binary file using joblib.
    logger.info(f"Binary file saved at: {path}")  # Logs a message indicating where the binary file was saved.

# Function to Load Data from a Binary File
@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    This function loads data from a binary file.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The Python object stored in the file.
    """
    data = joblib.load(path)  # Loads the binary data using joblib.
    logger.info(f"Binary file loaded from: {path}")  # Logs a success message.
    return data  # Returns the loaded data.

# Function to Get the Size of a File in Kilobytes
@ensure_annotations
def get_size(path: Path) -> str:
    """
    This function returns the size of a file in kilobytes.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in kilobytes, rounded to the nearest integer.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculates the file size in kilobytes.
    return f"~ {size_in_kb} KB"  # Returns the size as a string.

# Function to Decode an Image from a Base64 String and Save it as a File
def decodeImage(Imgstring, fileName):
    """
    This function decodes a base64-encoded image string and saves it as a file.

    Args:
        Imgstring: The base64-encoded image string.
        fileName: The name of the file where the image will be saved.
    """
    imgdata = base64.b64decode(Imgstring)  # Decodes the base64 string into binary image data.
    with open(fileName, 'wb') as f:
        f.write(imgdata)  # Writes the binary image data to the specified file.
        f.close()  # Closes the file.

# Function to Encode an Image File into a Base64 String
def encodeImageIntoBase64(croppedImagePath):
    """
    This function encodes an image file into a base64 string.

    Args:
        croppedImagePath: The path to the image file that needs to be encoded.

    Returns:
        str: The base64-encoded string representation of the image.
    """
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())  # Reads the file and encodes it into a base64 string.
