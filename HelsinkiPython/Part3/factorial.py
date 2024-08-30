# Write your solution here
while True:
    fact = 1
    x = 1
    num = int(input("Please type in a number:"))

    if(num == 0 or num < 0):
        print("Thanks and bye!")
        break
    while x <= num:
        fact  *= x
        x +=1
     
    print(f"The factorial of the number {num} is {fact}")
    
    
