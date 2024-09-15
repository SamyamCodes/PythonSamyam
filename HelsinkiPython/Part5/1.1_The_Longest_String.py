'''

Please write a function named longest(strings: list), which takes a list of strings as its argument. 
The function finds and returns the longest string in the list. 
You may assume there is always a single longest string in the list.

An example of expected behaviour:


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
Sample output
howdydoody


'''

# Write your solution here
def longest(strings: list):
    long_string = ' '
    for item in strings:
        if len(item) > len(long_string):
            long_string = item
    return long_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))


# Just out of context code:
persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]

for person in persons:
  name = person[0]
  age = person[1]
  height = person[2]
  print(f"{name}: age {age} years, height {height} meters")

my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

print(my_matrix[0][1])
my_matrix[1][0] = 10
print(my_matrix)

for row in my_matrix:
    print(row)