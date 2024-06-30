# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_of_letters = int(input("Enter the number of letters you want."))
number_of_numbers = int(input("Enter the number of numbers you want"))
number_of_symbols = int (input("Enter the number of symbols you want."))

# password  = ""
# for chr in range(1, number_of_letters+1):
#     password += random.choice(letters)

# for chr in range(1, number_of_numbers+1):
#     password += random.choice(numbers)

# for chr in range (1, number_of_symbols+1):
#     password += random.choice(symbols)

# print(password)

#Hard Level
password_list = []

for char in range(1, number_of_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, number_of_numbers + 1):
  password_list += random.choice(symbols)

for char in range(1, number_of_symbols + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")