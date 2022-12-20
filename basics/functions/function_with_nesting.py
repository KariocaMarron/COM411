# The function
def identity():
    # Ask user for what lies ahead
    print("What lies before us?")
    response = input()

    # Display message
    if response == "a large boulder":
        print("It's time to run")

    else:
        print("We will be fine.")


# To make the function run we have to "call the function"
identity()
