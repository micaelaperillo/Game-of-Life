# Implementation of Conway's Game of Life

## About

The Game of Life is a cellular automaton devised by John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. 

The universe of the Game of Life is a two-dimensional grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Usage

This game requires PyGame, Numpy and Tkinter to run. You can install them using the package manager

```bash
pip install pygame
pip intall numpy
pip install tkinter
```

To run, just execute the file using

```bash
python3 main.py
```

### Commands
- Click on every cell to mark it alive, click it again to mark it dead
- Press space to begin the game, since the game is paused at first. You can press space anytime to pause the game
- Press n to create a new game
- Press h to open help
- Press x to close the window

## Credits
This channel inspired me to do this project, specially these two videos
- https://www.youtube.com/watch?v=qPtKv9fSHZY
- https://www.youtube.com/watch?v=omMcrvVGTMs
- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

## License
MIT Licence

Copyright (c) 2023 Micaela Perillo