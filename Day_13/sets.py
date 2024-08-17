'''
Sets are unordered collection of data items.
 They store multiple items in a single variable. 
Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. 
Sets do not contain duplicate items.

items of set occur in random order and hence they cannot be accessed using index numbers. 
Also sets do not allow duplicate values.
'''


s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

harry = set()  #Creating an empty set.
print(type(harry))

# You can access items of set using a for loop.
for value in info:
  print(value)