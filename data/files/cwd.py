import os  # Load os library


def cwd():
    path = os.getcwd()
    print(f"The current file path is {path}")
    print("The directory contains contains the following files:")
    for file in os.listdir(path):
        print(file)

def run():
    print("Processing...")
    cwd()


if __name__ == "__main__":
    run()
