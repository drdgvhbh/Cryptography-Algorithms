#!/usr/bin/env python3

import unittest
import numpy as np
from expansion_permutation import expansion_permutation


class TestExpansionPermutation(unittest.TestCase):
    def test_should_throw_if_text_size_is_greater_than_32bits(self):
        with self.assertRaisesRegex(Exception, "length of text must not exceed"):
            expansion_permutation("12345")

    def test_should_remap_bits_correctly(self):
        mapped_bits = expansion_permutation("test")
        np.testing.assert_array_equal(np.array([
            0, 0, 1, 1, 1, 0,
            1, 0, 1, 0, 0, 0,
            0, 0, 1, 1, 0, 0,
            0, 0, 1, 0, 1, 0,
            1, 0, 1, 1, 1, 0,
            1, 0, 0, 1, 1, 0,
            1, 0, 1, 1, 1, 0,
            1, 0, 1, 0, 0, 0
        ]), mapped_bits)


if __name__ == '__main__':
    unittest.main()
