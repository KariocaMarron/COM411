# Ask user for eye character
print("Please enter an eye character:")
eye = input()  # Insert an character for the eye.

# Ask user for the length of the glasses
print("Please enter the length of the glasses:")
length = int(input())

# Display ascii glasses
print()  # To insert a space

print(f"#########{' ' * length}#########")  # "{' ' * length} --> '  ' blank spaces to be left times
print(f"#   {eye}   {'#' * (length + 2)}   {eye}   #")
print(f"#########{' ' * length}#########

print()