# https://www.delftstack.com/howto/numpy/python-compare-arrays/
"""
Compare Two Arrays in Python Using the numpy.array_equal() Method
Compare Two Arrays in Python Using the numpy.allclose() Method
Compare Two Arrays in Python Using the numpy.array_equiv() Method
Compare Two Arrays in Python Using the == Operator and numpy.all() Method
"""

import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

a1 = np.array([1])
a2 = np.array([])
a3 = np.array([])

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3])

print(np.array_equal(a1,a1))
print(np.array_equal(a1,a2))
print(np.array_equal(a3,a2))

"""
Output:

True
False
False
"""

import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

a1 = np.array([1])
a2 = np.array([])
a3 = np.array([])

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3])

print(np.allclose(a1,a2))
# print(np.allclose(a3,a2))

"""
Output:

False
True

The numpy.allclose(a1, a2, rtol=1e-05, atol=1e-08, equal_nan=False) method takes array a1 and a2 as input and returns True if the each element of a1 is equal to corresponding element of a2, or their difference is within the tolerance value.

The value of tolerance is calculated using the a2, rtol, and atol arguments.

atol + rtol*absolute(a2)
"""

import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

a1 = np.array([1])
a2 = np.array([])
a3 = np.array([])

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3])

print(np.array_equiv(a1,a2))
print(np.array_equiv(a3,a2))

"""
Output:

False
False
"""

import numpy as np

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3,4.00001,5,7])

a1 = np.array([1])
a2 = np.array([])
a3 = np.array([])

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3])

print((a1==a2).all())
# print((a3==a2).all())

a1 = [1]
a2 = []
if a1 == a2:
    print("a1 is equal to a2")
else:
    print("a1 is not equal to a2")  # a1 is not equal to a2
     
"""
for np.array():

Traceback (most recent call last):

    if a1 == a2:
       ^^^^^^^^
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
"""
"""
Output:

False
False

"Note
This method returns True if both arrays are empty or one array has a length of 1. <===  not exactly correct
And also will raise an error if the shape of both arrays is not the same; that is why the methods mentioned above must be preferred."

a1 = np.array([1])
a2 = np.array([])
a3 = np.array([])

True
True
False  <====== only np.array_equal(a3, a2) returns False if one array is empty and another array has a length of 1
True
True
True
True
True
True

If both arrays are empty, all return True
"""

"""

a1 = np.array([1,2,4,6,7])
a2 = np.array([1,3,4,5,7])
a3 = np.array([1,3])

print(np.allclose(a3,a2)) and print((a3==a2).all()) don't support this comparation
Others would returns False when array sizes are not the same.
"""

# https://www.geeksforgeeks.org/how-to-compare-two-dictionaries-in-python/
dict1 = {'Name': 'asif', 'Age': 5}
dict2 = {'Name': 'lalita', 'Age': 78}
 
if dict1 == dict2:
    print("dict1 is equal to dict2")
else:
    print("dict1 is not equal to dict2") 

"""
Output:

dict1 is not equal to dict2
"""

dict1 = {'Name': 'asif', 'Age': 5}
dict2 = {'Name': 'asif', 'Age': 5}
 
if len(dict1)!=len(dict2):
    print("Not equal")
     
else:
   
    flag=0
    for i in dict1:
        if dict1.get(i)!=dict2.get(i):
            flag=1
            break
    if flag==0:
        print("Equal")
    else:
        print("Not equal")
"""
Output:

Equal
"""

d = {"a": 3, "b": 2}
d1 = {"a": 2, "b": 3}
res = all((d1.get(k) == v for k, v in d.items()))
print(res)

"""
Output:

False
"""

# pip install deepdiff
from deepdiff import DeepDiff
 
x = {'Name': 'asif', 'Age': 5}
y = {'Name': 'lalita', 'Age': 78}
 
diff = DeepDiff(x, y)
 
print(diff)

"""
Output:

{‘values_changed’: {“root[‘Name’]”: {‘new_value’: ‘lalita’, ‘old_value’: ‘asif’}, “root[‘Age’]”: {‘new_value’: 78, ‘old_value’: 5}}}
"""

shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print(shared_items)
print(len(shared_items))