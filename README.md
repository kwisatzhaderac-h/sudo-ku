# Pseudo-ku
### A simple sudoku solver written in Python!

Pseudo-ku is a lockdown project I started to teach myself the basics of Python.
It's very simple and straightforward to use. Let me show you:

Say I have the following puzzle I wish to be solved:
<p align="center">
  <img width="292" height="294" src="https://i.imgur.com/cIDW5bG.png">
</p>

I first convert it to a 9x9 array, where `0` represent blank spaces.
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


If you provide Pseudo-ku with a 9x9 array representing an uncompleted Sudoku 
puzzle  




