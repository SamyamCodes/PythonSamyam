# Title: String Slicing
# For slicing we use square brackets [].
names = "Samyam,Shrestha"
print(names[0:5])
print(len(names))


fruit = "Mango"
len1 = len(fruit)
print(len1)
print(fruit[0: 4])  # Including 0 but not 4.
print(fruit[0: 4])  # Including 1 but not 4.
print(fruit[1: 4])
print(fruit[: 4])
print(fruit[:])

# Negative SLicing

print(fruit[0: -3])  #THis is equivalent to len(fruit) - 3 = 5-3 >> 0:2
print(fruit[-3: -1])








