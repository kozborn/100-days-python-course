from art import logo, vs
from game_data import data
import random

print(logo)

def get_pair(init_a):

    if init_a is None:
        a = data[random.randint(0, len(data)-1)]
    else:
        a = init_a

    b = data[random.randint(0, len(data)-1)]

    return a, b


def print_items(item_a, item_b):
    print(f"Compare A {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(vs)
    print(f"Against B {item_b['name']}, a {item_b['description']}, from {item_b['country']}")

def game():
    game_continue = True
    points = 0
    init_a = None
    while game_continue:
        a, b = get_pair(init_a)

        pair = {
            'a' : a,
            'b': b
        }

        print_items(a, b)
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice not in ['a', 'b']:
            game_continue = False
            print("Sorry, that's not a valid option.")

        if choice == 'a':
            comparator = 'b'
        else :
            comparator = 'a'

        if pair[choice]['follower_count'] > pair[comparator]['follower_count']:
            points += 1
            print(f"You're right! Current score: {points} points.")
            init_a = b
        else:
            print(f"Sorry, you've lost {pair[choice]['follower_count']} followers. vs {pair[comparator]['follower_count']}")
            game_continue = False

game()









