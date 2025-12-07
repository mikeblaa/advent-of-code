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


def find_column_widths(data: List[List[str]]) -> List[int]:
    column_count = len(data[0])
    max_col_widths = [0 for _ in range(len(line_to_array(data[0])))]

    for row in data:
        row_data = line_to_array(row)
        for col in range(len(row_data)):
            value = row_data[col]
            value_len = len(value)

            if value_len > max_col_widths[col]:
                max_col_widths[col] = value_len
    
    return max_col_widths


def line_to_array_with_fixed_widths(line: str, column_widths: List) -> List[str]:
    values = []
    current_index = 0

    col_idx = 0
    col_start = 0
    col_end = col_start + column_widths[col_idx]

    while col_start < len(line):
        value = line[col_start:col_end]
        values.append(value)
        
        col_start += column_widths[col_idx] + 1# assuming a space between columns
        col_idx += 1
        if col_idx == len(column_widths):
            break

        col_end += column_widths[col_idx] + 1
        

    return values


def pad_with_zeros(value: str, width: int) -> str:
    if value.startswith(" "):
        return value.lstrip().rjust(width, "0")
    elif value.endswith(" "):
        return value.rstrip().ljust(width, "0")
    else:
        return value


def do_cephalapod_math(operator: str, values: List[str]) -> int:
    number_width = len(values[0])
    grand_total = 0

    padded_values = []
    for v in values:
        padded_values.append(pad_with_zeros(v, len(v)))

    if operator == "+":
        for num_col in range(number_width):
            curr_value_str = ""
            for v in values:
                curr_value_str += v[num_col]
            
            if curr_value_str.isspace():
                break

            curr_value = int(curr_value_str)
            grand_total += curr_value
    elif operator == "*":
        grand_total = 1
        for num_col in range(number_width):
            curr_value_str = ""
            for v in values:
                curr_value_str += v[num_col]
            
            if curr_value_str.isspace():
                break

            curr_value = int(curr_value_str)
            grand_total *= curr_value
    else:
        print(f"Unknown operator: {operator}")
        return 0
    
    return grand_total


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

    column_widths = find_column_widths(data)

    for row in range(len(data)):
        data[row] = line_to_array_with_fixed_widths(data[row], column_widths)

    operators = data.pop(-1)

    for col in range(len(operators)):
        operators[col] = operators[col].strip()

    grand_total = 0

    for col in range(len(column_widths)):
        values = []
        for row in range(len(data)):
            values.append(data[row][col])

        col_value = do_cephalapod_math(operators[col], values)
        grand_total += col_value

    return grand_total

def main(argv: List[str] | None = None) -> int:
    args = parse_args(argv)
    raw = read_input(args.input)
    data = parse_input(raw)

    part1 = solve_part1(data.copy())
    part2 = solve_part2(data.copy())

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
