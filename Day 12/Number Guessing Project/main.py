import random

logo = """
  ________                            ___________.__            _______               ___.                 
 /  _____/ __ __   ____   ______ _____\__    ___/|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ |    |   |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  |    |   |   Y  \  ___//    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > |____|   |___|  /\___  >____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                \/     \/        \/            \/    \/     \/ 
"""


print("Welcome to Number Guessing Project!")
computer_number = random.randint(1, 100 + 1)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. (easy or hard)").lower()

lives = None
tries = 0
if difficulty == "easy":
    lives = 10
elif difficulty == "hard":
    lives = 5
else:
    lives = 0

while lives > 0:
    guess = int(input("Guess a number between 1 and 100: "))
    tries += 1
    if guess == computer_number:
        print(f"You guessed the number {computer_number} in {tries} lives.")
        break
    elif guess < computer_number:
        print("Your guess is too low.")
        lives -= 1
    elif guess > computer_number:
        print("Your guess is too high.")
        lives -= 1
    print(f"You have {lives} lives left.")





