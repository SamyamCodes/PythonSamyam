# Break Statement

for i in range(12):
    if (i==10):
        break  # Break means leave the loop.
    print("5 X ", i+1, "=" ,5*(i+1))
print("Loop lai xodera nikli.")

# Continue Statement
# >> Leave the iteration
    
for i in range(12):
    if (i==10):
        print("Skip the iteration.")
        continue
    print("5 X ", i, "=" ,5*(i))

# Emulate do while loop in python

num = 0
while (True):
    print(num)
    num = num +1   #This is do
    if(num % 100 == 0):  # This is condition of while. 
        break



