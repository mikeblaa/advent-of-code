#!/usr/bin/env python3

import unittest
from trash_compactor import *

class TrashCompactorTest(unittest.TestCase):
    def test_line_to_array(self):
        line = "1   2     3"
        arr = line_to_array(line)
        self.assertEqual(arr, ["1", "2", "3"])
    
if __name__ == "__main__":
    unittest.main()
