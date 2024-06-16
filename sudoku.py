def find_next_empty(puzzle):
    # finds the next row,col, on the puzzle that's not filled yet 
    # return row,col tuple 
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # figures out if guess at that row and col is valid or not 
    # return true if valid
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # which 3x3 box 
    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True
  
def solve_sudoku(puzzle):
    # solve sudoku using backtracking 
    # our puzzle is a list of list, where each list represents a row in sudoku 
    # return whether a solution exists 
    # mutates the puzzle to be the solution (if solution exists)
    
    # choose somewhere on the puzzle to make a guess 
    row, col = find_next_empty(puzzle)

    if row is None:
        return True
    
    # if there is a place to place our guess, then make a guess from 1 to 9 
    for guess in range(1, 10):
        # check if it is valid 
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if solve_sudoku(puzzle):
                return True

        # backtracking 
        puzzle[row][col] = -1  # reset the value

    # if none of them work, return false
    return False
def print_sudoku(puzzle):
    for row in puzzle:
        print(" ".join(str(num) if num != -1 else "." for num in row))

# Define a Sudoku puzzle (use -1 to represent empty spaces)
puzzle = [
    [-1, -1, -1, 2, 6, -1, 7, -1, 1],
    [6, 8, -1, -1, 7, -1, -1, 9, -1],
    [1, 9, -1, -1, -1, 4, 5, -1, -1],
    [8, 2, -1, 1, -1, -1, -1, 4, -1],
    [-1, -1, 4, 6, -1, 2, 9, -1, -1],
    [-1, 5, -1, -1, -1, 3, -1, 2, 8],
    [-1, -1, 9, 3, -1, -1, -1, 7, 4],
    [-1, 4, -1, -1, 5, -1, -1, 3, 6],
    [7, -1, 3, -1, 1, 8, -1, -1, -1]
]

print("Original puzzle:")
print_sudoku(puzzle)

if solve_sudoku(puzzle):
    print("\nSolved puzzle:")
    print_sudoku(puzzle)
else:
    print("\nNo solution exists for the puzzle")