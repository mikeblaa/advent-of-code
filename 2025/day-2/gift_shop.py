#!/usr/bin/env python3
"""
gift_shop.py - Advent of Code 2025 Day 2 skeleton.

Run:
    python gift_shop.py --input input.txt
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
    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    return lines


def solve_part1(data: Any) -> Any:
    """Solve part 1. Return result (int, str, etc.)."""
    
    invalid_sum = 0

    ranges = data[0].split(',') 
    
    # iterate through each "A-B" range and then through each integer in that range (inclusive)
    for rng in ranges:
        start_s, end_s = rng.split('-')
        start, end = int(start_s), int(end_s)
        for n in range(start, end + 1):
            s = str(n)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                left, right = s[:mid], s[mid:]
                if left == right:
                    invalid_sum += int(s)

    return invalid_sum


def solve_part2(data: Any) -> Any:
    """Solve part 2. Return result (int, str, etc.)."""
    # TODO: implement
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