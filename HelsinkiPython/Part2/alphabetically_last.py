# Python comparison operators can also be used on strings. 
# String a is smaller than string b if it comes alphabetically before b. 
# Notice however that the comparison is only reliable if the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
# only the standard English alphabet of a to z, or A to Z, is used.
# Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

# You can assume all words will be typed in lowercase entirely.


# Write your solution here
string1 = input("Please type in the 1st word:")
string2 = input("Please type in the 2nd word:")
if(string1 > string2):
    print(f"{string1} comes alphabetically last.")
elif(string2 > string1):
    print(f"{string2} comes alphabetically last.")
else:
    print("You gave the same word twice.")