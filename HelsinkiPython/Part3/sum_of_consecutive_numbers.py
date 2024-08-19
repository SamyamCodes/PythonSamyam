up = int(input("Limit:"))
sums = 0
current_number = 1
strings = ""

while sums < up:
    sums+= current_number
    if strings == "" :
        strings += str(current_number)
    
    else:
        strings += " + " + str(current_number)
    
    current_number += 1
print(f"The consecutive sum : {strings} = {sums}")

'''
The * operator can also be used with a string, when the other operand is an integer. 
The string operand is then repeated the number of times specified by the integer. 
For example this would work:

word = "banana"
print(word*3)

Sample output
bananabananabanana
'''