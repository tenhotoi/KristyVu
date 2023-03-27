# https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-itemgetter/

# importing "operator" for implementing itemgetter
from operator import itemgetter
 
# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 
# using sorted and itemgetter to print list sorted by age
print("The list printed sorting by age: ")
print(sorted(list, key=itemgetter('age')))
 
print("\r")
 
# using sorted and itemgetter to print
# list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=itemgetter('age', 'name')))
 
print("\r")
 
# using sorted and itemgetter to print list
# sorted by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=itemgetter('age'), reverse=True))

"""
Output:

The list printed sorting by age: 
[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

The list printed sorting by age and name: 
[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]

The list printed sorting by age in descending order: 
[{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]
Time complexity: O(n log n)
Auxiliary space: O(n)
"""

# Python code demonstrate the working of
# sorted() with lambda
 
# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 
# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))
 
print("\r")
 
# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))
 
print("\r")
 
# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))

"""
Output:

The list printed sorting by age: 
[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

The list printed sorting by age and name: 
[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]

The list printed sorting by age in descending order: 
[{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]
"""

"""
You shouldn't worry about performance unless your code is in a tight inner loop, and is actually a performance problem. Instead, use code that best expresses your intent. Some people like lambdas, some like itemgetter. Sometimes it's just a matter of taste.

itemgetter is more powerful, for example, if you need to get a number of elements at once. For example:

operator.itemgetter(1,3,5)

is the same as:

lambda s: (s[1], s[3], s[5])
"""