import random
names = ["Alex", 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

scores = { name: random.randint(1, 100) for name in names }

print(scores)
passed_students = {key: value for (key, value) in scores.items() if value >= 60}
print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split(' ')}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

def convert_to_f(temp):
    return temp * 9/5 + 32

weather_f = {day:convert_to_f(temp) for (day, temp) in weather_c.items()}

print(weather_f)