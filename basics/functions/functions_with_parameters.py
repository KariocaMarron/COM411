#
def climb_ladder(steps_remaining, steps_crossed):
    # Compare and display a suitable message
    if steps_remaining > steps_crossed:

        print("Still some way to go")
    else:
        print("We are almost there!")

# Calls to function

climb_ladder(5, 3)
climb_ladder(2, 5)