'''
Please write a function named palindromes, which takes a string argument and returns True if the string is a palindrome. 
Palindromes are words which are spelled exactly the same backwards and forwards.

Please also write a main program which asks the user to type in words until they type in a palindrome:

Sample output
Please type in a palindrome: python
that wasn't a palindrome
Please type in a palindrome: java
that wasn't a palindrome
Please type in a palindrome: oddoreven
that wasn't a palindrome
Please type in a palindrome: neveroddoreven
neveroddoreven is a palindrome!
'''

def palindrome(word):
    return word.lower() == word[::-1].lower()

def main():
    while True:
        ask = input("Please type in a palindrome:")
        if (palindrome(ask)):
            print(f"{ask} is a palindrome.")
            break
        else:
            print("that wasn't a palindrome.")

main()