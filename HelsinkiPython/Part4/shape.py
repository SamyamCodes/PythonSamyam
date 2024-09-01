'''
Please write a function named shape, which takes four arguments. The first two parameters specify a triangle, 
as above, and the character used to draw it. The first parameter also specifies the width of a rectangle, 
while the third parameter specifies its height. The fourth parameter specifies the filler character of the 
rectangle. The function prints first the triangle, and then the rectangle below it.

The function should call the function line from the exercise above for the actual printing out. 
Copy your solution to that exercise above the code for this exercise. Please don't change anything in the 
line function.

Some examples:

shape(5, "X", 3, "*")
print()
shape(2, "o", 4, "+")
print()
shape(3, ".", 0, ",")
Sample output
X
XX
XXX
XXXX
XXXXX
*****
*****
*****

o
oo
++
++
++
++

.
..
...
'''

def line(x, st):
    x_int = int(x)
    if st == "":
        print("*"* x_int)
    else:
        print(st[0]* x_int)

def triangle(size, shape):
    x = 1
    num = 1
    while x < (size +1):
        line(num, shape)
        num += 1
        x +=1
    
def rectangle(width, size, character):
    x = 1
    while x < (size + 1):
        line(width, character)
        x +=1

def shape( tint, tchar, hrect, rchar):
    tint = int(tint)
    hrect = int(hrect)

    triangle(tint, tchar)
    rectangle(tint, hrect, rchar)
       
    
if __name__ == "__main__":
    shape(5, "x", 2, "o")