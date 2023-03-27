# https://www.geeksforgeeks.org/python-conditional-string-append/?ref=rp

# Python3 code to demonstrate
# Conditional String Append
# using loop
 
def append_str(item, boy_str, girl_str):
    if len(item) > 4 and item[-5] == ' ':
        return item + girl_str
    return item + boy_str
     
# initializing list
test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
 
# initializing append string
boy_str = " Boy"
girl_str = " Girl"
 
# printing original list
print ("The original list is : " + str(test_list))
 
# Conditional String Append
# using loop
res = [append_str(item, boy_str, girl_str) for item in test_list]
 
# printing result
print ("The filtered strings are : " + str(res))

"""
Output
The original list is : ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
The filtered strings are : ['Manjeet Singh Boy', 'Harsimran Kaur Girl', 'Sarbjeet Kaur Girl']

Time Complexity: O(n)
Auxiliary Space: O(n)

Method #2: Using list comprehension List comprehension is shorthand for the longer method of loops. This solved problem in similar way but in shorter constructs. 
"""

# Python3 code to demonstrate
# Conditional String Append
# using list comprehension
 
# initializing list
test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
 
# initializing append string
boy_str = " Boy"
girl_str = " Girl"
 
# printing original list
print ("The original list is : " + str(test_list))
 
# Conditional String Append
# using list comprehension
res = [ele + girl_str if ele[-5] == ' ' else ele + boy_str for ele in test_list]
 
# printing result
print ("The filtered strings are : " + str(res))

"""
Output
The original list is : ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
The filtered strings are : ['Manjeet Singh Boy', 'Harsimran Kaur Girl', 'Sarbjeet Kaur Girl']
Time Complexity: O(n)

Auxiliary Space: O(n)

Method #3: Using map function Map function is used to create a new list by updating the existing list. We solve this problem by defining the condition append function for the map function which will apply to all the elements of the list.
"""

# # Python3 code to demonstrate
# Reverse Row sort in Lists of List
# using map
 
# Initializing append string
boy_str = " Boy"
girl_str = " Girl"
#  Function to append the string
 
 
def func(x):
    if x[-5] == ' ':
        return x + girl_str
    else:
        return x + boy_str
 
 
# initializing list
test_list = ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
 
 
# printing original list
print("The original list is : " + str(test_list))
 
# Conditinal string append using map
res = list(map(func, test_list))
 
# printing result
print("The filtered string are : " + str(res))

"""
Output
The original list is : ['Manjeet Singh', 'Harsimran Kaur', 'Sarbjeet Kaur']
The filtered string are : ['Manjeet Singh Boy', 'Harsimran Kaur Girl', 'Sarbjeet Kaur Girl']

Time Complexity: O(n)
Auxiliary Space: O(n)
"""

