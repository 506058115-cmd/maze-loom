#!/usr/bin/env python3
"""Generate a bounded, reproducible perfect maze as ASCII art."""

import argparse
import random
import secrets


MAX_WIDTH = 80
MAX_HEIGHT = 40
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def generate(width, height, seed):
    rng = random.Random(seed)
    maze = [["#"] * (2 * width + 1) for _ in range(2 * height + 1)]
    visited = {(0, 0)}
    stack = [(0, 0)]
    maze[1][1] = " "

    while stack:
        x, y = stack[-1]
        choices = [
            (x + dx, y + dy, dx, dy)
            for dx, dy in DIRECTIONS
            if 0 <= x + dx < width and 0 <= y + dy < height and (x + dx, y + dy) not in visited
        ]
        if not choices:
            stack.pop()
            continue

        nx, ny, dx, dy = rng.choice(choices)
        maze[2 * y + 1 + dy][2 * x + 1 + dx] = " "
        maze[2 * ny + 1][2 * nx + 1] = " "
        visited.add((nx, ny))
        stack.append((nx, ny))

    maze[0][1] = "S"
    maze[-1][-2] = "E"
    return "\n".join("".join(row) for row in maze)


def main():
    parser = argparse.ArgumentParser(description="Generate a seeded ASCII perfect maze.")
    parser.add_argument("--width", type=int, default=20, help="maze cells across (1–80)")
    parser.add_argument("--height", type=int, default=10, help="maze cells tall (1–40)")
    parser.add_argument("--seed", type=int, help="reproducible seed from 0 to 4294967295")
    args = parser.parse_args()
    if not 1 <= args.width <= MAX_WIDTH:
        parser.error(f"--width must be between 1 and {MAX_WIDTH}")
    if not 1 <= args.height <= MAX_HEIGHT:
        parser.error(f"--height must be between 1 and {MAX_HEIGHT}")
    if args.seed is not None and not 0 <= args.seed <= 0xFFFFFFFF:
        parser.error("--seed must be between 0 and 4294967295")

    seed = args.seed if args.seed is not None else secrets.randbits(32)
    print(f"Maze: {args.width} × {args.height} cells | seed: {seed}")
    print(generate(args.width, args.height, seed))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
