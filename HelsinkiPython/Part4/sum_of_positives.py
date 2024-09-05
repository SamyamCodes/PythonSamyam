'''
Please write a function named sum_of_positives, which takes a list of integers as its argument. 
The function returns the sum of the positive values in the list.

my_list = [1, -2, 3, -4, 5]
result = sum_of_positives(my_list)
print("The result is", result)
Sample output
The result is 9
'''
# Write your solution here
def sum_of_positives(lst):
    sums = 0
    for x in lst:
        if x > 0:
            sums += x
        else:
            continue
    return sums  


def main():
    my_list = [1,-2, 3,-4,5]
    result = sum_of_positives(my_list)
    print("The result is", result)

if __name__ == "__main__":
    main()