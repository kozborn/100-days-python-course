from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculate(first, second, operation):
    operations[operation](first, second)

should_program_continue = True
should_program_continue_with_previous_result = ""

first = None
second = None
operation = None

while should_program_continue:

    if not first:
        try:
            first = float(input("What is your first number? "))
        except ValueError:
            print("Sorry, I didn't understand that.")
            quit(1)

    operation = input("Pick operation? ('+', '-', '*', '/') ")

    try:
        second = float(input("What is your second number? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        quit(1)

    result = operations[operation](first, second)
    if operation in operations:
        print(f"{first} {operation} {second} = {result}")
    else:
        print("Invalid operation")
        quit(1)
    should_program_continue_with_previous_result = input("Would you like to continue with previous result as first number? (y/n) (q to quit): ").lower()

    if should_program_continue_with_previous_result not in ["y", "n"]:
        print("Thank you for using our calculator")
        should_program_continue = False
    elif should_program_continue_with_previous_result == "y":
        first = result
    else:
        print("\n"*20)
        print(logo)
        first = None
        second = None
        operation = None













