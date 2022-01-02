#!/usr/bin/env python
################################# Pseudo-ku ####################################
# Steven Lam - 2020
# inspired by Computerphile: https://youtu.be/G_UYXzGuqvM
################################################################################

import numpy as np
import time

# Begin tracking program run time
start_time = time.time()

# Initialise puzzle
sudoku = np.array([
    [1,0,0,4,8,9,0,0,6],
    [7,3,0,0,0,0,0,4,0],
    [0,0,0,0,0,1,2,9,5],
    [0,0,7,1,2,0,6,0,0],
    [5,0,0,7,0,3,0,0,8],
    [0,0,6,0,9,5,7,0,0],
    [9,1,4,6,0,0,0,0,0],
    [0,2,0,0,0,0,0,3,7],
    [8,0,0,5,1,2,0,0,4]
        ])

# Checker function
def can_fit(x, y, val):
    global sudoku
    row = x - (x % 3)
    col = y - (y % 3)
    for i in sudoku[x, :]:
        if i == val:
            return False
    for j in sudoku[:, y]:
        if j == val:
            return False
    for k in range(row, row + 3):
        for z in range(col, col + 3):
            if sudoku[k][z] == val:
                return False
    return True

# Potential solutions
def all_sols(x, y):
    sols = [num for num in range(1, 10) if can_fit(x, y, num) == True]
    return sols


# Recursive solver
def solve():
    global sudoku
    for x in range(0, 9):
        for y in range(0, 9):
            if sudoku[x][y] == 0:
                for sol in all_sols(x, y):
                    sudoku[x][y] = sol
                    solve()
                sudoku[x][y] = 0
                return
    print(sudoku)

# If app is run in the command line
if __name__ == "__main__":
    solve()
    print("Solved in %s seconds" % (time.time() - start_time))
