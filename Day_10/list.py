# This is Day 10
marks = [3,4,5, "Samyam", True]

# print(marks[0])

# if "Samyam" in marks:
#     print("Yes")
# else:
#     print("No")

# # Same thing applies for string as well.
# if "am" in "Samyam":
#     print("Yes")
# else:
#     print("No")

print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:4])
print(marks[1:4:2])

# List Comprehension
lst = [i*i for i in range(4)]
print(lst)
lst = [i*i for i in range(10) if (i % 2 == 0)]
print(lst)




