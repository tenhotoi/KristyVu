
"""
https://media.licdn.com/dms/document/C4D1FAQG_KSXOcjXLRw/feedshare-document-pdf-analyzed/0/1678359984872?e=1679529600&v=beta&t=kv-VM0VivqsPnds6--CKYD5CmjE6iPjse1-YQgqn0u0

Syntax of Lambda function:

lambda argument(s) : expression

There can be a number os arguments but only one expression.
Options:

1. map
2. filter
3. reduce

"""
# regular function
def multiply_by_2(x):
    return x*2

# lambda function
result = lambda x: x*2

print(multiply_by_2(5))
print(result(5))

# find a+b whole square using lambda
square = lambda a,b: a**2 + b**2 + 2*(a*b)
print(square(2,5))

input_list = [2, 3, 4, 5, 6, 7]

# using map function to square each list item
map_answer = map(lambda x: x*x, input_list)
print(list(map_answer))

# using filter function to filter list item with value less than 5
filter_answer = filter(lambda x: x<5, input_list)
print(list(filter_answer))

from functools import reduce

reduce_answer = reduce(lambda x,y: x+y, input_list)
print(reduce_answer)

# Python3 code to demonstrate working of
# Extract Dictionaries with given Key
# Using filter() + lambda
 
# initializing list
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
             {'gfg': 1, 'for': 10, 'geeks': 9},
             {'love': 3, 'gfg': 4}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing key
key = 'good'
 
# checking for key using in operator
# keys() used to get keys
# filter() + lambda used to perform filtration
# res = list(filter(lambda sub: key in list(sub.keys()), test_list))
res = list(filter(lambda sub: key in sub, test_list))
 
# printing result
print("The filtered Dictionaries after Kristy modified: " + str(res))

# using map function to square in range
map_answer = map(lambda x: (x+1)*2, range(10))
print(list(map_answer))

# Sort a Python String with sorted()
word = 'da ta ?gy!'

sorted_word = ''.join(filter(lambda x:x.isalpha(), sorted(word,key=lambda x:x.lower())))

print(sorted_word)

# Returns: aadgty

# Sort a Python String with sorted()
word = 'da ta ?gy!'

sorted_word = ''.join(filter(lambda x:x.isalpha(), sorted(word,key=lambda x:x.lower())))

print(sorted_word)

# Returns: aadgty

"""
Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.

a = 10 = 1010 (Binary)
b = 4 =  0100 (Binary)

a ^ b = 1010
         ^
        0100
      = 1110
      = 14 (Decimal)
1 = 01
2 = 10
3 = 11
xor = 00
"""
# Python program to Find the Number
# Occurring Odd Number of Times (only works for this case: when numbers are 1, 2, and 3; list of odd numbers of these numbers)
# using Lambda expression and reduce function
 
from functools import reduce
from collections import Counter
 
def oddTimes(input):
     # write lambda expression and apply
     # reduce function over input list
     # until single value is left
     # expression reduces value of a ^ b into single value
     # a starts from 0 and b from 1
     # ((((((1 ^ 2)^3)^2)^3)^1)^3)
     # ^ means XOR
     print (reduce(lambda a, b: a ^ b, input))
 
# Driver program
if __name__ == "__main__":
    # input = [1, 2, 3, 2, 3, 1, 3]
    input = [1, 2, 3, 2, 3, 1, 3, 3, 2]
    print(Counter(input))
    oddTimes(input)

"""
Output:
Counter({3: 3, 1: 2, 2: 2})
3
"""

print(5//2)
print(5/2)
"""
2
2.5
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
