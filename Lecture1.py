import numpy as np
import sys
import time

#size comparison
python_list = list(range(1000))
numpy_array = np.arange(1000)

print(sys.getsizeof(python_list))
print(sys.getsizeof(numpy_array))


#time comparison
l1 = list(range(1000000))
l2 = list(range(1000000))

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Time taken by python list: ", (time.time()-start) * 1000, "ms")

n1 = np.arange(1000000)
n2 = np.arange(1000000)

start = time.time()
result = n1 + n2
print("Time taken by numpy array: ", (time.time()-start) * 1000, "ms")