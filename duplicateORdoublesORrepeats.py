# find and return the elements that are repeated exactly twice in the list

import collections

print('===================== EXAMPLE 1 ==========================')
arr = [2, 8, 4, 6, 1, 2, 8, 4, 7, 9, 4, 5] 
repeatsOnlyTwice = [
    item 
    for item, count in collections.Counter(arr).items() 
    if count == 2
]
print('repeatsOnlyTwice is: ', repeatsOnlyTwice)

# if you want just to remove duplicates you can use
print(set(arr))

print(set([x for x in arr if arr.count(x) == 2])) # set is used to remove duplicates
print(list(set([x for x in arr if arr.count(x) == 2]))) # to print it as a list

print([x for x in arr if arr.count(x) == 2]) # set is NOT used, so NOT remove duplicates
print(list([x for x in arr if arr.count(x) == 2])) # to print it as a list

NOduplicates = [number for number in arr if arr.count(number) == 1]
# unique_NOduplicates = list(set(NOduplicates))
print('Unique numbers are: ', NOduplicates)

print('===================== EXAMPLE 2 ==========================')
# Finding Duplicate Items in a Python List
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

duplicates = [number for number in numbers if numbers.count(number) > 1]
unique_duplicates = list(set(duplicates))

print(unique_duplicates)

# Returns: [2, 3, 5]

print(set([2, 2, 1, 8, 7, 8]))

# Finding Duplicate Items in a Python List and Count Them
from collections import Counter
numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]

counts = dict(Counter(numbers))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)

# Returns: {2: 2, 3: 4, 5: 3}

print('===================== EXAMPLE 3 ==========================')
my_list = [1, 2, 3, 4, 5]
my_new_list = [i * 5 for i in my_list]
print(my_new_list)

print('===================== EXAMPLE 4 ==========================')
arr = [9, 11, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8]
doubles = [
    item
    for item, count in collections.Counter(arr).items() 
    if count == 2
]
print(doubles)

doubles = [number for number in arr if arr.count(number * 2) == 1]
print('Input: ', arr)
print('All elements of the list for which there exists exactly one element of the list which is twice that number: ', doubles)
print(arr[-1])
print(reversed(arr))
print(list(reversed(arr)))
print(list(set(arr)))
print(list(dict.fromkeys(arr)))

# write a python code to remove duplicates from the list without using any in-built functions, and no using temporary list
def remove_dup(a):
   i = 0
   while i < len(a):
      j = i + 1
      while j < len(a):
         if a[i] == a[j]:
            del a[j]
         else:
            j += 1
      i += 1

print('===================== EXAMPLE 5 ==========================')
s = ['cat','dog','cat','mouse','dog']
remove_dup(s)
print(s)

# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/


# Python 3 code to demonstrate
# removing duplicate elements from the list
l = [1, 2, 4, 2, 1, 4, 5]
print("Original List: ", l)
res = [*set(l)]
print("List after removing duplicate elements: ", res)

# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension
 
# initializing list
test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : "
      + str(test_list))
 
# using list comprehension
# to remove duplicated
# from list
res = []
[res.append(x) for x in test_list if x not in res]
 
# printing list after removal
print ("The list after removing duplicates : "
       + str(res))

# Python 3 code to demonstrate
# removing duplicated from list
# using set()
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
 
# using set()
# to remove duplicated
# from list
test_list = list(set(test_list))
 
# printing list after removal
# distorted ordering
print ("The list after removing duplicates : "
        + str(test_list))

# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension + enumerate()
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
 
# using list comprehension + enumerate()
# to remove duplicated
# from list
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
 
# printing list after removal
print ("The list after removing duplicates : "
        + str(res))

# Python 3 code to demonstrate
# removing duplicated from list
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
       + str(test_list))
 
# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
res = list(OrderedDict.fromkeys(test_list))
 
# printing list after removal
print ("The list after removing duplicates : "
       + str(res))

# Python 3 code to demonstrate
# removing duplicates from list
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
 
res = []
for i in test_list:
    if i not in res:
        res.append(i)
 
# printing list after removal
print("The list after removing duplicates : " + str(res))

# Python 3 code to demonstrate
# removing duplicated from list
# using list comprehension and arr.index
 
# initializing list
arr = [1, 5, 3, 6, 3, 5, 6, 1]
print ('The original list is : '+ str(arr))
 
# using list comprehension + arr.index()
# to remove duplicated
# from list
res = [arr[i] for i in range(len(arr)) if i == arr.index(arr[i]) ]
 
# printing list after removal
# of duplicate
print('The list after removing duplicates :'
        ,res)

from collections import Counter
# Python 3 code to demonstrate
# removing duplicated from list
# using Counter() method
 
# initializing list
arr = [1, 5, 3, 6, 3, 5, 6, 1]
print ('The original list is : '+ str(arr))
 
# using Counter() + keys()
# to remove duplicated
# from list
temp = Counter(arr)
res = [*temp]
 
# printing list after removal
# of duplicate
print('The list after removing duplicates :'
        ,res)

# Python 3 code to demonstrate
# removing duplicated from list
# using numpy
  
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
  
# using numpy
import numpy as np
  
# removing duplicated
# from list
res = np.unique(test_list)
  
# printing list after removal
print ("The list after removing duplicates : "
        + str(res))
#This code is contributed by Edula Vinay Kumar Reddy

# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
# remove duplicates from a list, while preserving order?
items = [1, 2, 0, 1, 3, 2]
a = list(dict.fromkeys(items))  # Or [*dict.fromkeys(items)] if you prefer
print('result of list of dictionary is: ', a)

