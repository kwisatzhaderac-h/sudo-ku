#!/usr/bin/env python
################################# Pseudo-ku ####################################
# Steven Lam - 2020
# inspired by Computerphile: https://youtu.be/G_UYXzGuqvM
################################################################################

from flask import Flask, flash, redirect, render_template, request
import numpy as np
import time


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

def main():
    # Begin tracking program run time
    start_time = time.time()

    # Solve
    solve()

    print(f"Solved in {(time.time() - start_time):.5f} seconds")


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


if __name__ == "__main__":
    # Initialise puzzle
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
    main()
