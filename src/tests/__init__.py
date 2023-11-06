import os
import sys

def get_path():
    PROJECT_PATH = os.getcwd()
    SOURCE_PATH = os.path.join(
        PROJECT_PATH, "src/implementation"
    )
    sys.path.append(SOURCE_PATH)