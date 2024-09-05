'''
Please write a function named list_of_stars, which takes a list of integers as its argument. 
The function should print out lines of star characters. 
The numbers in the list specify how many stars each line should contain.

For example, with the function call list_of_stars([3, 7, 1, 1, 2]) the following should be printed out:

Sample output
***
*******
*
*
**
'''
# Write your solution here
def list_of_stars(lst):
    for ls in lst:
        print("*"*ls)
if __name__ == "__main__":
    list_of_stars([3,7,1,1,2])
    