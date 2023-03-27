"""
List comprehensions are a useful way of quickly creating lists whose contents obey a rule.
For example, we can do the following:
"""
# a list comprehension 
cubes = [i**3 for i in range(5)]
print(cubes)

"""
List comprehensions are inspired by set-builder notation in mathematics.
A list comprehension can also contain an if statement to enforce a condition on values in the list.
Example:
"""
evens=[i**2 for i in range(10) if i**2 % 2 == 0] 
print(evens)
 
"""Problem
Gien a word as input, output a list, containing only the letters of the word that are not vowels.
The vowels are a, e, i, o, u.
Sample Input
awesome
Sample Output
['w', 's', 'm']
Use a list comprehension to create the required list of letters and output it.
"""
word = input()
vowels=["a","e","i","o","u","A","E","I","O","U"]
a=[i for i in word if i not in vowels]
print(a)

arr = [9, 11, 2, 3, 4, 5, 6, 7, 8, 9, 0, 8]
doubles = [number for number in arr if arr.count(number * 2) == 1]
print('Input: ', arr)
print('All elements of the list for which there exists exactly one element of the list which is twice that number: ', doubles)

"""
Problem
Letter Counter 
Given a string as input, you need to output how many times each letter appears in the string.
You decide to store the data in a dictionary, with the letters as the keys, and the corresponding counts as 
the values.
Create a program to take a string as input and output a dictionary, which represents the letter count.
Sample Input
hello
Sample Output
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
You need to output the dictionary object.
Note, that the letters are in the order of appearance in the string.
"""
text = input()
dict = {}

for letter in text:
    dict.__setitem__(letter,text.count(letter))

print(dict)

"""
Input
incomprehensibilities
Output
{'i': 5, 'n': 2, 'c': 1, 'o': 1, 'm': 1, 'p': 1, 'r': 1, 'e': 3, 'h': 1, 's': 2, 'b': 1, 'l': 1, 't': 1}
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
