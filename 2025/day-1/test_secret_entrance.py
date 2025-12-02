#!/usr/bin/env python3

import unittest
from secret_entrance import SecretEntrance, Node, CircularLinkedList, Dial

class TestDial(unittest.TestCase):
    def test_seek(self):
        dial = Dial(10)
        self.assertEqual(dial.seek(0), 0)
        self.assertEqual(dial.seek(5), 5)
        self.assertEqual(dial.seek(9), 9)

    def test_current_number(self):
        dial = Dial(10)
        self.assertEqual(dial.current_number(), 0)
        dial.seek(5)
        self.assertEqual(dial.current_number(), 5)

    def test_rotate_left(self):
        dial = Dial(10)
        dial.seek(5)
        dial.rotate_left(3)
        self.assertEqual(dial.current_number(), 2)
        dial.rotate_left(5)
        self.assertEqual(dial.current_number(), 7)

    def test_rotate_right(self):
        dial = Dial(10)
        dial.seek(5)
        dial.rotate_right(3)
        self.assertEqual(dial.current_number(), 8)
        dial.rotate_right(5)
        self.assertEqual(dial.current_number(), 3)

class TestSecretEntrance(unittest.TestCase):
    
    def test_parse_line(self):
        result = SecretEntrance.parse_line("any input line")
        self.assertEqual(result, ("R", 3))

    def test_generate_dial(self):
        dial = SecretEntrance.generate_dial(100)
        values = []
        current = dial.head
        for _ in range(100):
            values.append(current.data)
            current = current.next
        self.assertEqual(values, list(range(100)))

    def test_circular_linked_list_append_and_seek(self):
        cll = CircularLinkedList()
        for i in range(5):
            cll.append(i)
        
        # Test seek
        self.assertEqual(cll.seek(0).data, 0)
        self.assertEqual(cll.seek(1).data, 1)
        self.assertEqual(cll.seek(4).data, 4)

    def test_left_rotation(self):
        cll = CircularLinkedList()
        for i in range(50):
            cll.append(i)
        
        node = cll.seek(10)  # Node with data 10
        node = cll.left_seek(node, 3)  # Move left 3 steps
        self.assertEqual(node.data, 7)

    def test_right_rotation(self):
        cll = CircularLinkedList()
        for i in range(50):
            cll.append(i)
        
        node = cll.seek(10)  # Node with data 10
        node = cll.right_seek(node, 3)  # Move right 3 steps
        self.assertEqual(node.data, 13)

if __name__ == "__main__":
    unittest.main()
