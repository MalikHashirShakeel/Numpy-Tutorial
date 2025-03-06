import numpy as np

#Looping over numpy arrays using nditer

a = np.arange(12).reshape(3, 4)
print(a)

for x in np.nditer(a, order = 'C'):#C-style iteration
    print(x)

for x in np.nditer(a, order = 'F'):#Fortran-style iteration
    print(x)

for x in np.nditer(a, flags = ['external_loop'], order = 'F'):#external loop iteration
    print(x)

for x in np.nditer(a, op_flags = ['readwrite']):#read-write iteration
    x[...] = x * x

print(a)

#Looping over two numpy arrays using nditer
b = np.arange(3, 15).reshape(3, 4)

for x, y in np.nditer([a, b]):
    print(x, y)

c = np.arange(3).reshape(3, 1)

for x, y in np.nditer([a, c]):
    print(x, y)

