# https://www.geeksforgeeks.org/python-merging-two-dictionaries/

"""
Using the method update() 
By using the method update() in Python, one list can be merged into another. But in this, the second list is merged into the first list and no new list is created. It returns None. 

Example: 
"""

# Python code to merge dict using update() method
# Time complexity: O(1) 
# Auxiliary space: O(1)
def Merge(dict1, dict2):
    return(dict2.update(dict1))
 
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# This returns None
print(Merge(dict1, dict2))
 
# changes made in dict2
print(dict2)

# Python code to merge dict using a single
# expression
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
     
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

# code
# Python code to merge dict using a single 
# expression
# Time complexity: O(1)
# Auxiliary space: O(N)
def Merge(dict1, dict2):
    res = dict1 | dict2
    return res
       
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)
 
# Using for loop and keys() method
# code
# Python code to merge dictionary
def Merge(dict1, dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
     
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

"""
One new approach to merge dictionaries in Python is to use the built-in ChainMap class from the collections module. This class allows you to create a single view of multiple dictionaries, and any updates or changes made to the ChainMap will be reflected in the underlying dictionaries.

Here’s an example of how to use ChainMap to merge two dictionaries:
"""

from collections import ChainMap
 
# create the dictionaries to be merged
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
 
# create a ChainMap with the dictionaries as elements
merged_dict = ChainMap(dict1, dict2)
 
# access and modify elements in the merged dictionary
print(merged_dict['a'])  # prints 1
print(merged_dict['c'])  # prints 3
merged_dict['c'] = 5  # updates value in dict2
print(merged_dict['c'])  # prints 5
 
# add a new key-value pair to the merged dictionary
merged_dict['e'] = 6  # updates dict1
print(merged_dict['e'])  # prints 6


# Time Complexity: O(N)
# Auxiliary Space: O(N)
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict
 
# Driver code
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
 
print(merge_dictionaries(dict1, dict2))

# method to merge two dictionaries using the dict() constructor with the union operator (|)
# Time complexity: O(n)
# Auxiliary Space: O(n)
def Merge(dict1, dict2):
    # create a new dictionary by merging the items of the two dictionaries using the union operator (|)
    merged_dict = dict(dict1.items() | dict2.items())
    # return the merged dictionary
    return merged_dict
 
# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
# merge the two dictionaries using the Merge() function
merged_dict = Merge(dict1, dict2)
 
# print the merged dictionary
print(merged_dict)



