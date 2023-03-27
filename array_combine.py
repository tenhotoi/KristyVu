# https://datagy.io/python-combine-lists/

# >>>>>>>>>>>>>>>>>> METHOD 1 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Merge Two Lists
list1 = ['datagy', 'is', 'a', 'site']
list2 = ['to', 'learn', 'python']

list3 = list1 + list2

print(list3)

# >>>>>>>>>>>>>>>>>> METHOD 2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Merge Two Lists
list1 = ['datagy', 'is', 'a', 'site']
list2 = ['to', 'learn', 'python']

list3 = [*list1, *list2]

print(list3)

# >>>>>>>>>>>>>>>>>> METHOD 3 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Merge Two Lists in Alternating Fashion
list1 = ['1a', '2a', '3a']
list2 = ['1b', '2b', '3b']

list3 = [item for sublist in zip(list1, list2) for item in sublist]
print(list3)
print(list(zip(list1, list2)))

"""
[('1a', '1b'), ('2a', '2b'), ('3a', '3b')]
['1a', '1b', '2a', '2b', '3a', '3b']
"""

# >>>>>>>>>>>>>>>>>> METHOD 4 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine Python Lists without Duplicates
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]

list3 = list(set(list1 + list2))

print(list3)

"""
# >>>>>>>>>>>>>>>>>> METHOD 5 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Concactenate Python Arrays
import numpy as np

list1 = [1,2,3]
list2 = [4,5,6]

array1 = np.array(list1)
array2 = np.array(list2)

array3 = np.concatenate((array1, array2.T))

print(array3)
"""
# >>>>>>>>>>>>>>>>>> METHOD 6 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine Two Python Lists with a For Loop
list1 = ['datagy', 'is', 'a', 'site']
list2 = ['to', 'learn', 'python']

# Combine all items
for item in list2:
    list1.append(item)

print(list1)
# Returns: ['datagy', 'is', 'a', 'site', 'to', 'learn', 'python']

# >>>>>>>>>>>>>>>>>> METHOD 7 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine items conditionally
list1 = ['datagy', 'is', 'a', 'site']
list2 = ['to', 'learn', 'python']
for item in list2:
    if len(item) > 3:
        list1.append(item)

print(list1)

# >>>>>>>>>>>>>>>>>> METHOD 8 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine Two Python Lists with a List Comprehension
list1 = ['datagy', 'is', 'a', 'site']
list2 = ['to', 'learn', 'python']

[list1.append(item) for item in list2]

# >>>>>>>>>>>>>>>>>> METHOD 9 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine common elements between two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3 = list(set(list1).intersection(set(list2)))
print(list3)

# >>>>>>>>>>>>>>>>>> METHOD 10 <<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Combine unique elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(common_elements := list(set(list1).intersection(set(list2))))
print(combined := list1 + list2)

for item in common_elements:
    combined = [element for element in combined if element != item]

print(combined)
# Returns: [1, 2, 5, 6]

# >>>>>>>>>>>>>>>>>> METHOD 10 my way <<<<<<<<<<<<<<<<<<<<<<<<<<<<
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common_elements = list(set(list1).intersection(set(list2)))
combined = list(set(list1 + list2))
final = [i for i in combined if i not in common_elements]
print(final)

"""
https://stackoverflow.com/questions/53958419/sort-an-array-which-contains-number-and-strings

arr.sort((a, b) => ((typeof b === "number") - (typeof a === "number")) || (a > b ? 1 : -1));

const arr = [9, 5, '2', 'ab', '3', -1];

const nums = arr.filter(n => typeof n == "number").sort((a, b) => a - b); // If the data type of a given element is a number store it in this array (and then sort numerically)
const non_nums = arr.filter(x => typeof x != "number").sort(); // Store everything that is not a number in an array (and then sort lexicographically)

const res = [...nums, ...non_nums]; // combine the two arrays
console.log(res); // [-1, 5, 9, "2", "3", "ab"]
"""

l = 4
m = 10
for i in range(m, l-1, -1):
    print(i)

for i in range(m, l, -1):
    print(i)

"""
10
9
8
7
6
5
4  <======== this is (l - 1)

10
9
8
7
6
5
>>>>>>>>>>>>> it won't print anything when '-1' is not there in the 3rd location
"""
l = 0
m = 4
for i in range(m, l-1, -1):
    print(i)

for i in range(m, l, -1):
    print(i)

"""
4
3
2
1
0   <=========== same rule when reverse: never reach to upper bound (2nd location), thus need to have (l -1) since reverse counting here

4
3
2
1
"""


"""
Python lambda λ : functions
by Alex Kelin
prompt command result
Concept function_name = ( lambda variable(s): result if 
condition else result_2 )
Condition and ternery is 
optional
Simple value 
operation squared = lambda x: x ** 2
>>> print(squared(5))
25
Multiple value 
operation value = lambda x, y: x + 2 - y
>>> print(value(2,1))
3
Check single value
check_num = (
 lambda x: f'{x} is greater than 5' if x > 5
 else f'{x} is not greater than 5')
>>> print(check_num(6))
6 is greater than 5
Check multiple 
values
check_num = (
 lambda x, y: f'{x} and {y} are greater than 5' if 
x > 5 and y > 5
 else f'{x} and {y} are not greater than 5')
>>> print(check_num(2,3))
2 and 3 are not greater than 
5
Check for value
lib = ['a', 'b', 'c', 'd']
boolean = list(map(lambda x: x == 'b', lib))
>>> print(boolean)
[False, True, False, False]
Any() or all() 
value check
lst = [1, 2, 3, 4, 5]
check_1 = any(map(lambda x: x % 2 == 0, lst))
check_2 = all(map(lambda x: x % 2 == 0, lst))
>>> print(check_1)
True
>>> print(check_2)
False
Operations with 
list
lib = [3, 1, 2]
a = [lambda x=_: x + 1 for _ in lib] 
b = [(lambda x: x * 2)(_()) for _ in a] 
>>> print(a)
[<function 
<listcomp>.<lambda> at 
0x104761a80>, ……]
>>> print(b)
[8, 4, 6]
lib = [3, 1, 2, 4]
c = list(map(lambda x: x, lib))
d = list(map(lambda x: x / 2, lib))
>>> print(c)
[3, 1, 2, 4]
>>> print(d)
[1.5, 0.5, 1.0, 2.0]
lib = ['Bob', 'Mike', 'John', 'Jerry']
e = list(map(lambda x: f' Hi, {x}', lib))
>>> print(e)
[' Hi, Bob', ' Hi, Mike', ' Hi, 
John', ' Hi, Jerry']
lib_1 = ['a', 'b', 'c', 'd']
lib_2 = [20, 'M', 'T', 'V']
f = list(map(lambda x, y: f'{x} - {y}', lib_1, lib_2))
>>> print(f)
['a - 20', 'b - M', 'c - T', 'd - V']
Operations with 
dict
a = ['a', 'b', 'c']
b = [1, 2, 3]
new_dict = dict(zip(a, map(lambda x: x+1, b)))
>>> print(new_dict)
{'a': 2, 'b': 3, 'c': 4}
Determine length 
of a string
names = ['Bob', 'Mike', 'John', 'Jerry']
lengths = [len(x) for x in names]
>>> print(lengths)
[3, 4, 4, 5]
Opposite boolean booleans = [True, False, True]
result = [not x for x in booleans]
>>> print(result)
[False, True, False]
Extract positive 
values
my_list = [1, -2, 3, -4, 5]
pos_nums = list(filter(lambda x: x > 0, my_list))
>>> print(pos_nums)
[1, 3, 5]

https://media.licdn.com/dms/document/C4E1FAQFGYgUJCd18Mg/feedshare-document-pdf-analyzed/0/1678706696754?e=1679529600&v=beta&t=kdDmJSRn9OCx3vkMvzhpzRzeHjGnv8TuJwQLabBbpC0
"""

lib = [3, 1, 2]
print(a := [lambda x=_: x + 1 for _ in lib]) 
print(b := [(lambda x: x * 2)(_()) for _ in a]) 
# a = [lambda x=_: x + 1 for _ in lib]
# b = [(lambda x: x * 2)(_()) for _ in a]

lib_1 = ['a', 'b', 'c', 'd']
lib_2 = [20, 'M', 'T', 'V']
print(f := list(map(lambda x, y: f'{x} - {y}', lib_1, lib_2)))

if not None:
    print('it\'s not None')

def solution1():
    print('solution1 is called')
def solution2():
    print('solution2 is called')
def solution3():
    print('solution3 is called')
num = [1 , 2, 3]
"""
[<function <listcomp>.<lambda> at 0x0000015A19E5CEA0>, <function <listcomp>.<lambda> at 0x0000015A19E5CFE0>, <function <listcomp>.<lambda> at 0x0000015A19E5DEE0>]
[8, 4, 6]
['a - 20', 'b - M', 'c - T', 'd - V']
it's not None
['solution1()', 'solution2()', 'solution3()']
"""
print(l := list(map(lambda x: f'solution{x}()', num)))
print([eval(x) for x in l])
"""
solution1 is called
solution2 is called
solution3 is called
[None, None, None]
"""

# # https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/
# initializing list
test_list = [ '4', '6', '7', '2', '1']
from itertools import combinations
print(list(combinations([int(x) for x in test_list], 3)))
# [(4, 6, 7), (4, 6, 2), (4, 6, 1), (4, 7, 2), (4, 7, 1), (4, 2, 1), (6, 7, 2), (6, 7, 1), (6, 2, 1), (7, 2, 1)]
val = 12
print([sol for sol in list(combinations([int(x) for x in test_list], 3)) if sum(sol) == val])
# [(4, 6, 2), (4, 7, 1)]
print(list(filter(lambda x: sum(x)==val, list(combinations([int(x) for x in test_list], 3)))))
# [(4, 6, 2), (4, 7, 1)]