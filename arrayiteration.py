# https://stackoverflow.com/questions/66417329/how-to-quickly-iterate-through-an-array-in-python

import sys
import time

t0=time.time() 
arr=list(range(1,11))
for i in arr:
    arr[i-1]= 'dsaijhjsdha' + str(i) + '\n'

arr = ['Line number ' + str(i) + ' \n' for i in range(1,11)]    
print(arr)
print('Beautiful form in printing: \n', ''.join(arr))
open("bla.txt", "wb").write(bytearray(''.join(arr),'utf-8'))
d=time.time()-t0
print ("duration: %.2f s." % d)

# https://www.geeksforgeeks.org/10-essential-python-tips-tricks-programmers/?ref=rp

test = [8, 1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5, 9]
print('Original list is: ', test)
print(max(set(test), key = test.count))
# Output: 4
# print(max(set(test), test.count)) # <<<< not supported between instances of 'builtin_function_or_method' and 'set'
print(max(set(test)))
# Output: 9
# print(max(set(test), key = test.append([10, 11])))
# print(max(set(test), key = test.extend([10, 11]))) # <<<<<<<<< TypeError: unhashable type: 'list'
print(test)
print(set(test))
# print(set([[1,2],[3,4]]))  # <<<<<<<<<<<<< TypeError: unhashable type: 'list'
print(list(enumerate(test)))
print([x for x,y in enumerate(test)])
print([y for x,y in enumerate(test)])
"""
Output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
[8, 1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 5, 9]
"""
print(list(dict.fromkeys(test)))
print(list(set(test)))
"""
Output:
[8, 1, 2, 3, 4, 5, 9]
[1, 2, 3, 4, 5, 8, 9]
"""

initial = [1, 1, 9, 1, 9, 6, 9, 7]
print('Original list is: ', initial)
result = [y for x, y in enumerate(initial)]
print(result)
"""
Output:
[1, 1, 9, 1, 9, 6, 9, 7]
"""
print(list(set(initial)))
"""
OUtput:
[1, 7, 9, 6]
"""
# Remove Duplicates and Keep the Order:
# https://blog.finxter.com/python-list-remove-duplicates-and-keep-the-order/

result = list(dict.fromkeys(initial))
print(result)

"""
Output:
[1, 9, 6, 7]
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
