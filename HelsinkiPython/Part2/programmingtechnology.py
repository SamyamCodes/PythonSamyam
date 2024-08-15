# Fix the program
number = int(input("Please type in a number: "))
if (number>100):
      print("The number was greater than one hundred")
      number -= 100
      print("Now its value has decreased by one hundred")
      print(f"Its value is now {number}")
print( f"{number} must be my lucky number!")
print("Have a nice day!")

# Programming exercise:
# Number of characters

# The function len can be used to find out the length of a string, among other things. 
# The function returns the number of characters in a string.
# Write your solution here
word = input("Please type in a word:")
if(len(word)>1):
    print(f"There are {len(word)} letters in the word {word}")
    print("Thank you!")
else:
    print("Thank you!")

# Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

# You can assume the number given by the user is always greater than zero.

# An example of expected behaviour:

# Sample output
# Please type in a number: 1.34
# Integer part: 1
# Decimal part: 0.34

# Write your solution here
number = float(input("Please type in a number:"))
print(f"Integer part: {int(number)}")
print(f"Decimal part: {number-int(number)}")
