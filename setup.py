# Importing the setuptools Library
# setuptools: This is a library used to package Python projects, making them easy to distribute and install. 
# It helps define the package metadata and dependencies.
import setuptools

#Reading the README.md File:
with open("README.md", "r", encoding="utf-8") as f: #Opens the "README.md" file in "read" mode with UTF-8 encoding.
    long_description = f.read() #Reads the content of the README.md file and stores it in the variable

# Defining the Package Version:
__version__ = "0.0.0" # Specifies the current version of the package

# Setting Up Package Metadata
REPO_NAME = "Chicken-disease-classification---DL"
AUTHOR_USER_NAME = "AbdulQadir"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "aq452831@gmail.com"

# Calling setuptools.setup()
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Python Package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This line was corrected from "long_description_content" to "long_description_content_type"
    package_dir={"": "src"},  # Changed the set {} to a dictionary {}
    packages=setuptools.find_packages(where="src"),
)