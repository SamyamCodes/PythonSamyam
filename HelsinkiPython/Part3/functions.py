'''
Important: on this course the automatic tests that are run on the exercise files 
require an empty main function. No commands should be left in the main function of 
your solution. That is, any code that you yourself use for testing must be contained 
in a specially defined if block:

def greet():
    print("Hi!")

# Write your main function within a block like this:
if __name__ == "__main__":
    greet()
'''

# Write your solution here
# You can test your function by calling it within the following block
# if __name__ == "__main__":
#   seven_brothers()
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")
if __name__ == "__main__":
    seven_brothers()

# Arguments and Parameters
'''
While argument is used with the data passed to the function when the function is 
called, inside the function the arguments are assigned to variables called parameters. 
So, approximately, when the function is called, we call the passed bits of data arguments, 
but when we are defining the function, we call them parameters.
'''
def first_character(text):
   if text:
       print(text[0])
# write your code here

# testing the function:
if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

# Write your code here
# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)
def mean(x,y,z):
    me = (x+y+z)/3
    print(me)

# Write your solution here
def print_many_times(string, number):
    x = 1
    while x <= number:
        print(string)
        x+=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)