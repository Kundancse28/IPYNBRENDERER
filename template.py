import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format =  "[%(asctime)s: %(levelname)s]:%(message)s"
)
while True:
    project_name = input("Enter the Project Name:  ")
    if project_name != '':
        break
    
logging.info(f"Creating project by name: {project_name}")

#list of file
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    'setup.cfg',
    'tox.ini'
]    

for filepath in list_of_files:
    filedir, filename = os.path.split(Path(filepath))
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a directory at: {filedir}  for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a file at: {filepath}")
    else:
        logging.info(f"File already present at: {filepath}")
        