'''
Please write a program which finds the second occurrence of a substring.
If there is no second (or first) occurrence, the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. 
For example, in the string aaaa the second occurrence of the substring aa is at index 2.

Some examples of expected behaviour:

Sample output
Please type in a string: abcabc
Please type in a substring: ab
The second occurrence of the substring is at index 3.

Sample output
Please type in a string: methodology
Please type in a substring: o
The second occurrence of the substring is at index 6.

Sample output
Please type in a string: aybabtu
Please type in a substring: ba
The substring does not occur twice in the string.
'''




# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# Find the first occurrence of the substring
first_occurrence = string.find(substring)

if first_occurrence == -1:
    
    print("The substring does not occur twice in the string.")
else:

    second_occurrence = string.find(substring, first_occurrence + len(substring))
    
    if second_occurrence == -1:
       
        print("The substring does not occur twice in the string.")
    else:
        
        print(f"The second occurrence of the substring is at index {second_occurrence}.")
