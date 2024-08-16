# Write your solution here
print("hi")
while True:
    ask = input("Shall we continue?")
    if (ask == "no"):
        break
    else:
        print("hi")
print("okay then")


from math import sqrt

while True:
    num = int(input("Please type in a number: "))
    
    if num < 0:
        print("Invalid number")
    elif num > 0:
        print(sqrt(num))
    else:
        print("Exiting...")
        break
