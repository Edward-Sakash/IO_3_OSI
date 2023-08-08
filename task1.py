"""
Define a function named show_data_list that prints the contents of the directory src/data/initial.

Your result should look like this:
todos.txt
jobs.csv
bookmarks.txt
customers.csv
    
"""

# Solution

import os

def show_data_list():
    # Define the directory path
    directory = 'src/data/initial'
    
    # Check if the directory exists and is a directory
    if os.path.exists(directory) and os.path.isdir(directory):
        # List the contents of the directory
        contents = os.listdir(directory)
        
        # Iterate through the contents and print each item
        for item in contents:
            print(item)

# Call the function to display the contents of the directory
show_data_list()
