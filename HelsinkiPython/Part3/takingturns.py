'''
Please write a program which asks the user to type in a number.
The program then prints out the positive integers between 1 and the number itself,
alternating between the two ends of the range as in the examples below.

Sample output
Please type in a number: 5
1
5
2
4
3

Sample output
Please type in a number: 6
1
6
2
5
3
4
'''


# Ask the user to type in a number
num = int(input("Please type in a number: "))

# Initialize the starting (low) and ending (high) numbers
low = 1
high = num

# Loop to alternate between low and high
while low <= high:
    print(low)   # Print the low end of the range
    if low != high:
        print(high)  # Print the high end of the range if they are not the same
    low += 1   # Move low up
    high -= 1  # Move high down
