import numpy as np
print("1D array")
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print("2D array")
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print("3D array")
arr2 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
                 [[10,11,12],[13,14,15],[16,17,18]],
                 [[19,20,21],[22,23,24],[25,26,27]]
                 ])
print(arr2)
print("4D Array")
arr3 = np.array([
                [[[1,2,3],[4,5,6],[7,8,9]],
                 [[10,11,12],[13,14,15],[16,17,18]]],
                
                [[[19,20,21],[22,23,24],[25,26,27]],
                 [[28,29,30],[31,32,33],[34,35,36]]]
                ])

print(arr3)

print("\n\nArray information : ")

print("Shape of array : ",arr2.shape)

print("Size of array : ",arr2.size)

print("Data type of array : ",arr2.dtype)

print("No of Dimensions : ",arr2.ndim)

print("Item Size(bytes) : ",arr2.itemsize)


print("\n\n Reshaping Array0")
print("Original Array : ")
print(arr1)

new_shape = (1,9)
print("Original array converted into 1 row and 8 columns : ",np.reshape(arr1,new_shape))

print("2D array flattened into 1D : ",arr1.flatten())

print("Transpose of the array : \n",arr1.T)
