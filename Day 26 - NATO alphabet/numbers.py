numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = []
for number in numbers:
    new_list.append(number + 1)


def add(number1, number2):
    return number1 + number2

def add_two(number):
    return add(number, 2)

another_list = [add_two(item) for item in numbers]
print(numbers)
print(new_list)
print(another_list)

name = "Piotrek"
new_list = [letter for letter in name]
print(new_list)

squared_list = [number * 2 for number in range(1,5)]
print(squared_list)

#Conditional list comprehension

even_list = [number for number in range(1,15) if number % 2 == 0]
print(even_list)

names = ["Alex", 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

uppercase_long_names = [name.upper() for name in names if len(name) > 4]
print(uppercase_long_names)
