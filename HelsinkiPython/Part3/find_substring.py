'''
The operator in returns a Boolean value, so it will only tell us 
if a substring exists in a string, but it will not be useful in finding out where 
exactly it is. 
Instead, the Python string method find can be used for this purpose.
 It takes the substring searched for as an argument, and returns either the first 
 index where it is found, 
 or -1 if the substring is not found within the string.
'''

input_string = "test"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))

input_string = "perpendicular"

while True:
    substring = input("What are you looking for? ")
    index = input_string.find(substring)
    if index >= 0:
        print(f"Found it at the index {index}")
    else:
        print("Not found")


'''
Sample output
What are you looking for? perp
Found it at the index 0
What are you looking for? abc
Not found
What are you looking for? pen
Found it at the index 3
'''


'''
Please write a program which asks the user to type in a string and a single character.
The program then prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. 
The program must print out three characters, or else nothing.

Pay special attention to when there are less than two characters left in the string after the
 first occurrence of the character looked for. 
 In that case nothing should be printed out, and there should not be any indexing 
 errors when executing the program.

Sample output
Please type in a word: mammoth
Please type in a character: m
mam

Sample output
Please type in a word: banana
Please type in a character: n
nan

Sample output
Please type in a word: tomato
Please type in a character: x

Sample output
Please type in a word: python
Please type in a character: n
'''

# Find the first substring
# Write your solution here
ask = input("Please type in a word:")
car = input("Please type in a character:")

index = ask.find(car)
end_index = index +3
to_print = ask[index:end_index]
if(len(to_print)>=3):
    print(to_print)
else:
    print("")
    