# This is Day_06

# Title: If else Statement
a = int(input("Enter Your Age: "))
print("Your age is: ", a)

# Conditional Operators
# >, <,  >=, <= , ==, != 

if (a > 18):
    print("You can drive.")
else:
    print("You are not eligible to drive.")

last_text = "Thank You For Using Our Service."
print(last_text.center(50))

# elif 

price = int(input("Enter the price of the mobile phone in Rs. = "))
budget = int(input("Enter you current budget"))
print("The price of the mobile phone is: ", price)
print("Your total budget is: ", budget)

if(budget - price > 5000):
    print("You can buy the phone and pay the dinner bills")
elif(budget - price > 3000):
    print("You can buy the phone but cannot pay the dinner price.")
else:
    print("It is not recommended to buy the phone.")

last_text = "Thank You For Using Our Service."
print(last_text.center(50))

