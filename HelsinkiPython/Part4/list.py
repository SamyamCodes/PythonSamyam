'''
Please write a program which initialises a list with the values [1, 2, 3, 4, 5]. 
Then the program should ask the user for an index and a new value, replace the 
value at the given index, and print the list again. 
This should be looped over until the user gives -1 for the index. 
You can assume all given index values will fall within your list.

An example execution of the program:

Sample output
Index: 0
New value: 10
[10, 2, 3, 4, 5]
Index: 2
New value: 250
[10, 2, 250, 4, 5]
Index: 4
New value: -45
[10, 2, 250, 4, -45]
Index: -1
'''

# Initialize the list with values
my_list = [1, 2, 3, 4, 5]

while True:

    idx = int(input("Index: "))
    
    # Exit the loop if the user enters -1
    if idx == -1:
        break

    new_value = int(input("New value: "))

    my_list[idx] = new_value
    print(my_list)
