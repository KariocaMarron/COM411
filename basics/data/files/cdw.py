import os

def cdw():
    file_path = os.getcwd()
    print(f"The current working directory is {file_path}")

    print("the Directory Contains the following files:")

    for file in os.listdir(file_path):
        print(file)

def run():
        print("Processin...")
        cdw()

if __name__ == "__main__":
    run()


