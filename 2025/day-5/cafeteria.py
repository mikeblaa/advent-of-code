#!/usr/bin/env python3
"""
cafeteria.py - Advent of Code 2025 Day 5

Run:
    python cafeteria.py --input input.txt
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


def solve_part1(data: Any) -> Any:
    """Solve part 1. Return result (int, str, etc.)."""
    
    # Find the first empty line, lines before are ranges of fresh ingredients, 
    # lines after are ingredients to check
    x = data.index("")

    fresh_ranges = data[:x]
    check_ingredients = data[x+1:]
    fresh_set = set()

    for ingredient in check_ingredients:
        # Sanity check: all ingredients should be integers
        int(ingredient)

        # Iterate through the fresh ranges, check if ingredient is in any range
        for r in fresh_ranges:
            start, end = range_to_start_end(r)
            if int(ingredient) >= start and int(ingredient) <= end:
                fresh_set.add(int(ingredient))
                break

    count_fresh = len(fresh_set)

    return count_fresh


def solve_part2(data: Any) -> Any:
    """Solve part 2. Return result (int, str, etc.)."""
    
    # Find the first empty line, lines before are ranges of fresh ingredients, 
    # lines after are ingredients to check
    x = data.index("")

    fresh_ranges = data[:x]
    check_ingredients = data[x+1:]
    fresh_set = set()

    return len(fresh_set)

"""Part 1 methods"""
def add_range_to_set(s: set[int], start: int, end: int) -> None:
    for i in range(start, end + 1):
        s.add(i)

def range_to_start_end(r: str) -> Tuple[int, int]:
    start_str, end_str = r.split("-")
    return int(start_str), int(end_str)

def range_size(r: str) -> int:
    start, end = range_to_start_end(r)
    return end - start + 1

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