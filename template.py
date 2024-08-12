import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(ascitime)s] : %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utiles/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "confi/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"


]

# For terminal only
# >>> from pathlib import Path    
# >>> path = "config/config.yaml"
# >>> Path(path)  
# WindowsPath('config/config.yaml')
# >>> import os
# >>> os.path.split(path)
# ('config', 'config.yaml')
# >>> os.path.getsize("README.md")


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filename, "w") as f:
            pass
            logging.info(f"creating empty file : {filepath}")

    else:
        logging.info(f"{filename} is already exist")