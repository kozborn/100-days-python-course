logo = """
________        .__         ________                       
\_____  \  __ __|__|_______/  _____/_____    _____   ____  
 /  / \  \|  |  \  \___   /   \  ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /\    \_\  \/ __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \______  (____  /__|_|  /\___  >
       \__>              \/       \/     \/      \/     \/ """

print(logo)

class User:
    name = ""
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age


u = User("Piotrek", 38)
print(u)
