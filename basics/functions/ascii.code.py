# ASCII Code

print("Program started")  # Message initiating the program

print("Please enter a standard character")  # Ask user to insert the character

character = input()  # Attributing a value to a variable  character

if len(character) == 1:
    print(f"The ASCII Code for {character} is {ord(character)}")
else:
    print("A single character was expected")

print("program ended")
