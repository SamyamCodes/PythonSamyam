student_scores = input("Enter the students scores list").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# To determine the highest score

highest_score = 0
for score in student_scores:
    if (score > highest_score):
        highest_score = score
print (f"The highest score is {highest_score}")

