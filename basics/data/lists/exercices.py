# Python program to explain os.listdir() method

# importing os module
import os

# Get the list of all files and directories
# in the root directory

file_path = os.getcwd()

print(f"Current Working Directory: ")

for file in os.listdir(path):