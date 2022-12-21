def display_ladder(steps):
    # Display each step
    for step in range(steps):
        print("| |")
        print("***")

    # Display bottom of the ladder
    print("| |")


def create_ladder():
    print("How many steps remaining?")
    steps = int(input())
    display_ladder(steps)


# Call the function
create_ladder()
