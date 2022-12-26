import random

# Ask for a minimum value
print("Please enter the minimum value: ")
# min-value is a integer defined by user
min_value = int(input())

# Ask for a maximum value
print("Please enter the maximum value: ")
# max-value is a integer defined by user
max_value = int(input())

# Define a random number
random_number = random.randrange(min_value, max_value)

print(f"I am thinking of a number between {min_value} and {max_value}.")

print("can you guess what it is?")

guessed_correctly = False

while not guessed_correctly:
    print("Please enter a number: ")
    guess = int(input())

    if guess == random_number:
        print("Congratulations! You guessed the correct answer!")
        guessed_correctly = True

    elif guess < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print("game over!")