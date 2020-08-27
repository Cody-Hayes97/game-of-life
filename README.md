# John Conway's Game of Life

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

[Youtube Demo](https://youtu.be/1PAIEgilVWE)

[Gif Demo](https://giphy.com/gifs/lpsVubVdTsf3y1kW52/fullscreen)

# Rules

In the Game of Life, each square in the grid is considered a **Cell**. each cell can be either dead or alive. Each of these cells has a set of rules in which they intereact with their eight surrounding cells, or **Neighbors**. the rules each cell abides by are as follows:

_1. Any live cell with fewer than two live neighbors dies, as if by underpopulation._
_1. Any live cell with two or three live neighbors lives on to the next generation._
_1. Any live cell with more than three live neighbors dies, as if by overpopulation._
_1. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction._

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

# To start the game
