# Write your solution here
num = int(input("Number:"))
if(num % 3 == 0 and num % 5 == 0):
    print("FizzBuzz")
elif(num % 3 == 0):
    print("Fizz")
elif(num % 5 == 0):
    print("Buzz")
else:
    print("")

# Leap Year
# Write your solution here
'''
num = int(input("Please type in a year:"))
if(num % 100 == 0 and num % 400 == 0):
    print("That year is a leap year.")
else:
    print("That  year is not a leap year.")
       
if(num% 4 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
num = int(input("Please type in a year: "))

'''

if (num % 400 == 0) or (num % 100 != 0 and num % 4 == 0):
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")