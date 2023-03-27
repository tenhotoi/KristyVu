# https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-dictionary-value-list/

"""
Method #1 : Using loop <<<<<<<<<<<<<<<<<<<<<<
Time Complexity: O(n*n), where n is the elements of dictionary
Auxiliary Space: O(n), where n is the size of dictionary
"""

# Python3 code to demonstrate working of
# Convert list of dictionaries to Dictionary Value list
# Using loop
from collections import defaultdict
 
# initializing lists
test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},
             {"Gfg" : 8, "is" : 11, "best" : 19},
             {"Gfg" : 2, "is" : 16, "best" : 10},
             {"Gfg" : 12, "is" : 1, "best" : 8},
             {"Gfg" : 22, "is" : 6, "best" : 8}]
 
# printing original list
print("The original list : " + str(test_list))
 
# using loop to get dictionaries
# defaultdict used to make default empty list
# for each key
res = defaultdict(list)
print('Default dictionary is: ', res)
for sub in test_list:
    for key in sub:
        print('key is: ', key, ' and sub[key] is: ', sub[key])
        res[key].append(sub[key])
     
# printing result
print("The extracted dictionary : " + str(dict(res)))

"""
Method #2 : Using list comprehension + dictionary comprehension
Time Complexity: O(n)
Auxiliary Space: O(n)
"""
# Python3 code to demonstrate working of
# Convert list of dictionaries to Dictionary Value list
# Using list comprehension + dictionary comprehension
from collections import defaultdict
 
# initializing lists
test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},
             {"Gfg" : 8, "is" : 11, "best" : 19},
             {"Gfg" : 2, "is" : 16, "best" : 10},
             {"Gfg" : 12, "is" : 1, "best" : 8},
             {"Gfg" : 22, "is" : 6, "best" : 8}]
 
# printing original list
print("The original list : " + str(test_list))
 
# dictionary and list comprehension
# for shorthand to solution of problem
res = defaultdict(list)
print('Default dictionary is: ', res)
# {res[key].append(sub[key]) for sub in test_list for key in sub}
{print(sub, key) for sub in test_list for key in sub}
     
# printing result
print("The extracted dictionary : ", dict(res))