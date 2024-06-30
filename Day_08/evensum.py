sum_even = 0
for number in range(0, 101):
    if(number % 2 == 0):
        sum_even = sum_even + number
print(f"The sum of even nnumber upto 100 is {sum_even}")


#Or, 
#This program could be written in this way as well.
sum=0
for number in range(2, 101, 2):
    sum+=number
print(sum)