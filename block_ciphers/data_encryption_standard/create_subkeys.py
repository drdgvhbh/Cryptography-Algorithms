import numpy as np

CHAR_BIT_SIZE = 8
MAX_BIT_SIZE = 64
MAX_LENGTH = MAX_BIT_SIZE // CHAR_BIT_SIZE

PC1 = np.array([
    57,	49,	41,	33,	25,	17,	9,
    1,	58,	50,	42,	34,	26,	18,
    10,	2,	59,	51,	43,	35,	27,
    19,	11,	3,	60,	52,	44,	36,
    63,	55,	47,	39,	31,	23,	15,
    7,	62,	54,	46,	38,	30,	22,
    14,	6,	61,	53,	45,	37,	29,
    21,	13,	5,	28,	20,	12,	4
])


def _pc1_permutation(text):
    if len(text) > MAX_LENGTH:
        raise Exception(f'length of key must not exceed {MAX_LENGTH}')
    bit_repr = np.array([int(c)
                         for c in "".join(_char_to_bin(x) for x in text)])
    return np.array([bit_repr[x] for x in expansion_permutation_lookup_table])


def create_subkeys(key):
    if len(key) > MAX_LENGTH:
        raise Exception(f'length of key must not exceed {MAX_LENGTH}')
    permuted_key = [key[x] for x in PC1]
