# https://www.geeksforgeeks.org/python-difference-in-keys-of-two-dictionaries/?ref=rp

# Code #1 : Using set to find keys that are missing. 
# Python code to find the difference in
# keys in two dictionary
 
# Initialising dictionary
dict1= {'key1':'Geeks', 'key2':'For', 'key3':'geeks'}
dict2= {'key1':'Geeks', 'key2:':'Portal'}
 
diff = set(dict2) - set(dict1)
 
# Printing difference in
# keys in two dictionary
print(diff)

# Code #2 : Finding keys in dict2 which are not in dict1. 
# Python code to find difference in keys in two dictionary
 
# Initialising dictionary
dict1= {'key1':'Geeks', 'key2':'For'}
dict2= {'key1':'Geeks', 'key2':'For', 'key3':'geeks',
        'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3': 32 }}
 
for key in dict2.keys():
    if not key in dict1:
 
        # Printing difference in
        # keys in two dictionary
        print(key)

# Code #3: Finding keys in dict1 which are not in dict2. 
# Python code to find difference in keys in two dictionary
 
# Initialising dictionary
dict1= {'key1':'Geeks', 'key12':'For'}
dict2= {'key1':'Geeks', 'key2':'For', 'key3':'geeks',
        'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3': 32 }}
         
for key in dict1.keys():
    if not key in dict2:
 
        # Printing difference in
        # keys in two dictionary
        print(key)

# Code #4 : Finding the same keys in two dictionaries. 
# Python code to find difference in keys in two dictionary
 
# Initialising dictionary
dict1= {'key1':'Geeks', 'key2':'For'}
dict2= {'key1':'Geeks', 'key2':'For', 'key3':'geeks',
        'key4': {'GeekKey1': 12, 'GeekKey2': 22, 'GeekKey3': 32 }}
         
print(set(dict1.keys()).intersection(dict2.keys()))

# Code #5 : Finding the keys that are missing in dict2 compared to dict1 using inbuilt method

# Initializing dictionaries
dict1 = {'key1': 'Geeks', 'key2': 'For', 'key3': 'geeks'}
dict2 = {'key1': 'Geeks', 'key2': 'Portal'}
 
# Finding the keys that are missing in dict2 compared to dict1
diff = set(dict1.keys()).difference(dict2.keys())
 
# Printing the difference in keys
print(diff)