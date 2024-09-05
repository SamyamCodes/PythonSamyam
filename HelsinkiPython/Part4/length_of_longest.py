'''
Finding the best or the worst item in a list
A very common programming task is finding the best or worst item in a list, according to some criteria. 
A simple solution is using a helper variable to "remember" which of the items processed so far was the most 
suitable. This temporary best choice is then compared to each item in turn, and at the end of the iteration 
the variable contains the best of the bunch.

A rough draft which doesn't quite compile yet:

best = initial_value # The initial value depends on the situation
for item in my_list:
    if item is better than best:
        best = item

# We now have the best one figured out!
The details of the final program code depend on the type of the items in the list, and also on the criteria 
for choosing the best (or worst) item. Sometimes you may need more than one helper variable.

Let's practice this method a little.
'''

'''
Please write a function named length_of_longest, which takes a list of strings as its argument. The function returns the length of the longest string.

my_list = ["first", "second", "fourth", "eleventh"]

result = length_of_longest(my_list)
print(result)
my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

result = length_of_longest(my_list)
print(result)
Sample output
8
7
'''

def length_of_longest(lst):
    longest = 0
    for item in lst:
        if len(item) > longest:
            longest = len(item)
    return longest

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)  

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result) 