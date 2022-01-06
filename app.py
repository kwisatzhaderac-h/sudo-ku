#!/usr/bin/env python
################################# Pseudo-ku ####################################
# Steven Lam - 2020
# inspired by Computerphile: https://youtu.be/G_UYXzGuqvM
################################################################################

from types import SimpleNamespace
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

    # Solve the puzzle
    solve(sudoku)

    solns = {}
    for i in range(0, 9):
        for j in range(0, 9):
            key = f"sol_{i}{j}"
            solns[key] = sudoku[i][j]

    return render_template(
                            "result.html",
                            sol_00 = solns["sol_00"],
                            sol_01 = solns["sol_01"],
                            sol_02 = solns["sol_02"],
                            sol_03 = solns["sol_03"],
                            sol_04 = solns["sol_04"],
                            sol_05 = solns["sol_05"],
                            sol_06 = solns["sol_06"],
                            sol_07 = solns["sol_07"],
                            sol_08 = solns["sol_08"],
                            sol_10 = solns["sol_10"],
                            sol_11 = solns["sol_11"],
                            sol_12 = solns["sol_12"],
                            sol_13 = solns["sol_13"],
                            sol_14 = solns["sol_14"],
                            sol_15 = solns["sol_15"],
                            sol_16 = solns["sol_16"],
                            sol_17 = solns["sol_17"],
                            sol_18 = solns["sol_18"],
                            sol_20 = solns["sol_20"],
                            sol_21 = solns["sol_21"],
                            sol_22 = solns["sol_22"],
                            sol_23 = solns["sol_23"],
                            sol_24 = solns["sol_24"],
                            sol_25 = solns["sol_25"],
                            sol_26 = solns["sol_26"],
                            sol_27 = solns["sol_27"],
                            sol_28 = solns["sol_28"],
                            sol_30 = solns["sol_30"],
                            sol_31 = solns["sol_31"],
                            sol_32 = solns["sol_32"],
                            sol_33 = solns["sol_33"],
                            sol_34 = solns["sol_34"],
                            sol_35 = solns["sol_35"],
                            sol_36 = solns["sol_36"],
                            sol_37 = solns["sol_37"],
                            sol_38 = solns["sol_38"],
                            sol_40 = solns["sol_40"],
                            sol_41 = solns["sol_41"],
                            sol_42 = solns["sol_42"],
                            sol_43 = solns["sol_43"],
                            sol_44 = solns["sol_44"],
                            sol_45 = solns["sol_45"],
                            sol_46 = solns["sol_46"],
                            sol_47 = solns["sol_47"],
                            sol_48 = solns["sol_48"],
                            sol_50 = solns["sol_50"],
                            sol_51 = solns["sol_51"],
                            sol_52 = solns["sol_52"],
                            sol_53 = solns["sol_53"],
                            sol_54 = solns["sol_54"],
                            sol_55 = solns["sol_55"],
                            sol_56 = solns["sol_56"],
                            sol_57 = solns["sol_57"],
                            sol_58 = solns["sol_58"],
                            sol_60 = solns["sol_60"],
                            sol_61 = solns["sol_61"],
                            sol_62 = solns["sol_62"],
                            sol_63 = solns["sol_63"],
                            sol_64 = solns["sol_64"],
                            sol_65 = solns["sol_65"],
                            sol_66 = solns["sol_66"],
                            sol_67 = solns["sol_67"],
                            sol_68 = solns["sol_68"],
                            sol_70 = solns["sol_70"],
                            sol_71 = solns["sol_71"],
                            sol_72 = solns["sol_72"],
                            sol_73 = solns["sol_73"],
                            sol_74 = solns["sol_74"],
                            sol_75 = solns["sol_75"],
                            sol_76 = solns["sol_76"],
                            sol_77 = solns["sol_77"],
                            sol_78 = solns["sol_78"],
                            sol_80 = solns["sol_80"],
                            sol_81 = solns["sol_81"],
                            sol_82 = solns["sol_82"],
                            sol_83 = solns["sol_83"],
                            sol_84 = solns["sol_84"],
                            sol_85 = solns["sol_85"],
                            sol_86 = solns["sol_86"],
                            sol_87 = solns["sol_87"],
                            sol_88 = solns["sol_88"]
                        )


def main():
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

    # Solve
    print(solve(sudoku))
    print(sudoku)
    print(f"Solved in {(time.time() - start_time):.5f} seconds")


# Checker function
def can_fit(x, y, val, puzzle):
    row = x - (x % 3)
    col = y - (y % 3)
    for i in puzzle[x, :]:
        if i == val:
            return False
    for j in puzzle[:, y]:
        if j == val:
            return False
    for k in range(row, row + 3):
        for z in range(col, col + 3):
            if puzzle[k][z] == val:
                return False
    return True


# Potential solutions
def all_sols(x, y, puzzle):
    sols = [num for num in range(1, 10) if can_fit(x=x, y=y, val=num, puzzle=puzzle) == True]
    return sols


def solve(sudoku):
    for x in range(0, 9):
        for y in range(0, 9):
            if sudoku[x][y] == 0:
                for sol in all_sols(x=x, y=y, puzzle=sudoku):
                    sudoku[x][y] = sol
                    if solve(sudoku):
                        return True
                sudoku[x][y] = 0
                return False
    return True


if __name__ == "__main__":
    main()
