# Ask user to define cover typy


print("Please enter the cover type (hard/soft)?")
cover_type = input()

if cover_type == "soft":
    print("is the book perfect bound?")
    perfect_bound = input()

    if perfect_bound == "yes":
        print("Soft cover perfect bound books are very familiar")

    else:
        print("Soft cover with coils or stitches are great for short books")

else:
    print("Books with hard covers can be very expensive")
