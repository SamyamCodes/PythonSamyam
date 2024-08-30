'''
the following program sums up numbers from input, but it only includes the 
numbers which are smaller than 10. If the number is 10 or greater, 
the execution jumps to the beginning of the loop and the number is not added to 
the sum.
'''

sum = 0

while True:
    number = int(input("Please type in a number, -1 to exit: "))
    if number == -1:
        break
    if number >= 10:
        continue
    sum += number

print (f"The sum is {sum}")