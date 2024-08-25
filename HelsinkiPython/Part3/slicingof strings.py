'''
If you know the beginning and end indexes of the slice 
you wish to extract, you can do so with the notation [a:b]. T
his means the slice begins at the index a and ends at 
the last character before index b - that is,
 including the first, but excluding the last
'''
input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])


'''
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character,
 from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
te
tes
test
'''

# Write your solution here
strings = input("Please type in a string:")
s= 1
for p in strings:
    print(strings[0:s])
    s+=1
