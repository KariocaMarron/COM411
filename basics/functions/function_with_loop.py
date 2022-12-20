# Function with a simple parameter named plan
def cross_bridge(steps):
    # Determine and
    # Display each step
    for step in range (steps):
        print("Crossed step.")

    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")

# calls to function
cross_bridge(3)
cross_bridge(6)
