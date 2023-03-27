# https://learnpython.com/blog/create-dictionary-in-python/
# 5 Ways to Create a Dictionary in Python

# 1. METHOD 1:
grades = {'John': 7.5, 'Mary': 8.9, 'James': 9.0}

# 2. METHOD 2:
prices = dict(apple=2.5, orange=3.0, peach=4.4)
print(prices)
""" 
# output: {'apple': 2.5, 'orange': 3.0, 'peach': 4.4}

It’s fair to say the first method is easier to read and understand at a glance. However, keyword arguments are always interpreted as strings, and using keyword arguments may not be an option if you need a dictionary in which the keys are not strings. Take a look at this example to see what I mean:
"""
# this works
values = [(1, 'one'), (2, 'two')]
# values = (1='one', 2='two')         # !!! WARNING: this would NOT work: SyntaxError: cannot assign to literal here. 
# values = {1:'one', 2:'two'}         # Hmmm....  Somehow this works too:

print(prices := dict(values))                   # {1: 'one', 2: 'two'}
print([type(k) for k in prices.keys()])         # [<class 'int'>, <class 'int'>]
print([type(v) for v in prices.values()])       # [<class 'str'>, <class 'str'>]
"""
Output:
{1: 'one', 2: 'two'}
[<class 'int'>, <class 'int'>]
[<class 'str'>, <class 'str'>]
""" 
# SyntaxError - a number is not a valid keyword argument!
# prices = dict(1='one', 2='two')

# 3. METHOD 3:
import json
 
with open('mydata.json', 'r') as json_file:
    person = json.load(json_file)
print(person)

# 4. METHOD 4:
# Here’s an example of the dictionary union operator in action:

jobs_1 = {
    'John': 'Engineer',
    'James': 'Physician',
}
 
jobs_2 = {
    'Jack': 'Journalist',
    'Jill': 'Lawyer',
}
 
jobs = jobs_1 | jobs_2
print(jobs)
 
# output: {'John': 'Engineer', 'James': 'Physician', 'Jack': 'Journalist', 'Jill': 'Lawyer'}

# It’s important to note that, if there are duplicate keys in the source dictionaries, the resulting dictionary gets the value from the right-most source dictionary. This is a consequence of Python not allowing duplicate keys in a dictionary. Take a look at what happens here:

d1 = {
    'A': 1,
    'B': 2,
}
 
d2 = {
    'B': 100,
    'C': 3,
}
 
result = d1 | d2
print(result)
# output: {'A': 1, 'B': 100, 'C': 3}

# 5. METHOD 5:
animals = ['cat', 'lion', 'monkey']
animal_dict = {animal: len(animal) for animal in animals}
print(animal_dict)
# output: {'cat': 3, 'lion': 4, 'monkey': 6}

"""
See how it works? For each animal in the list animals, we build a key-value pair of the animal itself and its length (len(animal)).

Here’s a more intricate example. We use a dict comprehension to filter the values from a preexisting dictionary. See if you can figure out what the code below does:
"""
ages = {
    'Bill': 23,
    'Steve': 34,
    'Maria': 21,
}
filtered_ages = {name: age for name, age in ages.items() if age < 30}
print(filtered_ages)
# output: {'Bill': 23, 'Maria': 21}

filtered_names = {age: name for name, age in ages.items() if name is not 'Bill'}
print(filtered_names)


