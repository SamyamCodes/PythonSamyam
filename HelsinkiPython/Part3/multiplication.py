'''
Please write a program which asks the user for a positive integer number. 
The program then prints out a list of multiplication operations until both operands 
reach the number given by the user. See the examples below for details:

Sample output
Please type in a number: 2
1 x 1 = 1
1 x 2 = 2
2 x 1 = 2
2 x 2 = 4

Sample output
Please type in a number: 3
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
'''

# Write your solution here

num = int(input("Please type in a number:"))
i = 1
while i<=num:
    j = 1
    while j <= num:
        print(f"{i} x {j} = {i*j}")
        
        if(j==num):
            break
        j+=1
        continue
    i+=1
    if i> num:
        break
        

