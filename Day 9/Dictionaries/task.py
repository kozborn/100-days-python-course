programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


for student in student_scores:
    score = student_scores[student]
    if score <= 70:
        student_scores[student] = "Fail"
    elif 71 < score <= 80:
        student_scores[student] = "Acceptable"
    elif 81 < score <= 90:
        student_scores[student] = "Exceeds Expectations"
    elif 91 < score <= 100:
        student_scores[student] = "Outstanding"
print(student_scores)