#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = open('./Input/Names/invited_names.txt', 'r').read().splitlines()

letter_template = open('./Input/Letters/starting_letter.txt', 'r').read()

for name in names:
    filled_letter = letter_template.replace('[name]', name)
    print(filled_letter)
    with open(f"./Output/ReadyToSend/letter-for-{name.replace(' ', '_')}.txt", 'w') as file:
        file.write(filled_letter)






