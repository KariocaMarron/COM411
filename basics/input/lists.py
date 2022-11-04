units = ["C0M411", "COM452","COM452"] #this is a list

for u in units:
    print(u)
units.append("COMM500")
print(units)

units.pop(2)
print(units)


units = ("C0M411", "COM452","COM452") #this is a tuple - imutable --> read only!!!



leader = ("Jose","Home") # This is a tuple
name, place = leader

print(place)