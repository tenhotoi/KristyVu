# https://www.geeksforgeeks.org/python-convert-key-value-pair-comma-separated-string-into-dictionary/?ref=rp
# >>>>>>>>>>>>>>>>>> Python3 code to demonstrate
# converting comma separated string
# into dictionary
# Method #1: Using dictionary comprehension
 
# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using dict comprehension
res = dict(item.split("=") for item in ini_string1.split(", "))
 
# Printing resultant string
print("Method #1: Using dictionary comprehension - Resultant dictionary 1: ", str(res))

# >>>>>>>>>>>>>>>>>> Python3 code to demonstrate
# converting comma separated string
# into dictionary
# Method #2: Using Map and lambda 
 
# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using map and lambda
res = dict(map(lambda x: x.split('='), ini_string1.split(', ')))
 
# Printing resultant string
print("Method #2: Using Map and lambda - Resultant dictionary", str(res))

# >>>>>>>>>>>>>>>>>> Python3 code to demonstrate
# converting comma separated string
# into dictionary
# Method #3: Using eval() function
 
# Initialising string
ini_string1 = 'name ="akshat", course ="btech", branch ="computer"'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
# using eval
res = eval('dict('+ini_string1+')')
 
# Printing resultant string
print("Method #3: Using eval() function - Resultant dictionary 2: ", str(res))

# >>>>>>>>>>>>>>>>>> Python3 code to demonstrate
# converting comma separated string
# into dictionary
# Method #4 : Using split() and index() methods
 
# Initialising string
ini_string1 = 'name = akshat, course = btech, branch = computer'
 
# Printing initial string
print("Initial String", ini_string1)
 
# Converting string into dictionary
res = dict()
x = ini_string1.split(",")
for i in x:
    a = i[:i.index("=")]
    b = i[i.index("=")+1:]
    res[str(a)] = str(b)
# Printing resultant string
print("Method #4 : Using split() and index() methods Resultant dictionary 3: ", str(res))

# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
# remove duplicates from a list, while preserving order?
items = [1, 2, 0, 1, 3, 2]
a = list(dict.fromkeys(items))  # Or [*dict.fromkeys(items)] if you prefer
print('result of list of dictionary is: ', a)

# Python code to demonstrate
# to convert dictionary into string
# using json.dumps()
 
import json
 
# initialising dictionary
test1 = { "testname" : "akshat",
          "test2name" : "manjeet",
          "test3name" : "nikhil"}
 
# print original dictionary
print (type(test1))
print ("initial dictionary = ", test1)
 
# convert dictionary into string
# using json.dumps()
result = json.dumps(test1)
 
# printing result as string
print ("\n", type(result))
print ("final string = ", result)