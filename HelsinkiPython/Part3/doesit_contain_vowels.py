'''
Please write a program which asks the user to input a string. 
The program then prints out different messages if the string contains 
any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. 
Have a look at the examples below.

Sample output
Please type in a string: hello there
a not found
e found
o found

Sample output
Please type in a string: hiya
a found
e not found
o not found
'''

# Write your solution here
ask = input("Please type in a string:")
s1 = "a"
s2 = "e"
s4 = "o"
while True:
    if s1 in ask and s2 in ask and s4 in ask:
        print("a found")
        print("e found")
        print("o found")
    
    elif s1 in ask and s2 in ask:
        print("a found")
        print("e found")
        print("o not found")
    elif s1 in ask and s4 in ask:
        print("a found")
        print("e not found")
        print("o found")

    elif s2 in ask and s4 in ask:
        print("a not found")
        print("e found")
        print("o found")  

    elif s1 in ask:
        print("a found")
        print("e not found")
        print("o not found")
        
    elif s2 in ask:
        print("a not found")
        print("e found")
        print("o not found")
      
    elif s4 in ask:
        print("a not found")
        print("e not found")
        print("o found")
    else:
        print("a not found")
        print("e not found")
        print("o not found")


    break  


        