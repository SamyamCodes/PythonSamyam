# Programming exercise:
# Calculator
# Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

# Some examples of expected behaviour:

# Sample output
# Number 1: 10
# Number 2: 17
# Operation: add

# 10 + 17 = 27

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: multiply

# 4 * 6 = 24

# Sample output
# Number 1: 4
# Number 2: 6
# Operation: subtract

# 4 - 6 = -2

# Write your solution here
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = input("Operation:")
if(operation == "add"):
    print(f"{num1} + {num2} = {num1+num2}")
elif(operation == "multiply"):
    print(f"{num1} * {num2} = {num1*num2}")
elif(operation == "subtract"):
    print(f"{num1} - {num2} = {num1-num2}")
else:
    print("")



# Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# The formula for converting degrees Fahrenheit to degrees Celsius can be found easily by any search engine of your choice.

# Two examples of expected behaviour:

# Sample output
# Please type in a temperature (F): 101
# 101 degrees Fahrenheit equals 38.333333333333336 degrees Celsius

# Please type in a temperature (F): 21
# 21 degrees Fahrenheit equals -6.111111111111111 degrees Celsius
# Brr! It's cold in here!

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Ask the user for temperature in Fahrenheit
fahrenheit = float(input("Please type in a temperature (F): "))

# Convert the temperature to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Print the result
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

# Check if the temperature is below 0 degrees Celsius and print a message
if celsius < 0:
    print("Brr! It's cold in here!")

# Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

# Sample output
# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros

# Sample output
# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros

# Function to calculate daily wages
def calculate_wages(hourly_wage, hours_worked, day_of_week):
    # If the day is Sunday, double the hourly wage
    if day_of_week.lower() == "sunday":
        hourly_wage *= 2
    # Calculate daily wages
    daily_wages = hourly_wage * hours_worked
    return daily_wages

# Ask the user for the hourly wage, hours worked, and day of the week
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_week = input("Day of the week: ")

# Calculate the daily wages
daily_wages = calculate_wages(hourly_wage, hours_worked, day_of_week)

# Print the result
print(f"Daily wages: {daily_wages} euros")

# Square Root
from math import sqrt

# Getting input values for a, b, and c
a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))

# Calculating the discriminant
discriminant = b**2 - 4*a*c

# Calculating the two roots using the quadratic formula
root1 = (-b + sqrt(discriminant)) / (2*a)
root2 = (-b - sqrt(discriminant)) / (2*a)

# Printing the roots
print(f"The roots are {root1} and {root2}")
