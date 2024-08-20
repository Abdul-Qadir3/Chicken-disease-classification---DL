# Importing the setuptools Library
# setuptools: This is a library used to package Python projects, making them easy to distribute and install. 
# It helps define the package metadata, dependencies, and other configurations required for distribution.
import setuptools

# Reading the README.md File:
# This block opens the "README.md" file in "read" mode with UTF-8 encoding and reads its content.
# The content is typically used as the long description of the package, which will be displayed on the package's page (e.g., on PyPI).
with open("README.md", "r", encoding="utf-8") as f: 
    long_description = f.read()  # Reads the content of the README.md file and stores it in the variable 'long_description'

# Defining the Package Version:
# This variable specifies the current version of the package. It's important to update this version with each new release.
__version__ = "0.0.0"  # Specifies the initial version of the package

# Setting Up Package Metadata
# These variables define the metadata for the package, including the repository name, author's username, source repository name, and author email.
REPO_NAME = "Chicken-disease-classification---DL"  # The name of the GitHub repository
AUTHOR_USER_NAME = "Abdul-Qadir3"  # The username of the author (likely GitHub username)
SRC_REPO = "cnnClassifier"  # The name of the source repository or the main package directory
AUTHOR_EMAIL = "aq452831@gmail.com"  # The email address of the author

# Calling setuptools.setup()
# This function is used to define and set up the package metadata and configuration for distribution.
# It's the main function that setuptools uses to gather all the information about your package.
setuptools.setup(
    name=SRC_REPO,  # The name of the package; usually the same as the source repository
    version=__version__,  # The version of the package
    author=AUTHOR_USER_NAME,  # The name or username of the package author
    author_email=AUTHOR_EMAIL,  # The author's email address
    description="Python Package for CNN app",  # A short description of the package
    long_description=long_description,  # The detailed description, typically from README.md
    long_description_content_type="text/markdown",  # The format of the long description (usually Markdown)
    package_dir={"": "src"},  # Specifies that the root package is in the "src" directory
    packages=setuptools.find_packages(where="src"),  # Automatically finds all packages inside the "src" directory
)