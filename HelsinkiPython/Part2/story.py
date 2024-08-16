'''
Part 1
Please write a program which keeps asking the user for words. If the user types in end, the program should print out the story the words formed, and finish.

Sample output
Please type in a word: Once
Please type in a word: upon
Please type in a word: a
Please type in a word: time
Please type in a word: there
Please type in a word: was
Please type in a word: a
Please type in a word: girl
Please type in a word: end
Once upon a time there was a girl

Part 2
Change the program so that the loop ends also if the user types in the same word twice in a row.

Sample output
Please type in a word: It
Please type in a word: was
Please type in a word: a
Please type in a word: dark
Please type in a word: and
Please type in a word: stormy
Please type in a word: night
Please type in a word: night
It was a dark and stormy night

'''

strings = " "
previous_word = " "
while True:
    ss = input("Please type in a word:")
    if(ss == "end" or ss == previous_word):
        break
    strings += ss + " "
    
    previous_word = ss

print(strings)

# Working with numbers

print("Please type in integer numbers. Type in 0 to finish.")

# Initialize variables
count = 0
total_sum = 0
positive_count = 0
negative_count = 0

while True:
    number = int(input("Number: "))
    
    if number == 0:
        break
    
    # Update the count of numbers
    count += 1
    
    # Update the total sum of numbers
    total_sum += number
    
    # Count positive and negative numbers
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

# Calculate the mean
mean = total_sum / count if count > 0 else 0

# Print the results with correct formatting
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {total_sum}")
print(f"The mean of the numbers is {mean:.1f}")
print(f"Positive numbers {positive_count}")
print(f"Negative numbers {negative_count}")
