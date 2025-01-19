with open("weather_data.csv") as f:
    data = f.readlines()

print(data)

import csv

temperatures = []
with open("weather_data.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        temperatures.append(int(row[1]))


print(temperatures)
import pandas as pd

df = pd.read_csv("weather_data.csv")
print(type(df))
print(type(df["temp"]))

print(sum(df["temp"].to_list())/len(df["temp"].to_list()))
print(df["temp"].mean())
print(df["temp"].min())
print(df["temp"].max())

monday = df[df.day == "Monday"]
temp = df[df.temp == 24]

print((monday["temp"] * 9/5) + 32)

data_dicts = {
    "students": ["Amy", "Frank", "Peter"],
    "scores": [90, 70, 60],
}

scores_df = pd.DataFrame(data_dicts)
print(scores_df)
scores_df.to_csv("scores.csv")







