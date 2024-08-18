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









