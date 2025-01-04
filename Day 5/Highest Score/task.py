student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

total_score = sum(student_scores)
sum = 0

for score in student_scores:
    sum += score

print(total_score, sum)

max_score = max(student_scores)
my_max = student_scores[0]
for score in student_scores:
    if score > my_max:
        my_max = score


print(my_max, max_score)
