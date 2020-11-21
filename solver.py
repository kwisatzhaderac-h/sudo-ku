#%%
import numpy as np

############################# array to be solved ##############################
sudoku = np.array([  
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0] 
        ])
################################# checker #####################################
def can_fit(x, y, val):
    global sudoku
    # checking row
    for i in sudoku[x, :]:
        if i == val:
            return False

    # checking column
    for i in sudoku[:, y]:
        if i == val:
            return False
    # checking square
    x = x - (x % 3)
    y = y - (y % 3)
    
    for i in range(x, x + 3):
        for z in range(y, y + 3):
            if sudoku[i][z] == val:
                return False

    return True
############################## find solutions #################################
# check each entry whether number from range(1,10) can fit
# If can fit, store number as possible entry

# let's first find all the possible solutions for a space
def all_sols(x, y):
    sols = [num for num in range(1, 10) if can_fit(x, y, num) == True]
    return sols                
################################## solver #####################################
# Now we have a checker, and a function to find all possible solutions for any
# given position. Now we iterate across each position of the puzzle, trying
# all possible solutions. 
# What happens with solver meets a blank entry?
#   finds all possible solutions. Makes blank entry the first possible solution
#   continues to solve the rest of the array with first possible solution.
#   


def solve():
    # remember that all functions check the original sudoku list
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

solve()
# %%