import os  # Load os library


def cwd():
    path = os.getcwd()  # variable path = os(operating system).GetCurrentWorkDirectory
    print(f"The current file path is {path}")  # Command to display the path
    print("The directory contains contains the following files:")
    for file in os.listdir(path):  # Nested command to look for files in the previous path
        print(file)  # Display files

def run():
    print("Processing...")  # this
    cwd()


if __name__ == "__main__":
    run()
