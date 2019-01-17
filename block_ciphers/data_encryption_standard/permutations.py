import os.path
import sys
import numpy as np

root_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)
from util.strings import char_to_bin, bin_repr

_CHAR_BIT_SIZE = 8

_expansion_lookup_table = np.array([
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
])

_EXPANSION_MAX_BIT_SIZE = 32
_EXPANSION_MAX_LENGTH = _EXPANSION_MAX_BIT_SIZE // _CHAR_BIT_SIZE


def expansion(text):
    return _permute(text, _expansion_lookup_table, _EXPANSION_MAX_LENGTH)


_PC1_lookup_table = np.array([
    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3
])

_PC1_MAX_BIT_SIZE = 64
_PC1_MAX_LENGTH = _PC1_MAX_BIT_SIZE // _CHAR_BIT_SIZE


def pc1(text):
    return _permute(text, _PC1_lookup_table, _PC1_MAX_LENGTH)


_PC2_lookup_table = np.array([
    13, 16, 10, 23, 0, 4, 2, 27,
    14, 5, 20, 9, 22, 18, 11, 3,
    25, 7, 15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54, 29, 39,
    50, 44, 32, 47, 43, 48, 38, 55,
    33, 52, 45, 41, 49, 35, 28, 31
])

_PC2_MAX_BIT_SIZE = 56
_PC2_MAX_LENGTH = _PC2_MAX_BIT_SIZE // _CHAR_BIT_SIZE


def pc2(text):
    return _permute(text, _PC2_lookup_table, _PC2_MAX_LENGTH)


def _permute(text, table, max_length):
    if len(text) != max_length and len(text) != max_length * _CHAR_BIT_SIZE:
        raise Exception(
            f'length of text must be {max_length}')
    bin_text = None
    if len(text) == max_length:
        bin_text = bin_repr(text)
    else:
        bin_text = text
    return np.array([bin_text[x] for x in table])
