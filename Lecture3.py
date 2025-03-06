import numpy as np

#Indexing on numpy arrays
arr = np.array([1,2,3,4,5])
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

arr2 = np.arange(1, 10).reshape(3, 3)#reshaping the array to 3x3
print(arr2)
print(arr2[0, 0])
print(arr2[0, 1])
print(arr2[0, 2])

#Slicing on numpy arrays
arr3 = np.arange(1, 10)
print(arr3[0 : 5])
print(arr2[0 : 2, 2])#slicing the row 0, 1 of 3rd column
print(arr2[2, 1 : 3])#slicing the column 1, 2 of 3rd row
print(arr2[0 : 2, 0 : 2])#slicing the 1st 2 rows and 1st 2 columns

#Iterating over numpy arrays
for row in arr2:
    print(row)

for cell in arr2.flat:#flat is an iterator that iterates over all the elements of the array
    print(cell)

#Stacking of numpy arrays
arr4 = np.arange(1, 5).reshape(2, 2)
arr5 = np.arange(5, 9).reshape(2, 2)
print(np.vstack((arr4, arr5)))#vertical stacking
print(np.hstack((arr4, arr5)))#horizontal stacking

#Splitting of numpy arrays
arr6 = np.arange(30).reshape(2, 15)
print(np.hsplit(arr6, 3))#horizontal splitting
print(np.vsplit(arr6, 2))#vertical splitting

#Boolean indexing
arr4 = arr2 > 5
print(arr4)
print(arr2[arr4])#returns the elements that are greater than 5
arr2[arr4] = 0#set the elements that are greater than 5 to 0
print(arr2)
