# Python file detection 

import os

file_path = "file/file.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
else:
    print("That location doesn't exist")
