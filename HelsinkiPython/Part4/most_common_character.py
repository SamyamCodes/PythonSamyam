'''
Please write a function named most_common_character, which takes a string argument. 
The function returns the character which has the most occurrences within the string. 
If there are many characters with equally many occurrences, 
the one which appears first in the string should be returned.

An example of expected behaviour:

first_string = "abcdbde"
print(most_common_character(first_string))

second_string = "exemplaryelementary"
print(most_common_character(second_string))
Sample output
b
e
'''


# Write your solution here
def most_common_character(lst):
    most_count = 0
    most_char = ''
    for item in lst:
        count = lst.count(item)
        if count > most_count:
            most_count = count
            most_char = item
    return  most_char
        

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))