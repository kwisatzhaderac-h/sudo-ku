#%%
import numpy as np

# sudoku array to be solved
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

# %%

# %%
