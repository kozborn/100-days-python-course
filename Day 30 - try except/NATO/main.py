import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

alphabet_df = pd.read_csv('nato_phonetic_alphabet.csv')
# print(alphabet_df)
#TODO 1. Create a dictionary in this format:
alphabet = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}
# print(alphabet)

user_input = input("Enter a word: \n").upper()
result = [alphabet[letter] for letter in user_input]
print(result)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

