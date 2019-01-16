import numpy as np

a = "test"

bit_repr = np.array([int(c) for c in "".join(
    str(format(ord(x), 'b')).zfill(8) for x in a)]).reshape((8, 4))
print(bit_repr)
