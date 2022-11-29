# Ask a user for a number

print("Please, enter your namer\n")
name = str(input())

print("Enter a number\n")
number = int(input())

# Display relevant message

if number % 2 != 0:
    print(f"{name}, the Number {number} is an odd number")

elif number % 2 == 0:
    print(f'{name}, the Number {number} is an even numer')

else:
    print(f"This is not a whole numer {name}")















# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

#def animate(frame):
