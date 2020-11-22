# Pseudo-ku
### A simple sudoku solver written in Python!

Pseudo-ku is a lockdown project I started to teach myself the basics of Python.
It is very simple and straightforward to use. 

Say we have the following puzzle to be solved:
<p align="center">
  <img width="292" height="294" src="https://i.imgur.com/cIDW5bG.png">
</p>

We will first make a `sudoku` variable equal to the 9x9 Sudoku array we want 
solved. The formatting is pretty much identical, except we will designate `0` 
for the blank spaces. 
```
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
```
If we run `solve()`, the solution is printed alongside the solve time:
```
[[1 5 2 4 8 9 3 7 6]
 [7 3 9 2 5 6 8 4 1]
 [4 6 8 3 7 1 2 9 5]
 [3 8 7 1 2 4 6 5 9]
 [5 9 1 7 6 3 4 2 8]
 [2 4 6 8 9 5 7 1 3]
 [9 1 4 6 3 7 5 8 2]
 [6 2 5 9 4 8 1 3 7]
 [8 7 3 5 1 2 9 6 4]]
Solved in 0.006982088088989258 seconds
```

We see that this matches the solution below!

<p align="center">
  <img width="294" height="294" src="https://i.imgur.com/JyAuwVt.png">
</p>

[Puzzle and solution from here](https://dingo.sbs.arizona.edu/~sandiway/sudoku/examples.html) 



