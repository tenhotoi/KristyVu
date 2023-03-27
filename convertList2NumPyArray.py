# https://www.statology.org/convert-list-to-numpy-array/

"""
https://numpy.org/install/
https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
https://stackoverflow.com/questions/40868345/checking-whether-pip-is-installed
https://www.computerhope.com/issues/ch000549.htm#:~:text=Setting%20the%20path%20and%20variables%20in%20Windows%2011,Power%20User%20Task%20Menu%2C%20select%20the%20System%20option.

py -m pip install numpy
Collecting numpy
  Downloading numpy-1.24.2-cp311-cp311-win_amd64.whl (14.8 MB)
     ---------------------------------------- 14.8/14.8 MB 3.6 MB/s eta 0:00:00
Installing collected packages: numpy

  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-1.24.2
"""

import numpy as np

# Example 1: Convert List to NumPy Array

#create list of values
my_list = [3, 4, 4, 5, 7, 8, 12, 14, 14, 16, 19]

#convert list to NumPy array
my_array = np.asarray(my_list)

#view NumPy array
print(my_array)

# Output: [ 3  4  4  5  7  8 12 14 14 16 19]

#view object type
print(type(my_array))

# Output: numpy.ndarray

print(my_array.dtype)

#convert list to NumPy array
my_array = np.asarray(my_list, dtype=np.float64)


#view NumPy array
print(my_array)

#view data type of NumPy array
print(my_array.dtype)

new_array = [i*2 for i in my_array if i % 2 == 0]
print(new_array)

# Example 2: Convert List of Lists to NumPy Array of Arrays

import numpy as np

#create list of lists
my_list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#convert list to NumPy array
my_array = np.asarray(my_list_of_lists)

#view NumPy array
print(my_array)
#view data type of NumPy array
print(my_array.dtype)
print(type(my_array))

"""
Output:

[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

"""
https://www.geeksforgeeks.org/numpy-array-in-python/
Python lists are a substitute for arrays, but they fail to deliver the performance required while computing large sets of numerical data. To address this issue we use a python library called NumPy. The word NumPy stands for Numerical Python. NumPy offers an array object called ndarray. They are similar to standard python sequences but differ in certain key factors.
https://www.geeksforgeeks.org/difference-between-numpy-array-and-numpy-matrix/?ref=rp
"""
tup = (1, 2, 3, 4)
numpyArr = np.array(tup)
  
print("tup =", tup, "and type(tup) =", type(tup))
print("numpyArr =", numpyArr, "and type(numpyArr) =", type(numpyArr))


import numpy as np
 
mat = np.matrix([[1, 2, 3],
                 [5, 6, 7],
                 [4, 6, 8]])
 
print("Matrix is : \n", mat)
print(type(mat))
#view data type of NumPy array
print(mat.dtype)

"""
https://www.geeksforgeeks.org/difference-between-numpy-array-and-numpy-matrix/?ref=rp

Matrix is 2-dimensional while ndarray can be multi-dimensional
Example 1: 

Here, we can print all the dimensions of an array in np.array.
"""

import numpy as np
 
arr1 = np.array([1, 2, 3])
print("1D array\n", arr1)
print("\n")
 
arr2 = np.array([[1, 2], [3, 4]])
print("2D array\n", arr2)
print("\n")
 
C = np.array([[[1, 2], [3, 4]],
             [[5, 6], [7, 8]],
             [[9, 10], [11, 12]]])
print("3D array\n", C)

"""
Example 2: 

Matrix works normally for a 2D matrix and if a 1D matrix will convert into 2D Matrix, but if we pass a 3D matrix it will through an error. 
"""
import numpy as np
 
arr1 = np.matrix([1, 2, 3])
print(arr1)
print("Dimensions:", arr1.ndim)
print("\n")

"""
arr2 = np.matrix([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]],
                  [[9, 10], [11, 12]]])
print("2D array\n", arr2)


Different functionality of  * operator in ndarray and Matrix
Example 1:

Array * operator does simple multiplication.
Array multiplication:
 [[ 1  4]
 [ 9 16]]
"""

a = np.array([[1, 2],
             [3, 4]])
b = np.array([[1, 2],
             [3, 4]])
 
print("Array multiplication: \n", a*b)

"""
Example 2: 

While it does matrix multiplication.
https://www.mathsisfun.com/algebra/matrix-multiplying.html
(1, 2) • (1, 3) = 1x1 + 2x3 = 7
(1, 2) • (2, 4) = 1x2 + 2x4 = 10
(3, 4) • (1, 3) = 3x1 + 4x3 = 15
(3, 4) • (2, 4) = 3x2 + 4x4 = 22
Matrix multiplication:
 [[ 7 10]
 [15 22]]
"""
a = np.matrix([[1, 2],
             [3, 4]])
b = np.matrix([[1, 2],
             [3, 4]])
 
print("Matrix multiplication: \n", a*b)

"""
Matrix has an array.I for inverse, but ndarray has linalg.inv
Example 1: 

The inverse can be done with array.I in ndarray.
Inverse
 [[-2.   1. ]
 [ 1.5 -0.5]]

https://byjus.com/maths/inverse-matrix/
(arr1)^(-1) = (1/(1x4 - 2x3))([[4, -2],
                                [-3, 1]])
            = (-1/2)([[4, -2],
                    [-3, 1]])
"""
arr1 = np.matrix([[1, 2],
              [3, 4]])
 
print('Inverse \n', arr1.I)

"""
Example 2:

The inverse can be done with np.linalg.inv in matrix.
Inverse
 [[-2.   1. ]
 [ 1.5 -0.5]]

https://byjus.com/maths/inverse-matrix/
"""
b = np.array([[1, 2],
             [3, 4]])
 
print('Inverse \n', np.linalg.inv(b))

# https://www.geeksforgeeks.org/calculate-the-difference-between-the-maximum-and-the-minimum-values-of-a-given-numpy-array-along-the-second-axis/?ref=rp
# Example 1:
# import library
import numpy as np
  
# create a numpy 2d-array
x = np.array([[100, 20, 305],
             [ 200, 40, 300]])
  
print("given array:\n", x)
  
# get maximum element row
# wise from numpy array
max1 = np.amax(x ,1)
print('max1 is: ', max1)
  
# get minimum element row
# wise from numpy array
min1 = np.amin(x, 1)
print('min1 is: ', min1)
  
# print the row-wise max 
# and min difference
print("difference:\n", max1 - min1)

# Example 2:
import numpy as np
  
# list
x = [12, 13, 14, 15, 16]
y = [17, 18, 19, 20, 21]
  
# create a numpy 2d-array
array = np.array([x, y]).reshape((2, 5))
  
print("original array:\n", array)
  
# find max and min elements
# row-wise
max1, min1 = np.amax(array, 1), np.amin(array,1)
  
# print the row-wise max 
# and min difference
print("Difference:\n", max1 - min1)

