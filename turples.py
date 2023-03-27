"""
Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.
Example:
"""
words = ("spam", "eggs", "sausages")
# You can access the values in the tuple with their index, just as you did with lists:
print(words[0])
# Trying to reassign a value in a tuple causes an error.
# words[1] = "cheese"

"""
Like lists and dictionaries, tuples can be nested within each other.
Tuples can be created without the parentheses by just separating the values with commas.
Example:
"""
my_tuple = "one", "two", "three" 
print(my_tuple[0])

"""
Tuples are faster than lists, but they cannot be changed.
Problem:
You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the 
contact.
Complete the program to get a string as input, search for the name in the list of contacts and output the 
age of the contact in the format presented below:
Sample Input
John
Sample Output
John is 31
If the contact is not found, the program should output "Not Found".
"""
contacts = [
('James', 42),
('Amy', 24),
('John', 31),
('Amanda', 63),
('Bob', 18)
]
name = input("Please enter the name: ")
for x in contacts:
    if name in x:
        print(str(x[0])+" is "+str(x[1]))
        break
    else:
        print("Not Found")

# Tuple unpacking allows you to assign each item in a collection to a variable.
# Example:
numbers = (1, 2, 3) 
a, b, c = numbers
print(a) 
print(b) 
print(c)

"""
This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the 
tuple (b, a) which is then unpacked.
A variable that is prefaced with an asterisk (*) takes all values from the collection that are left over from the 
other variables.
Example:
"""
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
print(a) 
print(b) 
print(c) 
print(d)

"""
Problem
Tuples can be used to output multiple values from a function.
You need to make a function called calc(), that will take the side length of a square as its argument and 
return the perimeter and area using a tuple.
The perimeter is the sum of all sides, while the area is the square of the side length.
Sample Input
3
Sample Output
Perimeter: 12
Area: 9
The given code takes a number from user input, passes it to the calc() function, and uses unpacking to get 
the returned values.
"""
def calc(x):
    return(x*4,x*x)

try:
    side = int(input("Please enter the side length of a square:"))
except:
    print("Invalid value entered.")
else:
    p, a = calc(side)
    print("Perimeter: " + str(p))
    print("Area: " + str(a))

# Python3 code to demonstrate working of
# Convert tuple mixed list to string list
# using list comprehension + tuple() + str() + generator expression
 
# initialize list
test_list = [('gfg', 1, True), ('is', False), ('best', 2)]
 
# printing original list
print("The original list : " + str(test_list))
 
# Convert tuple mixed list to string list
# using list comprehension + tuple() + str() + generator expression
res = [tuple(str(ele) for ele in sub) for sub in test_list]
 
# printing result
print("The tuple list after conversion : " + str(res))

"""
Output : 
The original list : [('gfg', 1, True), ('is', False), ('best', 2)]
The tuple list after conversion : [('gfg', '1', 'True'), ('is', 'False'), ('best', '2')]

Time Complexity: O(n)
Auxiliary Space: O(n)

https://www.geeksforgeeks.org/python-convert-mixed-data-types-tuple-list-to-string-list/?ref=rp
"""

# https://realpython.com/python-sort/

from collections import namedtuple

Runner = namedtuple('Runner', 'bibnumber duration')

runners = []
runners.append(Runner('2528567', 1500))
runners.append(Runner('7575234', 1420))
runners.append(Runner('2666234', 1600))
runners.append(Runner('2425234', 1490))
runners.append(Runner('1235234', 1620))
# Thousands and Thousands of entries later...
runners.append(Runner('2526674', 1906))

print(runners)
print(runners_by_duration := sorted(runners, key=lambda x: getattr(x, 'duration')))
print(top_five_runners := runners_by_duration[:5])
print(every_thirtyseventh_runners := runners[::37])
print(runners.sort(key=lambda x: getattr(x, 'duration')))
print(top_five_runners := runners[:5])

# https://docs.python.org/3/library/collections.html#collections.namedtuple