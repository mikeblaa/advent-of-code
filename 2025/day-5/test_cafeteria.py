#!/usr/bin/env python3

import unittest
from cafeteria import *

class CafeteriaTest(unittest.TestCase):
    
    def test_add_range_to_set(self):
        s = set()
        add_range_to_set(s, 5, 10)
        self.assertTrue(s == {5, 6, 7, 8, 9, 10})
        self.assertTrue(5 in s)
        self.assertFalse(4 in s)

        add_range_to_set(s, 15,20)
        self.assertTrue(s == {5, 6, 7, 8, 9, 10, 15, 16, 17, 18, 19, 20})

    def test_range_to_start_end(self):
        r = "5-10"
        start, end = range_to_start_end(r)
        self.assertEqual(start, 5)
        self.assertEqual(end, 10)

        r = "0-0"
        start, end = range_to_start_end(r)
        self.assertEqual(start, 0)
        self.assertEqual(end, 0)
        
    def test_range_size(self):
        r = "5-10"
        size = range_size(r)
        self.assertEqual(size, 6)

        r = "0-0"
        size = range_size(r)
        self.assertEqual(size, 1)
    
if __name__ == "__main__":
    unittest.main()
