# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is like in {location}?")


greet_with("Jack","NYC")


def calculate_love_score(name1, name2):
    true_num = 0
    love_num = 0
    concatenated_names = name1 + name2
    for letter in "true":
        for name_letter in concatenated_names.lower():
            if letter == name_letter:
                true_num += 1

    for letter in "love":
        for name_letter in concatenated_names.lower():
            if letter == name_letter:
                love_num += 1

    print(str(true_num) + str(love_num))


calculate_love_score("Angela Yu", "Jack Bauer")
calculate_love_score("Kanye West", "Kim Kardashian")
