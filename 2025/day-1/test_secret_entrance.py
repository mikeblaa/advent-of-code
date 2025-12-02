#!/usr/bin/env python3

import unittest
from secret_entrance import Node, CircularLinkedList, Dial

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

    def test_zero_click_count(self):
        dial = Dial(10)
        dial.seek(1)
        dial.rotate_left(2)  # Should pass 0 once
        self.assertEqual(dial.get_zero_click_count(), 1)
        dial.rotate_right(3)  # Should pass 0 once more
        self.assertEqual(dial.get_zero_click_count(), 2)
        dial.rotate_left(10)  # Full rotation, should pass 0 once more
        self.assertEqual(dial.get_zero_click_count(), 3)
        dial.rotate_left(2)  # Should end on 0
        self.assertEqual(dial.get_zero_click_count(), 4)

if __name__ == "__main__":
    unittest.main()
