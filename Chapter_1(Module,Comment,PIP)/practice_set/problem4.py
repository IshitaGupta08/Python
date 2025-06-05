#WAP to print the contents of the directory used os module. search online for the function which does that

import os

# Get current working directory
current_dir = os.getcwd()

# List all files and folders in the current directory
contents = os.listdir(current_dir)

print("Contents of the directory:")
for item in contents:
    print(item)
