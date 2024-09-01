'''
Please write three functions: first_word, second_word and last_word. 
Each function takes a string argument.

As their names imply, the functions return either the first, the second or the last
word in the sentence they receive as their string argument.

In each case you may assume the argument string contains at least two separate words, and all words are separated by exactly one space 
character. There will be no spaces in the beginning or at the end of the argument strings.

sentence = "it was a dark and stormy python"

print(first_word(sentence)) # it
print(second_word(sentence)) # was
print(last_word(sentence)) # python
Sample output
it
was
python

sentence = "it was"

print(second_word(sentence)) # was
print(last_word(sentence)) # was
'''

def first_word(sentence):
    # Split the sentence into words and return the first word
    return sentence.split()[0]

def second_word(sentence):
    # Split the sentence into words and return the second word
    return sentence.split()[1]

def last_word(sentence):
    # Split the sentence into words and return the last word
    return sentence.split()[-1]

# Test the functions with example sentences
if __name__ == "__main__":
    sentence1 = "it was a dark and stormy python"
    print(first_word(sentence1))  # Output: it
    print(second_word(sentence1))  # Output: was
    print(last_word(sentence1))   # Output: python

    sentence2 = "it was"
    print(second_word(sentence2))  # Output: was
    print(last_word(sentence2))    # Output: was
