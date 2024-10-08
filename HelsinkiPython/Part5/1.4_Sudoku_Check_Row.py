'''

Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional 
array representing a sudoku grid, and an integer referring to a single row, as its arguments. 
Rows are indexed from 0.

The function should return True or False, depending on whether the row is filled in correctly, 
that is, whether it contains each of the numbers 1 to 9 at most once.

sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))

Sample output
True
False

'''
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    seen = set()
    
    for number in row:
        if number != 0:  # Ignore 0s (empty spaces)
            if number in seen:  # Check if the number is already in the set
                return False
            seen.add(number)  # Add the number to the set
    
    return True


# Example sudoku grid
sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

# Test cases
print(row_correct(sudoku, 0))  # True
print(row_correct(sudoku, 1))  # False
