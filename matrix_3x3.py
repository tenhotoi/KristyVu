
import random

product = ['p1', 'p2', 'p3']
firmware = ['fw1', 'fw2', 'fw3']
version = ['1', '2', '3']
test_results = [None]*3
test_result = round(random.random())

print(zip_arr := list(zip(product, firmware, version)))
# [('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]

res_tmp = [{p:{f:{v:t}}} for (p, f, v, t) in zip(product, firmware, version, test_results)]
# print(res_tmp)
# # [{'p1': {'fw1': {'1': None}}}, {'p2': {'fw2': {'2': None}}}, {'p3': {'fw3': {'3': None}}}]

res_tmp = [{p:{f:{v:random.random()}}} for p in product for f in firmware for v in version]
print(res_tmp)
"""
[{'p1': {'fw1': {'1': None}}}, {'p1': {'fw1': {'2': None}}}, {'p1': {'fw1': {'3': None}}}, {'p1': {'fw2': {'1': None}}}, {'p1': {'fw2': {'2': None}}}, {'p1': {'fw2': {'3': None}}}, {'p1': {'fw3': {'1': None}}}, {'p1': {'fw3': {'2': None}}}, {'p1': {'fw3': {'3': None}}}, {'p2': {'fw1': {'1': None}}}, {'p2': {'fw1': {'2': None}}}, {'p2': {'fw1': {'3': None}}}, {'p2': {'fw2': {'1': None}}}, {'p2': {'fw2': {'2': None}}}, {'p2': {'fw2': {'3': None}}}, {'p2': {'fw3': {'1': None}}}, {'p2': {'fw3': {'2': None}}}, {'p2': {'fw3': {'3': None}}}, {'p3': {'fw1': {'1': None}}}, {'p3': {'fw1': {'2': None}}}, {'p3': {'fw1': {'3': None}}}, {'p3': {'fw2': {'1': None}}}, {'p3': {'fw2': {'2': None}}}, {'p3': {'fw2': {'3': None}}}, {'p3': {'fw3': {'1': None}}}, {'p3': {'fw3': {'2': None}}}, {'p3': {'fw3': {'3': None}}}]
"""
print(len(res_tmp))
# 27

print(type(res_tmp))
# <class 'list'>

dict_tmp = {}
for each in res_tmp:
    dict_tmp.update(each)

print(dict_tmp)
# {'p1': {'fw3': {'3': None}}, 'p2': {'fw3': {'3': None}}, 'p3': {'fw3': {'3': None}}}

print(type(dict_tmp))
# <class 'dict'>

from itertools import combinations
print(len(list(combinations(product + firmware + version, 3))))
# 84

import random
results = {}
for p in product:
    for f in firmware:
        for v in version:
            result = 1
            results.update({p:{f:{v:random.random()}}})
            # print(results)
"""
{'p1': {'fw1': {'1': 1}}}
{'p1': {'fw1': {'2': 1}}}
{'p1': {'fw1': {'3': 1}}}
{'p1': {'fw2': {'1': 1}}}
{'p1': {'fw2': {'2': 1}}}
{'p1': {'fw2': {'3': 1}}}
{'p1': {'fw3': {'1': 1}}}
{'p1': {'fw3': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw1': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw1': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw1': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw2': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw2': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw2': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw1': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw1': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw1': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw2': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw2': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw2': {'3': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw3': {'1': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw3': {'2': 1}}}
{'p1': {'fw3': {'3': 1}}, 'p2': {'fw3': {'3': 1}}, 'p3': {'fw3': {'3': 1}}}
"""

# print(sum(results[p][f][v].values() for p in product for f in firmware for v in version))
# print(results.values))


# print(results['p1'])

# {'p1': {'f3': {'3': 1}}, 'p3': {'f3': {'3': 1}}}

# print(sum(results))
# test = {}
# test_dict = dict([test.update{p:{f:v}} for p in product f in firmware v in vertion])

# https://www.geeksforgeeks.org/python-convert-lists-to-nested-dictionary/?ref=rp


# Python3 code to demonstrate working of
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()
 
# initializing list
test_list1 = ["gfg", 'is', 'best']
test_list2 = ['ratings', 'price', 'score']
test_list3 = [5, 6, 7]

# printing original list
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))
print("The original list 3 is : " + str(test_list3))
 
# Convert Lists to Nestings Dictionary
# Using list comprehension + zip()

res = [{a: {b: c}} for (a, b, c) in zip(test_list1, test_list2, test_list3)]

# printing result
print("The constructed dictionary : " + str(res))

"""
Output : 
The original list 1 is : ['gfg', 'is', 'best']
The original list 2 is : ['ratings', 'price', 'score']
The original list 3 is : [5, 6, 7]
The constructed dictionary : [{'gfg': {'ratings': 5}}, {'is': {'price': 6}}, {'best': {'score': 7}}]

Time complexity: O(n) because it uses list comprehension to create a new list with the same number of elements as the input lists, and then the zip() function iterates over all the elements of the input lists once. Therefore, the time complexity is linear with respect to the length of the input lists.
Auxiliary space: O(n) because it creates a new list with the same number of elements as the input lists, which requires O(n) space. Additionally, it creates a dictionary for each element of the new list, which requires O(1) space, so the overall auxiliary space complexity is also O(n).
"""

print(list(zip(test_list1, test_list2, test_list3)))
print(list(zip(firmware, list(zip(version, test_results)))))
print(tmp_list := list(zip(product, list(zip(firmware, list(zip(version, test_results)))))))
print(tmp_dic := dict(tmp_list).keys())
print(tmp_dic := dict(tmp_list).values())

"""
[('gfg', 'ratings', 5), ('is', 'price', 6), ('best', 'score', 7)]
[('fw1', ('1', None)), ('fw2', ('2', None)), ('fw3', ('3', None))]
[('p1', ('fw1', ('1', None))), ('p2', ('fw2', ('2', None))), ('p3', ('fw3', ('3', None)))]
dict_keys(['p1', 'p2', 'p3'])
dict_values([('fw1', ('1', None)), ('fw2', ('2', None)), ('fw3', ('3', None))])
"""


res_tmp = [{(p, f, v):round(random.random())} for p in product for f in firmware for v in version]
print(res_tmp)
# [{('p1', 'fw1', '1'): True}, {('p1', 'fw1', '2'): True}, {('p1', 'fw1', '3'): True}, {('p1', 'fw2', '1'): True}, {('p1', 'fw2', '2'): True}, {('p1', 'fw2', '3'): True}, {('p1', 'fw3', '1'): True}, {('p1', 'fw3', '2'): True}, {('p1', 'fw3', '3'): True}, {('p2', 'fw1', '1'): True}, {('p2', 'fw1', '2'): True}, {('p2', 'fw1', '3'): True}, {('p2', 'fw2', '1'): True}, {('p2', 'fw2', '2'): True}, {('p2', 'fw2', '3'): True}, {('p2', 'fw3', '1'): True}, {('p2', 'fw3', '2'): True}, {('p2', 'fw3', '3'): True}, {('p3', 'fw1', '1'): True}, {('p3', 'fw1', '2'): True}, {('p3', 'fw1', '3'): True}, {('p3', 'fw2', '1'): True}, {('p3', 'fw2', '2'): True}, {('p3', 'fw2', '3'): True}, {('p3', 'fw3', '1'): True}, {('p3', 'fw3', '2'): True}, {('p3', 'fw3', '3'): True}]    


dict_tmp = {}
for each in res_tmp:
    dict_tmp.update(each)

print(dict_tmp)
# {('p1', 'fw1', '1'): True, ('p1', 'fw1', '2'): True, ('p1', 'fw1', '3'): True, ('p1', 'fw2', '1'): True, ('p1', 'fw2', '2'): True, ('p1', 'fw2', '3'): True, ('p1', 'fw3', '1'): True, ('p1', 'fw3', '2'): True, ('p1', 'fw3', '3'): True, ('p2', 'fw1', '1'): True, ('p2', 'fw1', '2'): True, ('p2', 'fw1', '3'): True, ('p2', 'fw2', '1'): True, ('p2', 'fw2', '2'): True, ('p2', 'fw2', '3'): True, ('p2', 'fw3', '1'): True, ('p2', 'fw3', '2'): True, ('p2', 'fw3', '3'): True, ('p3', 'fw1', '1'): True, ('p3', 'fw1', '2'): True, ('p3', 'fw1', '3'): True, ('p3', 'fw2', '1'): True, ('p3', 'fw2', '2'): True, ('p3', 'fw2', '3'): True, ('p3', 'fw3', '1'): True, ('p3', 'fw3', '2'): True, ('p3', 'fw3', '3'): True}<class 'dict'>


print(type(dict_tmp))
# <class 'dict'>

print(sumNum := sum(dict_tmp.values()))
# 27

print(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti'))
print(sum(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print('p' in ['p', 'd', 's'])
print('why doesn\'t it print?', '1' in ('p', 'd', '1'))

maxNum = 0
for p in product:
    print([v for k, v in dict_tmp.items() if p in k])
    print(sumNum := sum([v for k, v in dict_tmp.items() if p in k]))
    print(maxNum := max(maxNum, sumNum))

maxNum = 0
for f in firmware:
    print([v for k, v in dict_tmp.items() if f in k])
    print(sumNum := sum([v for k, v in dict_tmp.items() if f in k]))
    print(maxNum := max(maxNum, sumNum))

maxNum = 0
for ver in version:
    print([val for k, val in dict_tmp.items() if ver in k])
    print(sumNum := sum([val for k, val in dict_tmp.items() if ver in k]))
    print(maxNum := max(maxNum, sumNum))


print(list_3x3 := [[p, f, v] for p in product for f in firmware for v in version])
print(len(list_3x3))
"""
[['p1', 'fw1', '1'], 
['p1', 'fw1', '2'], 
['p1', 'fw1', '3'], 
['p1', 'fw2', '1'], 
['p1', 'fw2', '2'], 
['p1', 'fw2', '3'], 
['p1', 'fw3', '1'], 
['p1', 'fw3', '2'], 
['p1', 'fw3', '3'], 
['p2', 'fw1', '1'], 
['p2', 'fw1', '2'], 
['p2', 'fw1', '3'], 
['p2', 'fw2', '1'], 
['p2', 'fw2', '2'], 
['p2', 'fw2', '3'], 
['p2', 'fw3', '1'], 
['p2', 'fw3', '2'], 
['p2', 'fw3', '3'], 
['p3', 'fw1', '1'], 
['p3', 'fw1', '2'], 
['p3', 'fw1', '3'], 
['p3', 'fw2', '1'], 
['p3', 'fw2', '2'], 
['p3', 'fw2', '3'], 
['p3', 'fw3', '1'], 
['p3', 'fw3', '2'], 
['p3', 'fw3', '3']]
27
"""

print(list_3x3 := list(zip(product, firmware, version)))    # I think this is what he wanted hic hic huhu....
# [('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]

# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-86.php
nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print(nums)
"""
3X3 grid with numbers:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
"""

nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(round(random.random()))
print("3X3 grid with numbers:")
print(nums)
# [[0, 1, 0], [0, 1, 1], [0, 0, 0]]

print('sum of 1st row: ', sum(nums[0]))
print('sum of 2nd row: ', sum(nums[1]))
print('sum of 3rd row: ', sum(nums[2]))

print('sums of rows: ', sum_row := list(map(sum,nums)))
print('max of all sums of rows: ', max(list(map(sum, nums))))
print('first row location that have max: ', sum_row.index(max(list(map(sum, nums)))))

"""
sum of 1st row:  2
sum of 2nd row:  2
sum of 3rd row:  1
sums of rows:  [2, 2, 1]
max of all sums of rows:  2
first row location that have max:  0
"""
print(len(nums))
print('sums of columes: ', sum_column := [sum(x) for x in zip(*nums)])
print('max of all columns: ', max(sum_column))
print('first column location that have max:', sum_column.index(max(sum_column)))

"""
3X3 grid with numbers:
[[1, 0, 1], [1, 0, 0], [0, 1, 1]]
sum of 1st row:  2
sum of 2nd row:  1
sum of 3rd row:  2
sums of rows:  [2, 1, 2]
max of all sums of rows:  2
first row location that have max:  0
3
sums of columes:  [1, 3, 2]
max of all columns:  3
first column location that have max: 1
"""

# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-87.php

# https://www.geeksforgeeks.org/sum-2d-array-python-using-map-function/?ref=rp
print(sumNum := sum(map(sum, nums)))

"""
3X3 grid with numbers:
[[1, 1, 1], [1, 1, 1], [1, 0, 0]]
sum of 1st row:  3
sum of 2nd row:  3
sum of 3rd row:  1
sums of rows:  [3, 3, 1]
max of all sums of rows:  3
first row location that have max:  0
3
sums of columes:  [3, 2, 2]
max of all columns:  3
first column location that have max: 0
7
"""

# Function to calculate sum of all elements in matrix
# sum(arr) is a python inbuilt function which calculates
# sum of each element in a iterable ( array, list etc ).
# map(sum,arr) applies a given function to each item of
# an iterable and returns a list of the results.
def findSum(arr):
 
    # inner map function applies inbuilt function
    # sum on each row of matrix arr and returns
    # list of sum of elements of each row
    return sum(map(sum,arr))
 
# Driver function
if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [2, 1, 2]]
    print ("Sum = ",findSum(arr))

"""
Output
Sum =  26
"""

# Python code to demonstrate working of map()
 
# Function to calculate square of any number
def calculateSquare(n):
    return n*n
 
# numbers is a list of elements
numbers = [1, 2, 3, 4]
 
# Here map function is mapping calculateSquare
# function to each element of numbers list.
# It is similar to pass each element of numbers
# list one by one into calculateSquare function
# and store result in another list
result = map(calculateSquare, numbers)
 
# resultant output will be [1,4,9,16]
print (result)
set_result=list(result)
print(set_result)

"""
Output
<map object at 0x7fdf95d2a6d8>
[1, 4, 9, 16]
"""

# https://www.geeksforgeeks.org/python-map-function-find-row-maximum-number-1s/?ref=rp

"""
Python map function to find row with maximum number of 1’s

Difficulty Level : Basic
Last Updated : 28 Jul, 2022
Read
Discuss
Courses
Practice
Video
Given a boolean 2D array, where each row is sorted. Find the row with the maximum number of 1s. 

Examples:

Input: 

matrix =
        [[0, 1, 1, 1],
         [0, 0, 1, 1],
         [1, 1, 1, 1],  
         [0, 0, 0, 0]]
 
Output: 2
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
We have existing solution for this problem please refer Find the row with maximum number of 1’s. We can solve this problem in python quickly using map() function. Approach is very simple, find sum of all 1’s in each row and then print index of maximum sum in a list because row having maximum 1 will also have maximum sum. 

Implementation:
"""

# Function to find the row with maximum number of 1's
def maxOnes(input):
 
    # map sum function on each row of
    # given matrix
    # it will return list of sum of all one's
    # in each row, then find index of maximum element
    result = list(map(sum,input))
    print (result.index(max(result)))
 
# Driver program
if __name__ == "__main__":
    input = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
    maxOnes(input)

"""
Output
2

Complexity : O(M*N)
"""
print(list_3x3 := list(zip(product, firmware, version)))    # I think this is what he wanted hic hic huhu....
# [('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]

print(list_3x3_start := list(zip(*list_3x3)))    # I think this is what he wanted hic hic huhu....
# [('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]

"""
[('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]
[('p1', 'p2', 'p3'), ('fw1', 'fw2', 'fw3'), ('1', '2', '3')]
"""

# print(indexes := [list_3x3_start.index(x) for x in product + firmware + version])
print(indexes := [x for x in product + firmware + version])
# ['p1', 'p2', 'p3', 'fw1', 'fw2', 'fw3', '1', '2', '3']

def initialize_2d_list(w,h, val = None):
 	 return [[val for x in range(w)] for y in range(h)]
print(initialize_2d_list(2, 2, 0))
# [[0, 0], [0, 0]]
print([[round(random.random()) for x in range(3)] for y in range(3)])
# [[0, 1, 1], [1, 1, 0], [0, 0, 1]]

# https://www.geeksforgeeks.org/python-matrix/

# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))
Row = len(product)
Column = len(firmware)

# Initialize matrix
matrix = []
print("Enter the entries row wise:")
 
# For user input
# A for loop for row entries
for row in range(Row):   
    a = []
    # A for loop for column entries
    for column in range(Column):  
        a.append(round(random.random()))
    matrix.append(a)
 
# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()

# [[p1, 'p2', 'p3'], ['fw1', 'fw2', 'fw3'], ['1', '2', '3']]
print([[x for x in [product, firmware, version]] for y in [product, firmware, version]])

"""
Enter the entries row wise:
1 0 0
1 1 0
0 0 1
print([[x for x in [product, firmware, version]] for y in range(3)])
[[['p1', 'p2', 'p3'], 
['fw1', 'fw2', 'fw3'], 
['1', '2', '3']], 
[['p1', 'p2', 'p3'], 
['fw1', 'fw2', 'fw3'], 
['1', '2', '3']], 
[['p1', 'p2', 'p3'], 
['fw1', 'fw2', 'fw3'], 
['1', '2', '3']]]
print([[x for x in [product, firmware, version]] for y in [product, firmware, version]])
[[['p1', 'p2', 'p3'], ['fw1', 'fw2', 'fw3'], ['1', '2', '3']], 
[['p1', 'p2', 'p3'], ['fw1', 'fw2', 'fw3'], ['1', '2', '3']], 
[['p1', 'p2', 'p3'], ['fw1', 'fw2', 'fw3'], ['1', '2', '3']]]
"""

"""
[['p1', 'fw1', ['1', '2', '3']], 
['p1', 'fw2', ['1', '2', '3']], 
['p1', 'fw3', ['1', '2', '3']], 

['p2', 'fw1', ['1', '2', '3']], 
['p2', 'fw2', ['1', '2', '3']], 
['p2', 'fw3', ['1', '2', '3']],

['p3', 'fw1', ['1', '2', '3']], 
['p3', 'fw2', ['1', '2', '3']], 
['p3', 'fw3', ['1', '2', '3']],

9
"""

print(matrix_new := [[p, f, version] for p in product for f in firmware])
print(len(matrix_new))

"""
[   
    ['p1', 'fw1', ['1', '2', '3']], 
    ['p1', 'fw2', ['1', '2', '3']], 
    ['p1', 'fw3', ['1', '2', '3']], 
    ['p2', 'fw1', ['1', '2', '3']], 
    ['p2', 'fw2', ['1', '2', '3']], 
    ['p2', 'fw3', ['1', '2', '3']], 
    ['p3', 'fw1', ['1', '2', '3']], 
    ['p3', 'fw2', ['1', '2', '3']], 
    ['p3', 'fw3', ['1', '2', '3']]
]
9
"""
print([row for row in zip(*matrix_new)])

"""
[('p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p3', 'p3', 'p3'), 
('fw1', 'fw2', 'fw3', 'fw1', 'fw2', 'fw3', 'fw1', 'fw2', 'fw3'), 
(['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'])]
"""

print(list(zip(*matrix_new)))

"""
[('p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p3', 'p3', 'p3'), 
('fw1', 'fw2', 'fw3', 'fw1', 'fw2', 'fw3', 'fw1', 'fw2', 'fw3'), 
(['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3'])]
"""

#print([set(list(item)) for item in list(zip(*matrix_new))])

print(list(set(list(('p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p3', 'p3', 'p3')))))
# ['p3', 'p2', 'p1']

print(list(set(('p1', 'p1', 'p1', 'p2', 'p2', 'p2', 'p3', 'p3', 'p3'))))
# ['p3', 'p2', 'p1']

print(matrix_result := [[p+f for p in product] for f in firmware])
print(matrix_new := [[[p, f, version] for p in product] for f in firmware])
print(len(matrix_new))
"""
[
    [['p1', 'fw1', ['1', '2', '3']], ['p2', 'fw1', ['1', '2', '3']], ['p3', 'fw1', ['1', '2', '3']]], 
    [['p1', 'fw2', ['1', '2', '3']], ['p2', 'fw2', ['1', '2', '3']], ['p3', 'fw2', ['1', '2', '3']]], 
    [['p1', 'fw3', ['1', '2', '3']], ['p2', 'fw3', ['1', '2', '3']], ['p3', 'fw3', ['1', '2', '3']]]
]
3
"""

print(matrix_new := [[[p, f, version] for f in firmware] for p in product])
print(len(matrix_new))

"""
[
    [['p1', 'fw1', ['1', '2', '3']], ['p1', 'fw2', ['1', '2', '3']], ['p1', 'fw3', ['1', '2', '3']]], 
    [['p2', 'fw1', ['1', '2', '3']], ['p2', 'fw2', ['1', '2', '3']], ['p2', 'fw3', ['1', '2', '3']]], 
    [['p3', 'fw1', ['1', '2', '3']], ['p3', 'fw2', ['1', '2', '3']], ['p3', 'fw3', ['1', '2', '3']]]
]
3
"""


# https://pythonguides.com/python-convert-tuple-to-list/
"""
There are more than 10 ways to convert the given tuple to a list in Python. These are methods are shown below.

Using the built-in function list()
Using a for loop
Using the list comprehension
Using the * operator
Using list constructor with iterable
Using map function and list constructor
Using reduce function of functools module
Using chain method of itertools module
Using the sum function
Using a lambda function
Using the zip function
Using the eval function
Using nested for loops
Using a recursive method
Using the enumerate function
Using the map() and eval()
"""
# Import the sum function from the built-in python library
from builtins import sum

# Define a tuple of countries
t = ("USA", "United Kingdom", "Canada","Brazil")

# Create a list from the elements of the tuple
# The sum function is used to concatenate the list of lists into a single list
print(lst := sum([[x] for x in t], []))
# Output: ['USA', 'United Kingdom', 'Canada', 'Brazil']

# Create a list from the tuple using the "unpacking" operator *
print(lst := [*t])
# Output: ['USA', 'United Kingdom', 'Canada', 'Brazil']

# Convert the tuple to a list using the built-in function `list` and the `iter` function
print(lst := list(iter(t)))

# Convert the tuple to a list using the `list` function and the `map` function with a lambda function
print(lst := list(map(lambda x: x, t)))

# Import the reduce function from the functools module
from functools import reduce
# Convert the tuple to a list using the reduce function
print(lst := reduce(lambda x, y: x + [y], t, []))

# Import the chain method from itertools
from itertools import chain
# Convert the tuple to a list using the chain method
print(lst := list(chain(t)))

# Convert each element in the tuple t to a list and store the result in a list
print(lst := sum(map(lambda x: [x], t), []))

# Unpack each tuple into x and _ and store x in a list
print(lst := [x for x, _ in zip(t, range(len(t)))])

# Convert the tuple to a string representation and then use the built-in eval function to evaluate the string as a list
print(lst := list(eval(str(t))))

# The list "lst" is constructed using a list comprehension that iterates over the elements in "t"
# The enumerate function is used to get the index and value of each element in "t"
# The list comprehension uses the value of each element and discards the index
print(lst := [x for i, x in enumerate(t)])

# Tuple Initialization
t = ('1', '2.5', '3', '4.2')
# Using map to convert tuple elements to list
print(lst := list(map(eval, t)))

"""
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
['USA', 'United Kingdom', 'Canada', 'Brazil']
[1, 2.5, 3, 4.2]
"""

"""
https://www.glassdoor.com/Interview/ChargePoint-Interview-Questions-E722356.htm
1. Write code where one thread generates a random number every second and another thread calculates the byte sum of the random number, and if the byte sum is an even, print the count of total even bytes sums so far. 
2. code to parse the strings, which were files/forlders path in Unix format.
"""

# https://www.pragmaticlinux.com/2022/04/how-to-create-an-array-of-strings-in-python/
import random

my_pets = ['Dog', 'Cat', 'Bunny', 'Fish']
my_pet_index = random.randint(0, 3)
my_pet = my_pets[my_pet_index]
print(my_pet)

def eval_result(str1, str2, str3):
    p = str1[random.randint(0, len(str1) - 1)]
    f = str2[random.randint(0, len(str2) - 1)]
    v = str3[random.randint(0, len(str3) - 1)]

    result = True if round(random.random()) else False
    return(p, f, v, result)

print(eval_result(product, firmware, version))

"""
Cat
p1
fw3
1
0
('p1', 'fw3', '1', 0)
"""

def handle_results():
    product = ['p1', 'p2', 'p3', 'p4']
    firmware = ['fw1', 'fw2', 'fw3', 'fw4']
    version = ['1', '2', '3', '4']

    dic_count = {}
    p_count = {}
    fw_count = {}
    v_count = {}

    while (len(dic_count.keys()) < (len(product))*(len(firmware))*(len(version))):
        (p, f, v, ans) = eval_result(product, firmware, version)
        p_count[p] = p_count.get(p, 0) + ans
        fw_count[f] = fw_count.get(f, 0) + ans        
        v_count[v] = v_count.get(v, 0) + ans    
        dic_count[(p, f, v)] = dic_count.get((p, f, v), 0) + ans         

    print(p_count)
    print(fw_count)
    print(v_count)

    # https://www.geeksforgeeks.org/python-matrix/
    # Initialize matrix
    matrix = []
    
    # For user input
    # A for loop for row entries
    for p in product:   
        a = []
        # A for loop for column entries
        for f in firmware:      
            a.append(round(random.random()))
        matrix.append(a)

    print(dic_count)
    print(len(dic_count.keys()))

    """
    print(sum([val for val in dic_count.values() if 'p1' or 'p2' or 'p3' in dic_count.keys()]))
    print(sum_p1 := sum([val for val in dic_count.values() if 'p1' in dic_count.keys()]))
    print(sum_p2 := sum([val for val in dic_count.values() if 'p2' in dic_count.keys()]))
    print(sum_p3 := sum([val for val in dic_count.values() if 'p3' in dic_count.keys()]))

    Above cancelled lines gave wrong outputs:

    {'p2': 2, 'fw3': 1, ('p2', 'fw3', '3'): 1, 'fw1': 2, ('p2', 'fw1', '1'): 1, 'p3': 2, ('p3', 'fw1', '2'): 0, 'p1': 1, ('p1', 'fw3', '1'): 0, ('p3', 'fw1', '3'): 1, 'fw2': 2, ('p1', 'fw2', '2'): 1, ('p3', 'fw2', '1'): 1, ('p3', 'fw1', '1'): 0, ('p2', 'fw2', '3'): 0}
    dict_values([2, 1, 1, 2, 1, 2, 0, 1, 0, 1, 2, 1, 1, 0, 0])
    15
    15
    15
    15
    1
    2
    2
    Max passed test for product is:  2
    """

    matrix2 = []
    # A for loop for row entries
    for p in product:   
        a = []
        # A for loop for column entries
        for f in firmware:
            # v1_result = dic_count.get((p, f, '1'),  float('-inf'))
            # v2_result = dic_count.get((p, f, '2'),  float('-inf'))
            # v3_result = dic_count.get((p, f, '3'),  float('-inf'))
            # print(v1_result := dic_count.get((p, f, '1'),  0))
            # print(v2_result := dic_count.get((p, f, '2'),  0))
            # print(v3_result := dic_count.get((p, f, '3'),  0))           
            # print(v_sum := v1_result + v2_result + v3_result)
            # print(p, f)
            v_sum = 0
            for v in version:
                v_sum += dic_count[(p, f, v)]
            print(f'({p}, {f}): {v_sum}', end=" ")
            a.append(v_sum)            
        print()
              
        matrix2.append(a)

    print('Max number of passed tests for all products: ', max(p_count.values()))
    print('Max number of passed tests for all products: ', max(sum(dic_count[key] for key in dic_count.keys() if p in key) for p in product))
    print(matrix2)
    print(len(matrix2))
    print('Max number of passed tests for all firmware: ', max(fw_count.values()))    
    print('Max number of passed tests for all firmware: ', max(sum(dic_count[key] for key in dic_count.keys() if f in key) for f in firmware))

    # For printing the matrix
    for row in range(len(product)):
        for column in range(len(firmware)):
            # print(matrix2[row][column])
            print(matrix2[row][column], end=" ")
        print()

    # print(p1_result := dic_count.get('p1', float('-inf')))
    # print(p2_result := dic_count.get('p2', float('-inf')))
    # print(p3_result := dic_count.get('p3', float('-inf')))
    # print('Max passed test for product is: ', max([p1_result, p2_result, p3_result]))
    # print(fw1_result := dic_count.get('fw1', float('-inf')))
    # print(fw2_result := dic_count.get('fw2', float('-inf')))
    # print(fw3_result := dic_count.get('fw3', float('-inf')))
    # print('Max passed test for firmware is: ', max([fw1_result, fw2_result, fw3_result]))
  
    print("Max number of passed tests for all versions: ", max(v_count.values()))
    print('Max number of passed tests for all products: ', max(sum(dic_count[key] for key in dic_count.keys() if v in key) for v in version))

    for key in sorted(dic_count.keys()):
        print(key, dic_count[key])

    # For printing the matrix
    for row in range(len(product)):
        for column in range(len(firmware)):
            print(matrix[row][column], end=" ")
        print()

    print('Max passed test for product is: ', max(sum(row) for row in matrix))
    print(columes := [[*column] for column in zip(*matrix)])
    # print('Max passed test for firmware firmware is: ', max(sum(column) for column in columes))
    print('Max passed test for firmware firmware is: ', max(sum([*column]) for column in zip(*matrix)))
    print('Total of all passed tests: ', sum(map(sum,matrix)))    

    # matrix = [[column for column in range(4)] for row in range(4)]  # can't use this since here we can't have fixed entry (have to call function and extract the result) 
    # print(matrix)

    import pandas as pd
    df = pd.DataFrame(
    matrix2, 
    index=product, 
    columns=firmware)

    print(df)

handle_results()
"""
{'p3': 17, 'p1': 18, 'p2': 22}
{'fw2': 18, 'fw3': 18, 'fw1': 21}
{'1': 19, '2': 22, '3': 16}
{('p3', 'fw2', '1'): 2, ('p1', 'fw3', '2'): 4, ('p3', 'fw3', '2'): 0, ('p2', 'fw2', '2'): 4, ('p1', 'fw1', '2'): 2, ('p2', 'fw1', '2'): 3, ('p1', 'fw3', '3'): 0, ('p2', 'fw3', '3'): 2, ('p2', 'fw1', '3'): 3, ('p2', 'fw2', '1'): 2, ('p1', 'fw1', '3'): 2, ('p2', 'fw3', '1'): 2, ('p3', 'fw1', '2'): 2, ('p3', 'fw3', '1'): 5, ('p2', 'fw1', '1'): 2, ('p1', 'fw2', '3'): 3, ('p2', 'fw3', '2'): 2, ('p1', 'fw3', '1'): 1, ('p2', 'fw2', '3'): 2, ('p1', 'fw2', '1'): 0, ('p3', 'fw1', '1'): 2, ('p3', 'fw3', '3'): 2, ('p1', 'fw2', '2'): 3, ('p3', 'fw2', '2'): 2, ('p1', 'fw1', '1'): 3, ('p3', 'fw1', '3'): 2, ('p3', 'fw2', '3'): 0}
(p1, fw1): 7 (p1, fw2): 6 (p1, fw3): 5
(p2, fw1): 8 (p2, fw2): 8 (p2, fw3): 6
(p3, fw1): 6 (p3, fw2): 4 (p3, fw3): 7
Max number of passed tests for all products:  22
Max number of passed tests for all products:  22
[[7, 6, 5], [8, 8, 6], [6, 4, 7]]
Max number of passed tests for all firmware:  21
Max number of passed tests for all firmware:  21
7 6 5
8 8 6
6 4 7
Max number of passed tests for all versions:  22
Max number of passed tests for all products:  22
('p1', 'fw1', '1') 3
('p1', 'fw1', '2') 2
('p1', 'fw1', '3') 2
('p1', 'fw2', '1') 0
('p1', 'fw2', '2') 3
('p1', 'fw2', '3') 3
('p1', 'fw3', '1') 1
('p1', 'fw3', '2') 4
('p1', 'fw3', '3') 0
('p2', 'fw1', '1') 2
('p2', 'fw1', '2') 3
('p2', 'fw1', '3') 3
('p2', 'fw2', '1') 2
('p2', 'fw2', '2') 4
('p2', 'fw2', '3') 2
('p2', 'fw3', '1') 2
('p2', 'fw3', '2') 2
('p2', 'fw3', '3') 2
('p3', 'fw1', '1') 2
('p3', 'fw1', '2') 2
('p3', 'fw1', '3') 2
('p3', 'fw2', '1') 2
('p3', 'fw2', '2') 2
('p3', 'fw2', '3') 0
('p3', 'fw3', '1') 5
('p3', 'fw3', '2') 0
('p3', 'fw3', '3') 2
0 0 1
0 0 0
1 0 0
Max passed test for product is:  1
[[0, 0, 1], [0, 0, 0], [1, 0, 0]]
Max passed test for firmware firmware is:  1
Total of all passed tests:  2
"""

def eval_result(str1, str2, str3):
    p = str1[random.randint(0, len(str1) - 1)]
    f = str2[random.randint(0, len(str2) - 1)]
    v = str3[random.randint(0, len(str3) - 1)]

    result = True if round(random.random()) else False
    return(p, f, v, result)

def main():
    product = ['p1', 'p2', 'p3']
    firmware = ['fw1', 'fw2', 'fw3']
    version = ['1', '2', '3']

    # print(matrix := list(zip(product, firmware, version)))
    # [('p1', 'fw1', '1'), ('p2', 'fw2', '2'), ('p3', 'fw3', '3')]

    dict_results = dict()
    p_count = {}
    f_count = {}
    v_count = {}

    while (len(dict_results.keys())) < (len(product)*len(firmware)*len(version)):
        p, f, v, r = eval_result(product, firmware, version)
        dict_results[(p, f, v)] = dict_results.get((p, f, v), 0) + r
        p_count[p] = p_count.get(p, 0) + r
        f_count[f] = f_count.get(f, 0) + r
        v_count[v] = v_count.get(v, 0) + r

    print('Number of items in the matrix: ', len(dict_results.items()))
    print(dict_results)
    print(dict_results.values())
    print('Sum of all passed tests: ', sum(dict_results.values()))
    print(p_count)
    print('Max passed test among products: ', max(p_count.values()))
    print(f_count)
    print('Max passed test among firmware: ', max(f_count.values()))
    print(v_count)
    print('Max passed test among versions: ', max(v_count.values()))

    matrix = []
    for i in range(len(p_count)):
        print(p_count[product[i]], f_count[firmware[i]], v_count[version[i]], end=' ')
        print()
        pi_f1 = sum([val for (p, f, v), val in dict_results.items() if (p == product[i] and f == firmware[0])]) 
        pi_f2 = sum([val for (p, f, v), val in dict_results.items() if (p == product[i] and f == firmware[1])]) 
        pi_f3 = sum([val for (p, f, v), val in dict_results.items() if (p == product[i] and f == firmware[2])]) 
        matrix.append([pi_f1, pi_f2, pi_f3])

    import pandas as pd
    df = pd.DataFrame(
    matrix, 
    index=product, 
    columns=firmware)

    print(df)



if __name__ == '__main__':
    main()