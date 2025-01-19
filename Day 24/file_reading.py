# file = open('./my_file.txt')
# contents = file.read()
# print(contents)
#
# file.close()


with open("./my_file.txt", mode="a") as file:
    file.write("\nAnd I drive 20 years old Ford Mondeo")


with open("./my_file.txt") as file:
    content = file.read()
    print(content)
