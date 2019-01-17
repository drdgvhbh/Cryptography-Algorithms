import numpy as np

_CHAR_BIT_SIZE = 8


def char_to_bin(character):
    return str(format(ord(character), 'b')).zfill(_CHAR_BIT_SIZE)


def bin_repr(string):
    return np.array([int(c)
                     for c in "".join(char_to_bin(x) for x in string)])
