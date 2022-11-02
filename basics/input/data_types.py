# Ask for the name
print("What is your name human?\n")
name = str(input())

print("How old are you (in years)?\n")
age = int(input())

print("How tall are you (in meters)?\n")
height = float(input())

print("How much do you weigh (in kilograms)?\n")
weight = int(input())

BMI = weight / (height ** 2)

print(f"\t\n{name} you are {age} years old and your bmi is {BMI}.")