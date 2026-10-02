# maze-loom

Generate a perfect maze as terminal-friendly ASCII art. The iterative randomized backtracker carves one connected route through every cell, with a single path between any two cells. A seed makes the same maze reproducible.

## Use

Requires Python 3.8+; no packages to install.

```sh
python maze_loom.py
python maze_loom.py --width 32 --height 16 --seed 42
```

`S` marks the entrance and `E` the exit. Width and height count maze cells (1–80 by 1–40); the rendered grid is twice that size plus the walls. If no seed is supplied, a random 32-bit seed is generated and printed so the maze can be recreated later.

## License

MIT
