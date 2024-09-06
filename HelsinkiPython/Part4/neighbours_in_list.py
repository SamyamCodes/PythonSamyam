'''
Given a list of integers, let's decide that two consecutive items in the list are 
neighbours if their difference is 1. 
So, items 1 and 2 would be neighbours, and so would items 56 and 55.

Please write a function named longest_series_of_neighbours, which looks for the 
longest series of neighbours within the list, and returns its length.

For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours 
would be [5, 4, 3, 4], with a length of 4.

An example function call:

my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
print(longest_series_of_neighbours(my_list))
Sample output
4
'''

# # Write your solution here
# def longest_series_of_neighbours(lst):
#     if not lst:  # Handle empty list
#         return 0
#     longest = 1
#     current_length = 1
#     for i in range(1, len(lst)):
#         if abs(lst[i] - lst[i-1] ==1):
#             current_length += 1
#         else:
#             longest = max(longest, current_length)
#             current_length += 1
#     longest = max(longest, current_length)
#     return longest

# if __name__ == "__main__":
#     my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
#     print(longest_series_of_neighbours(my_list))


def longest_series_of_neighbours(lst):
    if len(lst) < 2:
        return len(lst)  

    longest = 1  
    current_length = 1  

    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i - 1]) == 1:
            current_length += 1  
            longest = max(longest, current_length) 
        else:
            current_length = 1 

    return longest

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list)) 
