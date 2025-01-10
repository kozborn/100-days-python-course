from turtle import Turtle

timmy = Turtle()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", 'Charmander'])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.add_row(["Piotrek", "Will"])

table.align = 'l'


print(table)