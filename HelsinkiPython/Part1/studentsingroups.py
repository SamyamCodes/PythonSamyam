# Programming exercise:
# Students in groups

# Please write a program which asks for the number of students on a course and the desired group size.
# The program will then print out the number of groups formed from the students on the course. 
# If the division is not even, one of the groups may have fewer members than specified.

# If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. 
# The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

# Sample output
# How many students on the course? 8
# Desired group size? 4
# Number of groups formed: 2

# Write your solution here
students = int(input("How many students on the course?"))
desired = int(input("Desired group size?"))
if ((students%desired) == 0):
    print(f"Number of groups formed: {students/desired}")
else:
    print(f"Number of groups formed: {int((students/desired) + 1)}")

name = input("Please tell me your name:")
if(name == "Jerry"):
    print("Next please!")
else:
    n = int(input("How many portions of soup?"))
    print(f"The total cost is {5.90*n}")
    print("Next please!")
