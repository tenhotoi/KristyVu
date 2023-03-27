# https://www.delftstack.com/howto/python/python-max-value-in-list/

numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = None

for num in numbers:
    if (max_value is None or num > max_value):
        max_value = num

print('Maximum value:', max_value)

# If the index of the maximum value is needed to further manipulate the output
numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = None
max_idx = None

for idx, num in enumerate(numbers):
    if (max_value is None or num > max_value):
        max_value = num
        max_idx = idx

print('Maximum value:', max_value, "At index: ", max_idx)

# Python has a pre-defined function called max() that returns the maximum value in a list
numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20]

max_value = max(numbers)
print('Maximum value:', max_value)

numbers = [55, 4, 92, 1, 104, 64, 73, 99, 20, 104]

max_value = max(numbers)
print('Maximum value:', max_value, "At index:", numbers.index(max_value))

# string
strings = ['Elephant', 'Kiwi', 'Gorilla', 'Jaguar', 'Kangaroo', 'Cat']

max_value = max(strings)
print('Maximum value:', max_value, "At index:", strings.index(max_value))

# find the maximum value of a nested list in Python
nst = [ [1001, 0.0009], [1005, 0.07682], [1201, 0.57894], [1677, 0.0977] ]

idx, max_value= max(nst, key=lambda item: item[1])

print('Maximum value:', max_value, "At index:",idx)

lst = [1, 2, 45, 55, 5, 4, 4, 4, 4, 4, 4, 5456, 56, 6, 7, 67] 
print(max(lst,key=lst.count))
print(lst.index(max(lst,key=lst.count)))
"""
Output:
4  <========== number 4 occurs most frequently
5  <========== number 4 occurs most frequently, and it's first found index is at location 5 (6th slot)
"""

from collections import Counter

print(Counter(lst).most_common(1))

"""
Output:
[(4, 6)]  <========== number 4 occurs most frequently, which is 6 times
"""

# https://stackoverflow.com/questions/6987285/find-the-item-with-maximum-occurrences-in-a-list
# Here's a simple test of several different implementations:

import sys
from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter
from timeit import timeit

L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]

def max_occurrences_1(seq=L):
    "dict items"
    c = dict()
    for item in seq:
        c[item] = c.get(item, 0) + 1
    return max(c.items(), key=itemgetter(1))

def max_occurrences_3a(seq=L):
    "sort groupby generator expression"
    return max(((k, sum(1 for i in g)) for k, g in groupby(sorted(seq))), key=itemgetter(1))

def max_occurrences_3b(seq=L):
    "sort groupby list comprehension"
    return max([(k, sum(1 for i in g)) for k, g in groupby(sorted(seq))], key=itemgetter(1))

def max_occurrences_4(seq=L):
    "counter"
    return Counter(L).most_common(1)[0]

versions = [max_occurrences_1, max_occurrences_3a, max_occurrences_3b, max_occurrences_4]

print(sys.version, "\n")

for vers in versions:
    print(vers.__doc__, vers(), timeit(vers, number=20000))