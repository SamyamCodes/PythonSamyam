'''
Please write a program which asks the user to type in a number. 
The program then prints out all the positive integer values from 1 up to the number.
However, the order of the numbers is changed so that each pair or numbers is flipped. That is, 2 comes before 1, 4 before 3 and so forth. 
See the examples below for details.
Please type in a number: 5
2
1
4
3
5

Sample output
Please type in a number: 6
2
1
4
3
6
5
'''

# Write your solution here

# Ask the user to type in a number
num = int(input("Please type in a number: "))

# Initialize a variable to track the current number
i = 1

# Loop through numbers from 1 up to the user's input
while i <= num:
    # If the next number is within the range, print the next number first
    if i + 1 <= num:
        print(i + 1)
    # Print the current number
    print(i)
    # Increment by 2 to handle the next pair
    i += 2

