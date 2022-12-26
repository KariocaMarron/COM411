import os

def cwd():
    path = os.getcwd()
    print("Current Working Directory: {path}")
    print("The directory contains the following files: ")

def run():
    print("processing...")
    cwd()
