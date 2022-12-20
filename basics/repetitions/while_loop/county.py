# Ask a question to the user
print("How many live cables must I avoid?")

avoid_cables = int(input())


iterations = 1


while iterations <= avoid_cables:
    print(f"Avoiding {iterations} ", end="")
    print("on the same line")
    iterations = iterations +1


print("\t\t\t\t__________________________________________")
print("\n\t\t\t\t$$$$ All live cables have been removed $$$")
print("\t\t\t\t__________________________________________")

