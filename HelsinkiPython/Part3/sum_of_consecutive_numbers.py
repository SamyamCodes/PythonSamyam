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
