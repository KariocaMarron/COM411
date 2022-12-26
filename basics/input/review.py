# Ask user for eye character
print("Please enter an eye character:")
eye = input()  # Insert an character for the eye.

# Ask user for the length of the glasses
print("Please enter the length of the glasses:")
length = int(input())

# Display ascii glasses
print()

print(f"#########{' ' * length}#########")
print(f"#   {eye}   {'#' * (length + 2)}   {eye}   #")
print(f"#########{' ' * length}#########")

print()