'''
If you know the beginning and end indexes of the slice 
you wish to extract, you can do so with the notation [a:b]. T
his means the slice begins at the index a and ends at 
the last character before index b - that is,
 including the first, but excluding the last
'''
input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])