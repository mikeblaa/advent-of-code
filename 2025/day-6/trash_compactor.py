#!/usr/bin/env python3
"""
name.py - Advent of Code 2025 Day 6

Run:
    python name.py --input input.txt
"""

from __future__ import annotations
import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Any


def parse_args(argv: List[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Advent of Code 2025 - Day 2: Gift Shop")
    parser.add_argument("-i", "--input", type=Path, default=None, help="Path to input file (defaults to stdin)")
    return parser.parse_args(argv)


def read_input(path: Path | None) -> str:
    if path is None:
        return sys.stdin.read()
    return path.read_text()


def parse_input(raw: str) -> Any:
    """
    Parse raw input text into a structured form.
    Replace the body of this function with logic specific to the puzzle input.
    """
    # lines = [line.strip() for line in raw.splitlines() if line.strip()]
    lines = [line for line in raw.splitlines()]
    return lines

def line_to_array(line: str) -> List[str]:
    """Convert a line of input into an array of strings."""
    return [str(x.strip()) for x in line.split()]

def solve_part1(data: Any) -> Any:
    """Solve part 1. Return result (int, str, etc.)."""
    
    for row in range(len(data)):
        data[row] = line_to_array(data[row])
    
    row_count = len(data)
    col_count = len(data[0])

    grand_total = 0

    for col in range(col_count):

        values = []
        operator = data[row_count - 1][col]
        
        for row in range(row_count - 1):
            value = data[row][col]
            values.append(value)
        
        if operator == "+":
            col_total = sum(int(v) for v in values)
            grand_total += col_total
        elif operator == "*":
            col_total = 1
            for v in values:
                col_total *= int(v)
            grand_total += col_total
        else:
            print(f"Unknown operator: {operator}")
    
    return grand_total


def solve_part2(data: Any) -> Any:
    """Solve part 2. Return result (int, str, etc.)."""
    return None

def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)
    raw = read_input(args.input)
    data = parse_input(raw)

    part1 = solve_part1(data)
    part2 = solve_part2(data)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
