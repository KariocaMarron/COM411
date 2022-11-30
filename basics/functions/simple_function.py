def ascii_converter():
    print("Program Started")
    print("Please, enter an ASCii code")

    code = int(input())

    if code >= 32 and code <= 125:
        print(f"The character represented by the {code} is: {chr(code)} ")
        print("\n\n\t\t\tProgram Ending!!!")

ascii_converter()  # Calling the function
