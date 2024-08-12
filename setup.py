import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-disease-classification---DL"
AUTHOR_USER_NAME = "AbdulQadir"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "aq452831@gmail.com"

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