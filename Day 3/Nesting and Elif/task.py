print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))

    if age <= 12:
        price = 5
        print(f"Child tickets are ${price}")
    elif age <= 18:
        price = 8
        print(f"Adolescents tickets are ${price}")
    else:
        price = 10
        print(f"Adults tickets are ${price}")

    photo = input("Do you want a photo? (yes/no): ")
    if photo == "yes":
        price+= 3

    print(f"Total price: ${price}")


else:
    print("Sorry you have to grow taller before you can ride.")
