import numpy as np

arr1 = np.array([[1, 2, 3], 
                  [4, 5, 6]])
arr2 = np.array([[10, 20, 30], 
                  [40, 50, 60]])

print("Array 1 : \n",arr1)
print("Array 2 : \n",arr2)

print("Element-wise Addition: \n",np.add(arr1,arr2))

print("Element-wise subtract: \n",np.subtract(arr1,arr2))

print("Element-wise multiply: \n",np.multiply(arr1,arr2))

print("Element-wise divide: \n",np.divide(arr1,arr2))

print("Element-wise power: \n",np.power(arr1,2))

print("Element-wise Modules: \n",np.mod(arr2,8))

print("Element-wise Dot: \n",np.dot(arr1,arr2.T))

print("Element-wise Exponential: \n",np.exp(arr1))

print("Element-wise logarithmic: \n",np.log(arr1))

print("Sine of each element in arr :\n ",np.sin(arr1))
print("Cosine of each element in arr :\n ",np.cos(arr1))
print("Tangent of each element in arr :\n ",np.tan(arr1))


print("\n\n Statistical Function : ")

print("Mean : ",np.mean(arr1))

print("Median : ",np.median(arr1))

print("Standard Deviation : ",np.std(arr1))

print("Variance : ",np.var(arr1))

print("Product : ",np.prod(arr1))

print("Min value : ",np.min(arr1))

print("Max Value: ",np.max(arr1))

print("Index of Min : ",np.argmin(arr1))

print("Index of Max : ",np.argmax(arr1))





