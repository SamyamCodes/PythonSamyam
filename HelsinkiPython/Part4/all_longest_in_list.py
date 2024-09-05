'''
Please write a function named all_the_longest, which takes a list of strings as its argument. 
The function should return a new list containing the longest string in the original list. 
If more than one are equally long, the function should return all of the longest strings.

The order of the strings in the returned list should be the same as in the original.

my_list = ["first", "second", "fourth", "eleventh"]

result = all_the_longest(my_list)
print(result) # ['eleventh']
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = all_the_longest(my_list)
print(result) # ['dorothy', 'richard']
'''
def all_the_longest(lst):
    if not lst:
        return []

    longest_strings = []
    max_length = 0

    for item in lst:
        length = len(item)
        if length > max_length:
            max_length = length
            longest_strings = [item]
        elif length == max_length:
            longest_strings.append(item)

    return longest_strings

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)  # Output: ['eleventh']

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)  # Output: ['dorothy', 'richard']
