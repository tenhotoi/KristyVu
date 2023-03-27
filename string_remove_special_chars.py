# https://datagy.io/python-remove-special-characters-from-string/

# Remove Special Characters from a String Using .isalnum()

text = 'datagy -- is. great!'
new_text = ''

for character in text:
    if character.isalnum():
        new_text += character

print(new_text)

# Returns: datagyisgreat

# Remove Special Characters from a String Using re.sub()
import re

text = 'datagy -- is. great!'
new_text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

print(new_text)

# Returns: datagy  is great

new_text = re.sub(r"[^a-zA-Z0-9 ]", "?", text)
print(new_text)
# datagy ?? is? great?

# Remove Special Characters from a String Using re.sub()
import re

text = 'datagy -- is. great!'
new_text = ''.join(filter(str.isalnum, text))

print(new_text)

# Returns: datagyisgreat

new_text = ''.join(filter(lambda x: x.isalnum(), text))
print(new_text)
# datagyisgreat

# Remove Special Characters from a String Using filter()
import re

def remove_special_characters(character):
    if character.isalnum() or character == ' ':
        return True
    else:
        return False

text = 'datagy -- is. great!'
new_text = ''.join(filter(remove_special_characters, text))

print(new_text)

# Returns: datagy  is great

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


def function(x):
    print([int(c) if c.isdigit() else c for c in re.split('(\d+)', x)])  # <========== note: () wrapping around \d+ here
    """
    ['hello', 1, '']
    ['hello', 9, '']
    ['hello', 99, '']
    ['hello', 12, '']
    ['hello', 22, '']
    """
    return [int(c) if c.isdigit() else c for c in re.split('(\d+)', x)]
print(sort_s := sorted(my_list, key= function))                                 # key doesn't alter original values

"""
Output:

['hello1', 'hello9', 'hello12', 'hello22', 'hello99']
"""


# Remove Special Characters from a String Using re.sub()
import re

text = 'datagy -- is. great!'
new_text = re.sub(r"[^a-zA-Z0-9 ]", "", text)

print(new_text)

# Returns: datagy  is great

new_text = re.sub(r"[^a-zA-Z0-9 ]", "?", text)
print(new_text)
# datagy ?? is? great?


print(re.sub(r'[^a-zA-Z0-9]', '', 'hello----28837'))
# hello28837
print(re.sub('[^a-zA-Z0-9]', '', 'hello----28837'))
# hello28837
print(re.sub(r'[a-zA-Z0-9]', '', 'hello----28837'))
# ----
print(re.sub(r'[a-zA-Z0-9]', '?', 'hello----28837'))
# ?????----?????
print(re.sub(r'[a-zA-Z0-9]', '?', 'hello----28837', 4))
# ????o----28837
print(re.sub('[a-zA-Z0-9]', '?', 'hello----28837', 4))
# ????o----28837
print(re.sub('[^A-Z0-9]', '', 'hello----28837'))
# 28837
print(re.sub('^[A-Z0-9]', '', 'hello----28837'))
# hello----28837
print(re.sub('^[a-zA-Z0-9]', '', 'hello----28837'))
# ello----28837
print(re.sub('^[a-zA-Z0-9]', '?', 'hello----28837'))
# ?ello----28837

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
