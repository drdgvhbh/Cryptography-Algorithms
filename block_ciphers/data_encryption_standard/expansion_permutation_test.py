import unittest
from expansion_permutation import expansion_permutation


class TestExpansionPermutation(unittest.TestCase):
    def test_should_throw_if_text_size_is_greater_than_32bits(self):
        self.assertRaises(Exception, expansion_permutation, "12345")


if __name__ == '__main__':
    unittest.main()
