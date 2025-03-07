import numpy as np
import sys

list = [1, 2, 3, 4, 5]

array = np.array(list)

print(list)

print(array)

print("list ",sys.getsizeof(list))

print("array ",array.nbytes)

print(type(array))

print(type(list))