'''
Please write a function named distinct_numbers, which takes a list of integers as its argument. 
The function returns a new list containing the numbers from the original list in order of magnitude, 
and so that each distinct number is present only once.

my_list = [3, 2, 2, 1, 3, 3, 1]
print(distinct_numbers(my_list)) # [1, 2, 3]

'''


# Write your solution here
def distinct_numbers(lst):
    return sorted(set(lst))
    
if __name__ =="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))

# Model Solution
def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
 
    results.sort()
    return results