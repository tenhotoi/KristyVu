# https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string
words = ['this', 'is', 'a', 'sentence']
print('-'.join(words))
#'this-is-a-sentence'
print(' '.join(words))
#'this is a sentence'

# Element-wise concatenation of two NumPy arrays of string
# https://www.geeksforgeeks.org/element-wise-concatenation-of-two-numpy-arrays-of-string/
# importing library numpy as np
import numpy as np
 
# creating array as first_name
first_name = np.array(['Geeks'],
                      dtype = np.str)
print("Printing first name array:")
print(first_name)
 
# creating array as last name
last_name = np.array(['forGeeks'],
                     dtype = np.str)
print("Printing last name array:")
print(last_name)
 
# concat first_name and last_name
# into new array named as full_name
full_name = np.char.add(first_name, last_name)
print("\nPrinting concatenate array as full name:")
print(full_name)

# creating array as first_name
first_name = np.array(['Akash', 'Ayush', 'Diksha',
                       'Radhika'], dtype = np.str)
print("Printing first name array:")
print(first_name)
 
# creating array as last name
last_name = np.array(['Kumar', 'Sharma', 'Tewari',
                      'Pegowal'], dtype = np.str)
print("Printing last name array:")
print(last_name)
 
# concat first_name and last_name
# into new array named as full_name
full_name = np.char.add(first_name, last_name)
print("\nPrinting concatenate array as full name:")
print(full_name)

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

