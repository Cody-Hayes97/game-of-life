# John Conway's Game of Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

[Youtube Demo](https://youtu.be/1PAIEgilVWE)

[Gif Demo](https://giphy.com/gifs/lpsVubVdTsf3y1kW52/fullscreen)

# Rules

In the Game of Life, each square in the grid is considered a **Cell**. each cell can be either dead or alive. Each of these cells has a set of rules in which they intereact with their eight surrounding cells, or **Neighbors**. the rules each cell abides by are as follows:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
1. Any live cell with two or three live neighbors lives on to the next generation.
1. Any live cell with more than three live neighbors dies, as if by overpopulation.
1. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

# To start the game
If you would like to download and play the game for yourself, please follow the link below to the repository where I have uploaded the executable, alternatively, you could just clone this repo and run the main.py file!

**Once you have the game open, you will have several options:**
1. START - will run the algorithm based on the layout of cells you have initially clicked
1. STOP - will pause the simulation, if you would like to rerun it, simply click START again
1. RESET - will wipe the grid completely 
1. SLOW - will cut the frame rate of the game in half and cause the cells to move more slowly 
1. FAST - will double the frame rate and cause the cells to move more quickly

# Portfolio 
If you would like to see my portfolio, please follow the link below
[Portfolio](https://www.codyhayesdeveloper.com/)

