'''
Please write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character,
from the shortest to the longest. Have a look at the example below.

Sample output
Please type in a string: test
t
st
est
test
'''

# Write your solution here
ad = input("Please type in a string:")
s = len(ad)
for x in ad:
    print(ad[s:])
    s-=1
    if s==0:
        print(ad)

input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)

# The program below lets the user search for substrings 
# within a string hardcoded into the program:
input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    if substring in input_string:
        print("Found it")
    else:
        print("Not found")

