# Please write a program which asks for the user's name and address. The program should also print out the given information, as follows:

# Sample output
# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

# Write your solution here
name1 = input("Given name:")
name2 = input("Family name:")
address1 = input("Street address:")
address2 = input("City and postal code:")
print(name1 + " "+name2)
print(address1)
print(address2)


# 2)
# Here is a program which should ask for three utterances and print them out, like so:

# Sample output
# The 1st part: hickory
# The 2nd part: dickory
# The 3rd part: dock
# hickory-dickory-dock!
# However, there is something wrong with the code below. Please fix it.
# Fix the code
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1+"-" + part2+"-" + part3+"!")