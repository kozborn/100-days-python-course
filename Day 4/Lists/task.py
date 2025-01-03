import random
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland"]

for state in states_of_america:
    print(state)


print(states_of_america)

states_of_america.remove("Pennsylvania")
print(states_of_america)
states_of_america.append("New Jersey")
print(states_of_america)

print(len(states_of_america))

random_state = states_of_america[random.randint(0, len(states_of_america)-1)]
print(random_state)





