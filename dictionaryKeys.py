"""
https://www.geeksforgeeks.org/python-program-to-extract-dictionaries-with-given-key-from-a-list-of-dictionaries/?ref=rp
Python Program to extract Dictionaries with given Key from a list of dictionaries
"""
# Python3 code to demonstrate working of
# Extract Dictionaries with given Key
# Using list comprehension + keys()
 
# initializing list
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
             {'gfg': 1, 'for': 10, 'geeks': 9},
             {'love': 3}, {'testing':'gfg'}]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing key
key = 'gfg'
 
# checking for key using in operator
# keys() used to get keys
# res = [sub for sub in test_list if key in list(sub.keys())]
res = [sub for sub in test_list if key in sub]
 
# printing result
print("The filtered Dictionaries after Kristy modified: " + str(res))

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

# Initializing list of dictionaries
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
             {'gfg': 1, 'for': 10, 'geeks': 9},
             {'love': 3}]
 
# Printing original list
print('The original list is below: \n')
{print(line) for line in test_list}
{print(item) for line in test_list for item in line.items()}
 
# Initializing key
key = 'gfg'
 
# Using for loop to extract dictionaries with given key
result = []
for sub_dict in test_list:
    print('sub keys are: ', list(sub_dict.keys()))
    if key in sub_dict:
        result.append(sub_dict)
 
# Printing result
print('The filtered dictionaries is below: \n')
{print(line) for line in result}
#This code is contributed by Vinay Pinjala.

print('just testing...')
{print("FOUND THE MATCH") for sub in result if key in sub and sub[key] == 2}
for sub in result:
    if key in sub and sub[key] == 2:
        del sub[key]

# Printing result
print('The filtered dictionaries is below: \n')
{print(line) for line in result}

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# Storing dictionaries in a dictionary
users = {
    'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
    }
for username, user_dict in users.items():
    print("\nUsername: " + username)
    full_name = user_dict['first'] + " "
    full_name += user_dict['last']
    location = user_dict['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using dict comprehension
res = dict(item.split("=") for item in ini_string1.split(", "))
 
# Printing resultant string
print("Resultant dictionary", str(res))

# Initialising string
ini_string1 = 'branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using dict comprehension
res = dict(item.split("=") for item in ini_string1.split(", "))
 
# Printing resultant string
print("Resultant dictionary", str(res))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import re
sums = dict()
fh= open(r'my_new_folder/test.txt','r')
for line in fh:
    words = [word.lower() for word in re.findall(r'\b\w+\b', line)]
    for word in (words):
        if word in sums:
            sums[word] += 1
        else:
            sums[word] = 1
print(sums)
fh.close

from pprint import pprint
pprint(sums)

print(maxVal := max([x for x in sums.values()]))

# https://pythonguides.com/python-dictionary-find-a-key-by-value/
mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)]) # Prints george

print(maxKeys := list(sums.keys())[list(sums.values()).index(maxVal)])  # retrun key value from known maxVal, but only the 1st key found
"""
{'hello': 2, 'this': 6, 'is': 6, 'delhi': 2, 'paris': 2, 'london': 2}
{'delhi': 2, 'hello': 2, 'is': 6, 'london': 2, 'paris': 2, 'this': 6}
6
george
this
"""
maxKeys = []
for k, v in sums.items():
    if v == maxVal:
        maxKeys.append(k)
print(maxKeys)                                                          # retrun all key values from known maxVal

print([k for k, v in sums.items() if v == maxVal])                      # retrun all key values from known maxVal

"""
['this', 'is']
['this', 'is']
"""


