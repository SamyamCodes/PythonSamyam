n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1


# Write your solution here
si = input("Please type in a string:")
amt = int(input("Please type in an amount:"))
print(si*amt)


input_string = input("Please type in a string: ")
print(input_string)
print("-"*len(input_string))


# Write your solution here
string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")

if (len(string1) > len(string2)):
    print(f"{string1} is longer")
elif (len(string2) > len(string1) ):
    print(f"{string2} is longer")
else:
    print("The strings are equally long")
    

input_string = input("Please type in a string: ")
print(input_string[0])
print(input_string[1])
print(input_string[3])

input_string = input("Please type in a string: ")
print("First character: " + input_string[0])
print("Last character: " + input_string[len(input_string) - 1])

# Prints from first to last.
input_string = input("Please type in a string: ")
index = 0
while index < len(input_string):
    print(input_string[index])
    index += 1

# Prints string from last to first
# Write your solution here
ask = input("Please type in a string:")
ste = len(ask)
while ste > 0:
    print(ask[ste - 1] )
    ste -= 1