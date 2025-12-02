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

    def seek(self, steps: int) -> Node:
        # Seek a number of steps from the head and return the node at that position
        if not self.head:
            return None
        current = self.head
        for _ in range(steps):
            current = current.next
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
    parser.add_argument("-e", "--encoding", help="Decode bytes with this encoding (default: raw binary)")
    args = parser.parse_args(argv)

    circular_list = CircularLinkedList()
    circular_list.append(1)
    circular_list.append(2)
    circular_list.append(3)

    print("Traversing Circular Linked List:")
    circular_list.traverse()

    try:
        if args.path == "-":
            data = sys.stdin.buffer.read()
            if args.encoding:
                try:
                    text = data.decode(args.encoding)
                except Exception as exc:  # decoding error
                    print(f"Decoding error: {exc}", file=sys.stderr)
                    return 2
                sys.stdout.write(text)
            else:
                sys.stdout.buffer.write(data)
            return 0

        p = Path(args.path)
        if args.encoding:
            with p.open("r", encoding=args.encoding) as f:
                sys.stdout.write(f.read())
        else:
            with p.open("rb") as f:
                sys.stdout.buffer.write(f.read())
        return 0

    except FileNotFoundError:
        print(f"File not found: {args.path}", file=sys.stderr)
        return 2
    except PermissionError:
        print(f"Permission denied: {args.path}", file=sys.stderr)
        return 3
    except Exception as exc:
        print(f"Error reading {args.path}: {exc}", file=sys.stderr)
        return 4



if __name__ == "__main__":
    raise SystemExit(main())
