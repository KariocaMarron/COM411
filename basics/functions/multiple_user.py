

def display_box(name):
    message = f"* Hello {name} *"
    print("=" * len(message))
    print(message)
    print("*" * len(message))


def great_user():
    print("Please enter your name")
    name = input()
    display_box(name)


great_user()