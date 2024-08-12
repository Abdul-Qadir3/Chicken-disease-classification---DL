# Importing necessary libraries
import os  # For interacting with the operating system (e.g., file and directory operations)
from pathlib import Path  # For handling file system paths in a way that's platform-independent
import logging  # For generating log messages to track the execution of the code

# Configuring the logging module to display messages with the INFO level or higher
# The format specifies how the log messages should look
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s')

# Defining the project name which will be used in the file paths
project_name = "cnnClassifier"

# List of files and directories to be created for the project
list_of_files = [
    ".github/workflows/.gitkeep",  # Placeholder file to keep empty directories in Git
    f"src/{project_name}/__init__.py",  # Initialization file for the project package
    f"src/{project_name}/components/__init__.py",  # Initialization file for the components module
    f"src/{project_name}/utils/__init__.py",  # Initialization file for the utils module (corrected typo from 'utiles')
    f"src/{project_name}/config/__init__.py",  # Initialization file for the config module
    f"src/{project_name}/config/configuration.py",  # Configuration script for the project
    f"src/{project_name}/pipeline/__init__.py",  # Initialization file for the pipeline module
    f"src/{project_name}/entity/__init__.py",  # Initialization file for the entity module
    f"src/{project_name}/constants/__init__.py",  # Initialization file for the constants module
    "config/config.yaml",  # Configuration file in YAML format
    "dvc.yaml",  # DVC (Data Version Control) pipeline file
    "params.yaml",  # Parameters file in YAML format
    "requirements.txt",  # File listing the project dependencies
    "setup.py",  # Script for installing the project as a package
    "research/trials.ipynb"  # Jupyter notebook for research or experimentation
]

# Loop through each file path in the list_of_files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object (platform-independent)
    filedir, filename = os.path.split(filepath)  # Split the path into directory and file name

    # If the directory part is not empty, create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory and any necessary parent directories
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # If the file doesn't exist or is empty, create an empty file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open the file in write mode
            pass  # No content is written, so the file remains empty
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and is not empty, log that information
    else:
        logging.info(f"{filename} already exists")


# For terminal only
# >>> from pathlib import Path    
# >>> path = "config/config.yaml"
# >>> Path(path)  
# WindowsPath('config/config.yaml')
# >>> import os
# >>> os.path.split(path)
# ('config', 'config.yaml')
# >>> os.path.getsize("README.md")