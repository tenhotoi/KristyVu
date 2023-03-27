# https://datagy.io/python-sort-string/

# Sort a Python String with sorted()
word = 'datagy'

sorted_word = sorted(word)
print(sorted_word)

# Returns: ['a', 'a', 'd', 'g', 't', 'y']

# Sort a Python String with sorted()
word = 'datagy'

sorted_word = sorted(word)
sorted_word = ''.join(sorted_word)
print(sorted_word)

# Returns: aadgty

# Sort a Python String with sorted()
word = 'datagy'

sorted_word = ''.join(sorted(word))
print(sorted_word)

# Returns: aadgty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word))
print(sorted_word)

# Returns: Daagty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word, key=str.lower))
print(sorted_word)

# Returns: aaDgty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(word.lower()))
print(sorted_word)

# Returns: aadgty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(set(word)))
print(sorted_word)

# Returns: Dagty

# Sort a Python String with sorted()
word = 'Datagy'

sorted_word = ''.join(sorted(set(word), key=str.lower))
print(sorted_word)

# Returns: aDgty

#Sort a Python String with sorted()
word = 'da ta ?gy!'

sorted_word = ''.join(filter(lambda x:x.isalpha(), sorted(word,key=lambda x:x.lower())))

print(sorted_word)

# Returns: aadgty

print(s := ''.join(filter(lambda x: x.isalnum(), sorted(word, key= lambda x: x.lower()))))
# Returns: aadgty

# print(s := ''.join(filter(str.isalnum(), sorted(word, key= lambda x: x.lower()))))
"""
    print(s := ''.join(filter(str.isalnum(), sorted(word, key= lambda x: x.lower()))))
                              ^^^^^^^^^^^^^
TypeError: unbound method str.isalnum() needs an argument
"""

print(s := ''.join(filter(str.isalnum, sorted(word, key= lambda x: x.lower()))))
# Returns: aadgty


# https://www.tutorialspoint.com/How-to-correctly-sort-a-string-with-a-number-inside-in-Python

"""
This type of sort in which you want to sort on the basis of numbers within string is called natural sort or human sort. For example, if you have the text:

['Hello1','Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
 Then you want the sorted list to be:

['Hello1', 'Hello2','Hello12', 'Hello17', 'Hello25', 'Hello29']
 and not:

['Hello1','Hello12', 'Hello17', 'Hello2', 'Hello25', 'Hello29']
 To do this we can use the extra parameter that sort() uses. This is a function that is called to calculate the key from the entry in the list. We use regex to extract the number from the string and sort on both text and number. 
"""

import re
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]
my_list =['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
my_list.sort(key=natural_keys)
print(my_list)

"""
This will give you the output:

['Hello1','Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
"""

def function(x):
    print([int(c) if c.isdigit() else c for c in re.split('(\d+)', x)])  # <========== note: () wrapping around \d+ here
    """
    ['hello', 1, '']
    ['hello', 9, '']
    ['hello', 99, '']
    ['hello', 12, '']
    ['hello', 22, '']
    """
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)]
print(sort_s := sorted(my_list, key= function))                                 # key doesn't alter original values
print(sorted_s := sorted(my_list, key=lambda c: [int(c) if c.isdigit() else c for c in re.split("(\d+)", word) for word in my_list]))

"""
Output:

['Hello', 1, '']
['Hello', 2, '']
['Hello', 12, '']
['Hello', 17, '']
['Hello', 25, '']
['Hello', 29, '']
['Hello1', 'Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
['Hello1', 'Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
"""

# initializing list
test_list = [ '4', '6', '7', '2', '1']
print(list_sorted := sorted(test_list))


s = 'Name Character Sex Age'
print(sorted(s))
# Output: [' ', ' ', ' ', 'A', 'C', 'N', 'S', 'a', 'a', 'a', 'c', 'e', 'e', 'e', 'e', 'g', 'h', 'm', 'r', 'r', 't', 'x']
print(''.join(sorted(s)))
# Output: ACNSaaaceeeeghmrrtx
print(''.join(sorted(s.split())))
# Output: AgeCharacterNameSex
print(sorted(s.split()))
# Output: ['Age', 'Character', 'Name', 'Sex']
print(' '.join(sorted(s.split())))
# Output: Age Character Name Sex
print(s)
# Output: Name Character Sex Age

# reverse words
print(s.split()[::-1])
# Output: ['Age', 'Sex', 'Character', 'Name']
print(' '.join(s.split()[::-1]))
# Output: Age Sex Character Name
print(' '.join([word[::-1] for word in s.split()]))
# emaN retcarahC xeS egA
print(' '.join([word[::-1] for word in s.split()[::-1]]))
# egA xeS retcarahC emaN

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