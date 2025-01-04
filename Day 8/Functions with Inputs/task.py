def greet(name):
    print(f"Hello, {name}")

name = input("What is your name? ")
greet(name)


def life_in_weeks(age):
    rest_life_in_weeks = (90 - age) * 52
    print(f"You have {rest_life_in_weeks} weeks left.")

your_age = int(input("What is your age?"))
life_in_weeks(your_age)

