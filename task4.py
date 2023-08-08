"""
Now write another function named classify that takes a dictionary like this one:

{
    "directory_name": ["file_name_1", "file_name_2"]
}
The function should move each file to the appropriate directory.

Use the constant DATA_ROOT to make sure the function will not move the files outside the working directory.

Use the following dictionary to test it on the data:

categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}
Once executed, the directory tree of the initial directory should look like this:
+ initial
  + personal
    - bookmarks.txt
    - todos.txt
  + work
    - customers.csv
    - jobs.csv

"""

# Solution
import os
import shutil

# Define the ROOT constant pointing to the current script's path
ROOT = os.path.abspath(os.path.dirname(__file__))
# Define the DATA_ROOT constant based on the ROOT constant
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

def classify(file_dict):
    for directory_name, file_names in file_dict.items():
        directory_path = os.path.join(DATA_ROOT, directory_name)
        
        # Check if the directory exists, if not create it
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        
        # Move each file to its appropriate directory
        for file_name in file_names:
            source_path = os.path.join(DATA_ROOT, 'personal', file_name)
            destination_path = os.path.join(directory_path, file_name)
            
            # Check if the file exists before moving
            if os.path.exists(source_path) and os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved '{file_name}' to '{directory_name}' directory.")
            else:
                print(f"File '{file_name}' not found.")

# Dictionary of categories and corresponding files
categories = {
    "personal": ["todos.txt", "bookmarks.txt"],
    "work": ["customers.csv", "jobs.csv"]
}

# Call the function to move files to their appropriate directories
classify(categories)

