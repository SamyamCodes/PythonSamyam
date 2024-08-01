# def average(a= 9, b = 10): #Given default value of a and b. This is neglected if the value is provided in the argument by the user.
#     print("The average is ", (a+b)/2)

# average (5 , 3)

# def name( fname, mname = "Jhon", lname = "Watson"):
#     print("Hello, ", fname, mname, lname)

# name ("Sam", "Shrest" )

# Keyword Arguments

# average (b = 9, a = 22) # THe order doesnt matters here.

# def average(*numbers): #This creates tuple for variable number
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum / len(numbers))

# average (5,6,7,3)

# def name(**name): #This creates dictionary for variable number
#     print("Hello, ", name["fname"], name["lanme"], name["mname"])

# name(mname = "Samya,", lname = "Hoade", lname = "Opemnre")


# Return

def average(*numbers): #This creates tuple for variable number
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(4,3,42,22,12)
print(c)





