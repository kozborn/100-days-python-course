import random
from art import logo

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 # BLACKJACK

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        print("Draw")
    elif dealer_score == 0:
        print("Lose, opponent has Blackjack 😭")
    elif user_score == 0:
        print("Win with a Blackjack 😎")
    elif user_score > 21:
        print("You went over 21. You lose :(")
    elif dealer_score > 21:
        print("Computer went over 21. You win :)")
    elif user_score > dealer_score:
        print("You win")
    else:
        print("You lose")

def game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    dealer_cards = []
    print("\n" * 20)
    print(logo)
    playing = True

    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))

    while playing:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Dealer first card: {dealer_cards[0]}")
        deal_card = input("Play another card? Type 'y' or 'n': ")
        if deal_card == 'y':
            user_cards.append(random.choice(cards))

            if calculate_score(user_cards) > 21:
                playing = False
                print(f"You lose! {user_cards} with {sum(user_cards)} points")
        else:
            playing = False

    user_final_score = calculate_score(user_cards)

    while calculate_score(dealer_cards) != 0 and calculate_score(dealer_cards) < 17:
        dealer_cards.append(random.choice(cards))

    dealer_final_score = calculate_score(dealer_cards)
    print("User cards: ", user_cards, " final score: ", user_final_score)
    print("Dealer cards: ", dealer_cards, " final score: ", dealer_final_score)

    compare(user_final_score, dealer_final_score)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ").lower() == "y":
    game()

