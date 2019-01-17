import os.path
import sys
import numpy as np
from collections import deque

root_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..'))
sys.path.append(root_path)
from block_ciphers.data_encryption_standard.permutations import pc1, pc2

_MAX_KEY_LENGTH = 8
_DES_ROUNDS = 16

_left_rotations = [
    1,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    1
]


class RoundKeyFactory:
    def __init__(self, key):
        if len(key) > _MAX_KEY_LENGTH:
            raise Exception(f'length of key must not exceed {_MAX_KEY_LENGTH}')
        self._key = key
        pass

    def generate_subkeys(self):
        contracted_key = pc1(self._key)
        left_key, right_key = np.array_split(contracted_key, 2)
        left_key = deque(left_key)
        right_key = deque(right_key)

        subkeys = []
        for rotation_count in _left_rotations:
            left_key.rotate(-rotation_count)
            right_key.rotate(-rotation_count)
            subkeys.append([*left_key, *right_key])

        return np.array(list(map(lambda x: pc2(x), subkeys)))


def mix_keys(key_a, key_b):
    [ord(x) ^ ord(y) for x, y in zip(key_a, key_b)]
