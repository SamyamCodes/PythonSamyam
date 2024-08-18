myCat = {"size" : "fat", "color" : "white", "disposition" : "loud"}

print(myCat["color"])
print(f"My cat has {myCat["color"]} color.")


'''
Dictionaries can still use integer values as keys, 
just like lists use integers for indexes, 
but they do not have to start at 0 and can be any number.
'''
spam = {12345: 'Luggage Combination', 42: 'The Answer'}

'''
While the order of items matters for determining whether two lists are the same, 
it does not matter in what order the key-value pairs are typed in a dictionary.
'''
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']

print(spam == bacon) # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs ==  ham)

# Because dictionaries are not ordered, they can’t be sliced like lists.

spam = {"colour" : "red",
        "age": "18"}
for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)
for i in spam.items():
    print(i)

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

spamd = {'name': 'Pooka', 'age': 5}
if 'color' not in spamd:
    spamd['color'] = 'black'


'''
 spam = {'name': 'Pooka', 'age': 5}
 spam.setdefault('color', 'black')
'black'
 spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
 spam.setdefault('color', 'white')
'black'
 spam
{'color': 'black', 'age': 5, 'name': 'Pooka'}
The first time setdefault() is called, the dictionary in spam changes to {'color': 'black', 'age': 5, 'name': 'Pooka'}.
The method returns the value 'black' because this is now the value set for the key 'color'.
When spam.setdefault('color', 'white') is called next, the value for that key is not changed to 'white', because spam already has a key named 'color'.


'''


info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)  #The popitem() method removes the last key-value pair from the dictionary.





