# https://www.geeksforgeeks.org/python-find-the-common-keys-from-two-dictionaries/?ref=rp

"""
Time Complexity: O(M x N)
Space Complexity: O(1)
"""
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
for key in a:
    if key in b:
        print(key, end=" ")

"""
The time complexity of this program is O(n * log(n)), where n is the total number of items in both dictionaries. 
This is because the items() method returns a set-like object containing a view of the dictionary’s items, 
and the & operator performs a set intersection operation, both of which have a time complexity of O(n * log(n)). 
The sorted() function also has a time complexity of O(n * log(n)).
"""
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
res = a.items() & b.items()
 
for i in sorted(res):
    print(i[0], end=" ")

"""
Time complexity: O(nlogn), where n is the total number of items in both dictionaries. 
Auxiliary space: O(n)
"""
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
common_keys = set(a).intersection(b)
for key in sorted(common_keys):
    print(key, end=" ")

"""
Time complexity: O(n), where n is the total number of items in both dictionaries. 
Auxiliary space: O(1)
"""
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
for key in a:
    name = b.get(key, None)
    if name:
        print(key, end= " ")

"""
Time complexity: O(nlogn), where n is the total number of items in both dictionaries. 
Auxiliary space: O(n)
"""
a = {"a": 1, "b": 2, "c": 3, "d": 4}
b = {"c": 3, "d": 4, "e": 5, "f": 6}
 
common_keys = filter(lambda x: x in a, b)
for key in sorted(common_keys):
    print(key, end=" ")