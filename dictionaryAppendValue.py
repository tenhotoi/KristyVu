# https://www.geeksforgeeks.org/python-append-multitype-values-in-dictionary/?ref=rp
# Python3 code to demonstrate working of 
# Append Multitype Values in Dictionary
# Using isinstance() + update() + extend()
  
# helper_fnc
def update_dictionary(key, val, test_dict):
      
    if key not in test_dict:
        test_dict[key] = val
      
    elif type(val) not in [str, list, dict]:
        raise ValueError("Invalid Data Type")
      
    elif isinstance(val, list):
        test_dict[key].extend(val)
      
    elif isinstance(val, dict):
        test_dict[key].update(val)
      
    else:
        test_dict[key] = test_dict[key] + val
      
    return test_dict
  
# initializing dictionary
test_dict = {'gfg' : "geekfor", 'is' : {'a' : 5, 'b' : 6}, 'best' : [1, 2, 3]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# initializing dict, string and append
up_dict = {'c' : 7}
up_str = 'geeks'
up_list = [4, 5]
  
# Append Multitype Values in Dictionary
# Using isinstance() + update() + extend()
res = update_dictionary('gfg', up_str, test_dict)
res = update_dictionary('is', up_dict, res)
res = update_dictionary('best', up_list, res)
  
# printing result 
print("The update dictionary : " + str(res)) 

# https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
# Add a key:value pair to dictionary in Python
# Python program to add a key:value pair to dictionary

# Code #1: Using Subscript notation This method will create a new key:value pair on a dictionary by assigning a value to that key. 
# Time Complexity: O(1)
# Auxiliary Space: O(1)
test_dict = {'key1':'geeks', 'key2':'for'}
print("Current Dict is: ", test_dict)
   
# using the subscript notation
# Dictionary_Name[New_Key_Name] = New_Key_Value
 
test_dict['key3'] = 'Geeks'
test_dict['key4'] = 'is'
test_dict['key5'] = 'portal'
test_dict['key6'] = 'Computer'
print("Updated Dict is: ", test_dict)

# Code #2: Using update() method 
# Time Complexity: O(1)
# Auxiliary Space: O(1)
test_dict = {'key1':'geeks', 'key2':'for'}
print("Current Dict is: ", test_dict)
 
# adding dict1 (key3, key4 and key5) to dict
dict1 = {'key3':'geeks', 'key4':'is', 'key5':'fabulous'}
test_dict.update(dict1)
 
# by assigning
test_dict.update(newkey1 ='portal')
print(test_dict)

# Code #4: Using a dictionary comprehension 
# For example, you can create a new dictionary that adds a key:value pair to an existing dictionary like this:
# Time Complexity: O(n)
# Auxiliary Space: O(n)
existing_dict = {'key1': 'value1', 'key2': 'value2'}
new_key = 'key3'
new_value = 'value3'
 
updated_dict = {**existing_dict, new_key: new_value}
print(updated_dict)
#This code is contributed by Edula Vinay Kumar Reddy

# Code #3: Taking Key:value as input 
# Let's add key:value to a dictionary, the functional way
# Time Complexity: O(1)
# Auxiliary Space: O(n)
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

# >>>>>>>>>>>>>>> KRISTY TESTING <<<<<<<<<<<<<
# initializing dictionary
test_dict = {'gfg' : "geekfor", 'is' : {'a' : 5, 'b' : 6}, 'best' : [1, 2, 3]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# initializing dict, string and append
up_dict = {'c' : 7}
up_str = 'geeks'
up_list = [4, 5]

res = update_dictionary('gfg', up_str, test_dict)
res = update_dictionary('is', up_dict, res)
res = update_dictionary('best', up_list, res)

test_dict.update({'gfg':up_str})
print("The dictionary after updating test_dict with up_dict is : " + str(test_dict))
test_dict.update({'is':up_dict})
print("The dictionary after updating test_dict with up_dict is : " + str(test_dict))
test_dict.update({'best':up_list})
print("The dictionary after updating test_dict with up_dict is : " + str(test_dict))
