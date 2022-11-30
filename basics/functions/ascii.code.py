# ASCII Code

print("Program started")

print("Please enter a standard character")

character = input()

if len(character) == 1:
    print(f"The ASCII Code for {character} is {ord(character)}")

else:
    print("A single character was expected")

print("program ended")
