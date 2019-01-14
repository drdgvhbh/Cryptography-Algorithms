import numpy as np

expansion_permutation_lookup_table = np.array([
    31, 0,  1,  2,  3,  4,
    3,  4,  5,  6,  7,  8,
    7,  8,  9,  10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
])

CHAR_BIT_SIZE = 8
MAX_BIT_SIZE = 32
MAX_LENGTH = MAX_BIT_SIZE // CHAR_BIT_SIZE


def expansion_permutation(text):
    if len(text) > MAX_LENGTH:
        raise Exception(f'length of text must not exceed {MAX_LENGTH}')
    bit_repr = np.array([int(c)
                         for c in "".join(_char_to_bin(x) for x in text)])
    return np.array([bit_repr[x] for x in expansion_permutation_lookup_table])


def _char_to_bin(character):
    return str(format(ord(character), 'b')).zfill(CHAR_BIT_SIZE)
