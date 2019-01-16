#!/usr/bin/env python3

import unittest
import numpy as np
from create_subkeys import create_subkeys


class TestCreateSubkeys(unittest.TestCase):
    def test_should_throw_if_key_size_is_greater_than_64bits(self):
        with self.assertRaisesRegex(Exception, "length of key must not exceed"):
            create_subkeys("123456789")


if __name__ == '__main__':
    unittest.main()
