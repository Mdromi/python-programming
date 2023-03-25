# python3 chapter-7/smallProject.py

import re
import os

def create_directory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name, 'already exists')

create_directory('chapter-7/public')