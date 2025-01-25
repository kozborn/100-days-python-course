import pandas as pd
alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(alphabet_df)
#TODO 1. Create a dictionary in this format:
alphabet = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}
# print(alphabet)
def get_input_from_user():
    user_input = input("Enter a word: \n").upper()
    if user_input == 'EXIT':
        print("Thank you for using NATO alphabet converter, Bye")
        return None
    try:
        result = [alphabet[letter] for letter in user_input]
    except KeyError:
        print("Invalid input")
        get_input_from_user()
    else:
        print(result)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

get_input_from_user()