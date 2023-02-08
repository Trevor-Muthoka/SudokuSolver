# This solution uses backtracking to solve the sudoku puzzle

def is_valid(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num: #check each cell in a row to see if the number is already there
            return False
    # Check column
    for i in range(9):
        if grid[i][col] == num: #check each cell in a column to see if the number is already there
            return False
    # Check box
    box_row = row - (row % 3) #top left corner of box
    box_col = col - (col % 3) #top left corner of box
    for i in range(3):
        for j in range(3):
            if grid[box_row + i][box_col + j] == num: #check each cell in a 3 by 3 box to see if the number is already there
                return False
    return True

def solve(grid, row, col):
    if col ==9:
        if row == 8:
           return True #if we are at the end of the grid, we are done
        row += 1
        col = 0

    if grid[row][col] > 0: #if the cell is not empty, move to the next cell
        return solve(grid, row, col + 1)
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num #if the number is valid, put it in the cell
            if solve(grid, row, col + 1):
                return True #if the number is valid, move to the next cell
        grid[row][col] = 0 #if the number is not valid, reset the cell to 0
    return False

# replace the grid with the grid you want to solve and have the numbers blank as 0


grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]

if solve(grid, 0, 0):
    for i in range(9):
         for j in range(9):
             print(grid[i][j], end=" ")
         print()
else:
    print("No solution found for the grid")