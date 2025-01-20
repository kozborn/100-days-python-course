import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [80, 75, 98]
}

for(key, value) in student_dict.items():
    print(key, value)

student_df = pd.DataFrame(student_dict)
print(student_df)

for (key, value) in student_df.items():
    print(value)

for (index, row) in student_df.iterrows():



