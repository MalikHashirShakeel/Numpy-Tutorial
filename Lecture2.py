import numpy as np
# Performing basic operations on numpy arrays

#Dimensions of array
arr1 = np.array([1, 2, 3, 4, 5])
print(f"Dimensions of the array {arr1}: {arr1.ndim}")

arr2 = np.array([[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]])
print(f"Dimensions of the array {arr2}: {arr2.ndim}")

#Size of each item in the array
print("Size of each item in the array: ", arr2.itemsize)

arr3 = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(f"Size of each item in the array {arr3}: ", arr3.itemsize)

#size of the array
print("Size of the array", arr3.size)

#Shape of the array
print("Shape of the array", arr3.shape)

#Datatype of the array
print("Datatype of the array", arr3.dtype)

#Initializing zero array
arr4 = np.zeros((3, 4))
print(arr4)

#Initializing ones array
arr5 = np.ones((3, 4))
print(arr5)

arr6 = np.linspace(1, 5, 10)
print(arr6)

arr7 = arr2.reshape(9, 1)
print(arr7)

arr8 = arr7.ravel()
print(arr8)

print(arr2.min())#Minimum element in the array
print(arr2.max())#Maximum element in the array
print(arr2.sum(axis = 0))#Sum of each column
print(arr2.sum(axis = 1))#Sum of each row
print(np.sqrt(arr2))#Square root of each element
print(np.std(arr2))#Standard deviation of the array

arr9 = np.array([[1, 2], [3, 4]])
arr10 = np.array([[5, 6], [7, 8]])

print(arr9 + arr10)#Element wise addition
print(arr9 - arr10)#Element wise subtraction
print(arr9 * arr10)#Element wise multiplication
print(arr9 / arr10)#Element wise division
print(arr9 % arr10)#Element wise modulus

print(arr9.dot(arr10))#Matrix multiplication