# PROBLEM-2 : Write a python program to print the contents of a directory using the os module.Search online for the fuction which does that.

import os

# Select directory path
path = "C:/Users/dell/OneDrive/Desktop/Python"

# Get all files and folders
contents = os.listdir(path)

# Print contents
print("Contents of directory:")

for item in contents:
    print(item)