
# Dictionaries
"""
Only immutable objects can be used as keys to dictionaries. Immutable objects are those that can't be 
changed.  This means that you can use strings, integers, booleans, and any other immutable type as dictionary keys
"""
ages = { 
"Dave": 24, 
"Mary": 42, 
"John": 58 
} 
print(ages["Dave"]) 
print(ages["Mary"])

# take the key as input and output the corresponding value
car = {
'brand':'BMW',
'year': 2018,
'color': 'red',
'mileage': 15000
}

print('Please enter which dictionary key: ')
k=input()
if k in car:
    print("The value of ", k, "is: ", car.get(k))
else:
    print("Can't find the dictionary key ", k, "you're looking for.")

# To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums = { 
1: "one", 
2: "two", 
3: "three", 
} 
print(1 in nums) 
print("three" in nums) 
print(4 not in nums)

# A useful dictionary function is get. It does the same thing as indexing, 
# but if the key is not found in the dictionary it returns another specified value instead.
# Example:
pairs = { 
1: "apple", 
"orange": [2, 3, 4], 
True: False, 
12: "True", 
} 
print(pairs.get("orange")) 
print(pairs.get(7, 42)) 
print(pairs.get(12345, "not found"))
print(pairs.get(1)) 
print(pairs)
print(len(pairs)) 

data = {
'Singapore': 1,
'Ireland': 6,
'United Kingdom': 7,
'Germany': 27,
'Armenia': 34,
'United States': 17,
'Canada': 9,
'Italy': 74
}

while True:
    print("Please enter country name with first letter being capitalized.  Enter quit to exit.")
    a=input()
    
    if a == 'quit':
        break
    else:
        print(data.get(a,"Not found"))

# https://www.geeksforgeeks.org/python-convert-key-value-pair-comma-separated-string-into-dictionary/?ref=rp
# Python3 code to demonstrate
# converting comma separated string
# into dictionary
 
# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using dict comprehension
res = dict(item.split("=") for item in ini_string1.split(", "))
 
# Printing resultant string
print("Resultant dictionary", str(res))

# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
# remove duplicates from a list, while preserving order?
items = [1, 2, 0, 1, 3, 2]
a = list(dict.fromkeys(items))  # Or [*dict.fromkeys(items)] if you prefer
print('result of list of dictionary is: ', a)

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

my_function(name='John', age=30, city='New York')

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
             {'love': 3}]
 
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
res = list(filter(lambda sub: key in list(sub.keys()), test_list))
 
# printing result
print("The filtered Dictionaries : " + str(res))

# Initializing list of dictionaries
test_list = [{'gfg': 2, 'is': 8, 'good': 3},
             {'gfg': 1, 'for': 10, 'geeks': 9},
             {'love': 3}]
 
# Printing original list
print("The original list is: ", test_list)
 
# Initializing key
key = 'gfg'
 
# Using for loop to extract dictionaries with given key
result = []
for sub_dict in test_list:
    if key in sub_dict:
        result.append(sub_dict)
 
# Printing result
print("The filtered dictionaries: ", result)
#This code is contributed by Vinay Pinjala.


# Let's add key:value to a dictionary, the functional way
 
# Create your dictionary class
class my_dictionary(dict):
 
    # __init__ function
    def __init__(self):
        self = dict()
         
    # Function to add key:value
    def add(self, key, value):
        self[key] = value
 
# Main Function
dict_obj = my_dictionary()
 
# Taking input key = 1, value = Geek
dict_obj.key = input("Enter the key: ")
dict_obj.value = input("Enter the value: ")
 
dict_obj.add(dict_obj.key, dict_obj.value)
dict_obj.add(2, 'forGeeks')
 
print(dict_obj)

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

