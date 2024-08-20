# Chicken-disease-classification---DL
### <b>Project Template creation:
- Instead of creating folder structure manually we will use `template.py` file (one time effort and can be reused)(And then run to create)
- A `template.py` file is typically a Python script that serves as a starting point or a skeleton for creating other Python scripts


`A template.py file is typically a Python script that serves as a starting point or a skeleton for creating other Python scripts. It usually contains a basic structure, common imports, placeholder functions, or other reusable code that can be modified or extended to suit specific needs.`

## Common Uses of template.py:
- `Project Skeleton:` It might include the basic setup code, such as importing necessary libraries, setting up logging, and defining the main function. This helps developers start a new script or module quickly without having to rewrite common boilerplate code.

- `Reusable Components:` The template might have predefined classes, functions, or configurations that are commonly used across different projects or tasks.

- `Customization Points:` It may include placeholders where specific code or logic needs to be filled in by the user. These placeholders are often marked with comments or special tags like TODO, indicating where the user should add or modify the code.

- `Consistency Across Projects:` Using a template.py file helps maintain consistency in coding style and structure across multiple scripts or projects within a team or organization.

### __init__.py (constructor file)
- `__init__.py` is a special file in Python that tells Python that a directory should be treated as a package. This allows the directory to be importable as a module in other Python scripts.

### Pathlib (library)
#### COMMANDS
- from pathlib import Path
- path = "config/config.yaml"
- Path(path)  #it will return windows path

### after applyig split function
- Import os
- os.import.split(path)
  - will return ('config','config.yaml')

## UTILS file
functions that are frequently used in the project

# WorkFlow

1. update config.yaml
2. update secrets.yaml [optional]
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the dvc.yaml