'''
Recursion is the process of defining something in terms of itself.
A physical world example would be to place two parallel mirrors facing each other.
Any object in between them would be reflected recursively.


In Python, we know that a function can call other functions. 
It is even possible for the function to call itself. 
These types of construct are termed as recursive functions.
'''
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1
# factorial(n) = n * factorial(n-1)
def factorial (n):
    if (n==0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(12))
print(factorial(4))

# fibonacci series
# f(0) = 0
# f(1) = 1
# f(2) = f(0) + f(1)
# f(n) = f(n-1) + f(n-2)

def fibonacci (n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))

