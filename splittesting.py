# https://www.bitdegree.org/learn/python-split
# str.split(separator, maxsplit)
# Python split() only works on string variables. If you encounter problems with split(), it may be because you are trying to call it upon a non-string object. If this happens, you can force Python to treat the variable as a string with str(x).

text = 'The quick brown fox jumps over the lazy dog'
  
# Split the text wherever there's a space.
words = text.split()
print(words)

paragraph = 'The quick brown fox jumps over the lazy dog. The quick brown dog jumps over the lazy fox' 

# Split the text wherever there's a full stop.
a,b = paragraph.split('.')

# Display the results.
print(a)
print(b)

cars= 'Audi and Kia and BMV and Volvo and Opel'

# maxsplit of 1
print(cars.split(' and ',1))
# maxsplit of 2
print(cars.split(' and ',2)) 
# maxsplit of 1
print(cars.split(' and ',3))
# maxsplit of 1
print(cars.split(' and ',4))


# https://www.tutorialspoint.com/How-to-correctly-sort-a-string-with-a-number-inside-in-Python

"""
This type of sort in which you want to sort on the basis of numbers within string is called natural sort or human sort. For example, if you have the text:

['Hello1','Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
 Then you want the sorted list to be:

['Hello1', 'Hello2','Hello12', 'Hello17', 'Hello25', 'Hello29']
 and not:

['Hello1','Hello12', 'Hello17', 'Hello2', 'Hello25', 'Hello29']
 To do this we can use the extra parameter that sort() uses. This is a function that is called to calculate the key from the entry in the list. We use regex to extract the number from the string and sort on both text and number. 
"""

import re
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)',text) ]
my_list =['Hello1', 'Hello12', 'Hello29', 'Hello2', 'Hello17', 'Hello25']
my_list.sort(key=natural_keys)
print(my_list)

"""
This will give you the output:

['Hello1','Hello2', 'Hello12', 'Hello17', 'Hello25', 'Hello29']
"""
