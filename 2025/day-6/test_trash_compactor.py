#!/usr/bin/env python3

import unittest
from trash_compactor import *

class TrashCompactorTest(unittest.TestCase):
    def test_line_to_array(self):
        line = "1   2     3"
        arr = line_to_array(line)
        self.assertEqual(arr, ["1", "2", "3"])
    
    
    def test_line_to_array_with_fixed_widths(self):
        line = "  12 345   6  "
        column_width = 4
        arr = line_to_array_with_fixed_widths(line, column_width)
        self.assertEqual(arr, ["  12", "345 ", " 6  "])


    def test_find_column_widths(self):
        data = [
            "1   22    333",
            "444 5     66",
            "7   8888  9"
        ]
        col_widths = find_column_widths(data)
        self.assertEqual(col_widths, [3, 4, 3])


    def test_pad_with_zeros(self):
        self.assertEqual(pad_with_zeros(" 123", 4), "0123")
        self.assertEqual(pad_with_zeros("123 ", 4), "1230")
        self.assertEqual(pad_with_zeros("1234", 4), "1234")


    def test_do_cephalapod_math(self):
        values = ["123", " 45", "  6"]
        result_add = do_cephalapod_math("*", values)
        self.assertEqual(result_add, 8544)

        values = ["328", "64 ", "98 "]
        result_add = do_cephalapod_math("+", values)
        self.assertEqual(result_add, 625)



if __name__ == "__main__":
    unittest.main()
