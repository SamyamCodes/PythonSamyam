# Please write a program which asks the user for their age. The program should then print out a message based on whether the user is of age or not, using 18 as the age of maturity.

# Some examples of expected behaviour:

# Sample output
# How old are you? 12
# You are not of age!

# Sample output
# How old are you? 32
# You are of age!

# Write your solution here
age = int(input("How old are you?"))
if (age>=18):
    print("You are of age!")
else:
    print("You are not of age!")

# Programming exercise:
# Greater than or equal to
# Please write a program which asks for two integer numbers. 
# The program should then print out whichever is greater. 
# If the numbers are equal, the program should print a different message.

# Write your solution here
num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in another number:"))
if(num1 > num2):
    print(f"The greater number was: {num1}")
elif(num2 > num1):
    print(f"The greater number was: {num2}")
elif(num1 == num2):
    print(f"The numbers are equal!")

# Please write a program which asks for the names and ages of two persons. 
# The program should then print out the name of the elder.

# Write your solution here
print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))
print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))
if(age1> age2):
    print(f"The elder is {name1}")
elif(age1 < age2):
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")
    
