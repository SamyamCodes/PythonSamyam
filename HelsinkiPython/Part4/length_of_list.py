'''
Just like the built-in functions above, our own functions can also take a list as an argument and produce a list as a return value. 
The following function works out the central value in an ordered list, also called the median value:

def median(my_list: list):
    ordered = sorted(my_list))
    list_centre = len(ordered) // 2
    return ordered[list_centre]
The function creates an ordered version of the list given as an argument and returns the item in the very middle. 
Notice the integer division operator // used here. The index of a list should always be an integer.

The function works like this:

shoe_sizes = [45, 44, 36, 39, 40]
print("The median of the shoe sizes is", median(shoe_sizes))

ages = [1, 56, 34, 22, 5, 77, 5]
print("The median of the ages is", median(ages))
Sample output
The median of the shoe sizes is 40
The median of the ages is 22

A function can also return a list. The following function asks the user to type in integers and returns the input as a list:

def input_numbers():
    numbers = []
    while True:
        user_input = input("Please type in an integer, leave empty to exit: ")
        if len(user_input) == 0:
            break
        numbers.append(int(user_input))
    return numbers
The function makes use of a helper variable numbers, which is a list. 
All the numbers typed in by the user are added to the list. 
When the loop is exited from, the function returns the list with the statement return numbers.

Calling the function like this

numbers = input_numbers()

print("The greatest number is", max(numbers))
print("The median of the numbers is", median(numbers))
could print this, for example:

Sample output
Please type in an integer, leave empty to exit: 5
Please type in an integer, leave empty to exit: -22
Please type in an integer, leave empty to exit: 4
Please type in an integer, leave empty to exit: 35
Please type in an integer, leave empty to exit: 1
Please type in an integer, leave empty to exit:
The greatest number is 35
The median of the numbers is 4

This small example demonstrates one of the most important uses of functions: they can help you divide your code into smaller, 
easily understandable and logical wholes.

Of course the same functionality could be achieved without writing any of our own functions:

numbers = []
while True:
    user_input = input("Please type in an integer, leave empty to exit: ")
    if len(user_input) == 0:
        break
    numbers.append(int(user_input))

ordered = sorted(numbers)
list_centre = len(ordered) // 2
median = ordered[list_centre]

print("The greatest number is", max(numbers))
print("The median of the numbers is", median)
In this version, following the programming logic is more difficult, as it is no longer clear which commands are a part of which 
functionality. The code fulfils the same purposes - reading in input, calculating the median value, and so on - but the structure is 
less clear.

Organising your code into separate functions will improve you program's readability, but also make it easier to handle logical wholes. 
This in turn helps you verify that the program works as intended, as each function can be tested separately.

Another important use for functions is making code reusable. If you need to achieve some functionality multiple times in your program, 
it is a good idea to create your own function and name it appropriately:

print("Shoe sizes:")
shoe_sizes = input_numbers()

print("Weights:")
weights = input_numbers()

print("Heights:")
heights = input_numbers()
Programming exerc

'''

# Write your solution here
def length(lst):
    return len(lst)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)

'''
Please write a function named mean, which takes a list of integers as an argument. 
The function returns the arithmetic mean of the values in the list.

my_list = [1, 2, 3, 4, 5]
result = mean(my_list))
print("mean value is", result)
Sample output
mean value is 3.0
'''
# Write your solution here
def mean(lst):
    orderd = sorted(lst)
    sums = sum(lst)
    x = sums / len(lst)
    return x
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)

# To determine the range of the list.
# Write your solution here
def range_of_list(lst):
    maxx = max(lst)
    minn = min(lst)
    x = maxx - minn
    return x
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)