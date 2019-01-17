import unittest
import os.path
import sys
import numpy as np

root_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)
from block_ciphers.data_encryption_standard.permutations import expansion, pc1, pc2


class TestExpansion(unittest.TestCase):
    def test_should_throw_if_text_size_is_not_32bits(self):
        with self.assertRaisesRegex(Exception, "length of text must be"):
            expansion("12345")

    def test_should_remap_bits_correctly(self):
        mapped_bits = expansion("test")
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


class TestPC1(unittest.TestCase):
    def test_should_throw_if_text_size_is_not_64bits(self):
        with self.assertRaisesRegex(Exception, "length of text must be"):
            pc1("123456789")

    def test_should_remap_bits_correctly(self):
        mapped_bits = pc1("test1234")
        np.testing.assert_array_equal(np.array([
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 1,
            1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1,
            0, 1, 1, 0, 0, 1, 0,
            0, 1, 0, 0, 0, 1, 0,
            1, 1, 0, 0, 0, 0, 0,
            0, 0, 0, 1, 1, 0, 1
        ]), mapped_bits)


class TestPC2(unittest.TestCase):
    def test_should_throw_if_text_size_is_not_56bits(self):
        with self.assertRaisesRegex(Exception, "length of text must be"):
            pc2("12345678")

    def test_should_remap_bits_correctly(self):
        mapped_bits = pc2("test123")
        np.testing.assert_array_equal(np.array([
            1, 0, 1, 1, 0, 0,
            1, 1, 0, 1, 0, 1,
            1, 1, 0, 1, 1, 0,
            1, 0, 1, 1, 0, 1,
            0, 1, 0, 0, 1, 1,
            1, 1, 1, 0, 0, 0,
            1, 0, 0, 1, 0, 0,
            0, 0, 0, 1, 0, 0
        ]), mapped_bits)


if __name__ == '__main__':
    unittest.main()
