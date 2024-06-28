# Title : String Methods.

# Strings are immutable.
a = "Samyam"
print(len(a))

print(a.upper())   #This makes a new string.
print(a.lower())

# rstrip()
b = "Samyam!!!!!!!!!!"
print(b)
print(b.rstrip("!")) # This means, remove the trailing character from the string. That means removes only the end characters.
bc = "!!!!Samyam!!!!!!!!!!"
print(bc.rstrip("!")) 

# Replace
print(a.replace("Samyam", "Shrestha"))

# Split >> Must have blank space.
ac = "Sam yam Shre stha"
print(ac.split(" ") ) #>> This converts to list. 

# Capitalize
# This turns only the first character of the string to upper case. 
blogHeading = "introduction to js"
print(blogHeading.capitalize())
blogHeadings = "introduction tO jS"
print(blogHeadings.capitalize()) #Capitalize le yeslai pani milai dinxa.

# Center()
str1 = "Welcome to the Console!!!"
print(str1.center(50))

# Count(" ")
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
print(str2.count("a"))

# endswith("")
str3 = "Welcome to the Console !!!"
print(str3.endswith("!!!"))

# We can even also check for a value in-between the string by providing start and end index positions.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

# find()
'''
The find() method searches for the first occurrence of the given value
and returns the index where it is present. 
If given value is absent from the string then return -1.
'''
asd = "He's name is Samyam. He is an honest man"
print(asd.find("is"))

# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))

# index()

str1 = "He's name is Sam. Dan is an honest man."
print(str1.index("Sam"))

# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
str1 = "He's name is Sam. Dan is an honest man."
# print(str1.index("Daniel")) #>> This gives an output error of substring not found.

# isalphanum()
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

str22 = "WelcomeToTheConsole22"
print(str22.isalnum())

# isprintable()
printa = "Welcome to the new world of gaming"
print(printa.isprintable())
printa = "Welcome to the new world of gaming\n"
print(printa.isprintable()) #>> \n is not printable.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())





