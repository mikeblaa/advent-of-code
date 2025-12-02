#!/usr/bin/env python3
"""Read a file given on the command line and write it to stdout.

Usage:
  python read_file.py PATH
  python read_file.py -            # read from stdin

Options:
  -e, --encoding ENC   : decode using ENC when reading text (default: binary copy)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Tuple

class SecretEntrance():

    @staticmethod
    def generate_dial(size: int) -> CircularLinkedList:
        cll = CircularLinkedList()
        for i in range(size):
            cll.append(i)
        return cll
    
    @staticmethod
    def parse_line(line: str) -> Tuple[str, int]:
        return "R", 3

class Dial:
    def __init__(self, size: int):
        self.size = size
        self.cll = CircularLinkedList()
        for i in range(size):
            self.cll.append(i)
        self.current_node = self.cll.head
    
    def current_number(self) -> int:
        return self.current_node.data
    
    def seek(self, position: int) -> int:
        self.current_node = self.cll.seek(position)
        return self.current_node.data
    
    def rotate_left(self, steps: int):
        self.current_node = self.cll.left_seek(self.current_node, steps)

    def rotate_right(self, steps: int):
        self.current_node = self.cll.right_seek(self.current_node, steps)

class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        # Initialize an empty circular linked list with head pointer pointing to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the circular linked list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                # Traverse the list until the last node
                current = current.next
            # Make the last node point to the new node
            current.next = new_node
            # Make the new node point back to the head
            new_node.next = self.head
            new_node.prev = current
            # Update head's prev to new node
            self.head.prev = new_node

    def seek(self, number: int) -> Node:
        # Find the first node whose data equals number. Return None if not found.
        if not self.head:
            return None
        current = self.head
        while True:
            if current.data == number:
                return current
            current = current.next
            if current == self.head:
                return None
        return current
    
    def left_seek(self, node: Node, steps: int) -> Node:
        # Seek a number of steps to the left (previous) from the given node
        if not node:
            return None
        current = node
        for _ in range(steps):
            current = current.prev
        return current
    
    def right_seek(self, node: Node, steps: int) -> Node:
        # Seek a number of steps to the right (next) from the given node
        if not node:
            return None
        current = node
        for _ in range(steps):
            current = current.next
        return current
    
    def traverse(self):
        # Traverse and display the elements of the circular linked list
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next


def main(argv: list[str] | None = None) -> int:
    argv = list(argv) if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description="Read a file and write it to stdout")
    parser.add_argument("path", help="Path to file to read; use '-' for stdin")
    args = parser.parse_args(argv)

    rotations = []
    try:
        if args.path == "-":
            data = sys.stdin.buffer.read()
            sys.stdout.buffer.write(data)
            return 0

        p = Path(args.path)
        with p.open("r") as f:
            # Read one line at a time and parse it into an array of tuples
            for line in f:
                direction = line[:1]
                steps = int(line[1:].strip())
                rotations.append((direction, steps))

    except FileNotFoundError:
        print(f"File not found: {args.path}", file=sys.stderr)
        return 2
    except PermissionError:
        print(f"Permission denied: {args.path}", file=sys.stderr)
        return 3
    except Exception as exc:
        print(f"Error reading {args.path}: {exc}", file=sys.stderr)
        return 4
    
    dial = Dial(100)
    dial.seek(50)
    counter = 0

    for direction, steps in rotations:
        if direction == "L":
            dial.rotate_left(steps)
            if dial.current_number() == 0:
                counter += 1
        elif direction == "R":
            dial.rotate_right(steps)
            if dial.current_number() == 0:
                counter += 1
        else:
            print(f"Unknown direction: {direction}", file=sys.stderr)
            return 5

    print(counter)
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
