#!/usr/bin/env python
################################# Pseudo-ku ####################################
# Steven Lam - 2020
# inspired by Computerphile: https://youtu.be/G_UYXzGuqvM
################################################################################

from flask import Flask, redirect, render_template, request
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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    # create a dict with each number in the Sudoku grid
    nums = {}
    for i in range(0, 9):
        for j in range(0, 9):
            key = f"{i}{j}"
            nums[key] = int(request.values.get(f"grid_{i}{j}"))

    global sudoku
    sudoku = np.array([
        [nums["00"], nums["01"], nums["02"], nums["03"], nums["04"], nums["05"], nums["06"], nums["07"], nums["08"]],
        [nums["10"], nums["11"], nums["12"], nums["13"], nums["14"], nums["15"], nums["16"], nums["17"], nums["18"]],
        [nums["20"], nums["21"], nums["22"], nums["23"], nums["24"], nums["25"], nums["26"], nums["27"], nums["28"]],
        [nums["30"], nums["31"], nums["32"], nums["33"], nums["34"], nums["35"], nums["36"], nums["37"], nums["38"]],
        [nums["40"], nums["41"], nums["42"], nums["43"], nums["44"], nums["45"], nums["46"], nums["47"], nums["48"]],
        [nums["50"], nums["51"], nums["52"], nums["53"], nums["54"], nums["55"], nums["56"], nums["57"], nums["58"]],
        [nums["60"], nums["61"], nums["62"], nums["63"], nums["64"], nums["65"], nums["66"], nums["67"], nums["68"]],
        [nums["70"], nums["71"], nums["72"], nums["73"], nums["74"], nums["75"], nums["76"], nums["77"], nums["78"]],
        [nums["80"], nums["81"], nums["82"], nums["83"], nums["84"], nums["85"], nums["86"], nums["87"], nums["88"]]
    ])

    # TODO check that input sudoku grid is valid

    # Solve the puzzle
    solve()

    return render_template("result.html")


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
