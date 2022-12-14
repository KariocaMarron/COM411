# Transforming to a function

def cables():

    # Ask how many cables to remove
    print("How many cables should I remove?")

    # Defining variable iterations at initial value 0
    iterations = 0

    # Define variable amount_cab
    amount_cab = int(input())

    print(f"\t\tStart removing ** {amount_cab} ** cables\n")

    # Count how many cables user input
    while iterations < amount_cab:

        iterations = iterations + 1
        print("Cable removed\n")



    print(f"All the **_ {amount_cab} _** cables were removed as requested!")

# Call the function
cables()
cables()
cables()
