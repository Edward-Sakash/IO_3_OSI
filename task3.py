"""
Define a function named create_data_directories that takes a list of strings and creates a directory for each one (with the given name) in the directory src/data/initial.

The script will only create these directories if they do not exist. If they do, it will output a message saying The directory {directory} already exists.

Use the constant DATA_ROOT to make sure the function will not create directories outside the working directory.

Use the following list to call the function:

dirs = ["personal", "work"]
After executing your script, the directory tree should look like this:
+ initial
  + personal
  + work
  - todos.txt
  - jobs.csv
  - bookmarks.txt
  - customers.csv
Now, execute the script again, and you should see this message:
The directory personal already exists.
The directory work already exists.

"""

# Solution

import os

# Define the ROOT constant pointing to the current script's path
ROOT = os.path.abspath(os.path.dirname(__file__))

# Define the DATA_ROOT constant based on the ROOT constant
DATA_ROOT = os.path.join(ROOT, 'src', 'data', 'initial')

# Define the list of files to be created in each directory
files_to_create = ["todos.txt", "jobs.csv", "bookmarks.txt", "customers.csv"]

def create_data_directories(directory_names):
    # Create the 'initial' directory if it doesn't exist
    if not os.path.exists(DATA_ROOT):
        os.makedirs(DATA_ROOT)
    
    for directory_name in directory_names:
        directory_path = os.path.join(DATA_ROOT, directory_name)
        
        # Check if the directory already exists
        if os.path.exists(directory_path) and os.path.isdir(directory_path):
            print(f"The directory {directory_name} already exists.")
        else:
            try:
                os.mkdir(directory_path)
                print(f"Created directory: {directory_name}")
                for file_name in files_to_create:
                    file_path = os.path.join(directory_path, file_name)
                    open(file_path, 'w').close()  # Create an empty file
                    print(f"Created file: {file_name}")
            except OSError as e:
                print(f"An error occurred while creating {directory_name}: {e}")

# List of directory names to be created
dirs = ["personal", "work"]

# Call the function to create directories and files if they don't exist
create_data_directories(dirs)

