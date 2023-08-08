"""Exercise 6: Recursive File Search
Write a function that searches for all files with a given
extension (e.g., ".txt") in a directory and its subdirectories.
Print the full paths of these files."""

import os

def search_files_by_extension(directory, extension):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                print(file_path)

# Example usage:
directory_to_search = "C:\Users\edwar\OneDrive\Desktop\test"
file_extension = ".txt"
search_files_by_extension(directory_to_search, file_extension)
