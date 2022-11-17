# Ask user to enter their name
#print("What is your name human?\n")
#name = input()
#print(f"It is nice to meet you human {name}")

def get_name():
    name = str(input("Please enter your name \n"))
    return name

def get_weight():
    weight = float(input("Please enter your weight\n"))
    return weight

def get_heigh():
    height = float(input("Please enter your height\n"))
    return height

def calculate_bmi(weight, height):
    bmi = float(weight / (height ** 2))
    return bmi

def run():
     name = get_name()
     weight = get_weight()
     height = get_heigh()
     bmi = calculate_bmi(weight,height)
     print("############################################")
     print("#                                          #")
     print(f"#      {name} your bmi is  {bmi}           #")
     print("#                                          #")
     print("############################################")


if __name__ == "__main__":
    run()