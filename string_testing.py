# Split string with multiple delimiters in Python

import re

# s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
string_to_split = "r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4=" + r'"Va\"lue;\n3' + "\"\'"
for each in re.split('; |, ', string_to_split):
    print(each)
for each in re.split('; |, |\*|\n',string_to_split):
    print(each)
for item in string_to_split.split(";"):
    print(item.split("=", 1))


a = 'Beautiful, is; better*than\nugly'
for each in re.split('; |, |\*|\n',a):
    print(each)

#s1 = "r'Name1='Value=2" + ';Name2=Value2;Name3=Value3;Name4="Va \" + lue; + \n + 3"' 
s = "r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4=" + r'"Va\"lue;\n3' + "\"\'"
print(s)
# s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
# note: a semicolon inside a quoted string, a quote is escaped using a backslash, \n escape is used, both single and double quotes are used)

# res = dict(item.split("=", 1) for item in s.split(";") if len(item.split("=", 1)) == 2)
# ressub = dict([item, None] for item in s.split(";") if len(item.split("=", 1)) == 1)
res = dict(item.split("=", 1) if len(item.split("=", 1)) == 2 else [item, None] for item in s.split(";"))
"""
Output:
Beautiful
is
better
than
ugly
r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
<class 'dict'>
{"r'Name1": "'Value=2'", 'Name2': 'Value2', 'Name3': 'Value3', 'Name4': '"Va\\"lue', '\\n3"\'': None}
"""
# print(type(ressub))
# print(ressub)
# print(type(res))
# print(res)
# res.update(ressub)
print(type(res))
print(res)

fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
print(isApple)

i = ['k', 'v']
print(dict({i[0]:i[1]}))

"""
A variable is just something that refers/points to some data you have.

x = 5
Here x is a variable. Variables can point to more kinds of data than just numbers, though. They can point to strings, functions, etc.

A parameter is something that is passed into a function

def my_function(y):
print(y)
Here y is a parameter. It doesn't contain a value yet. But if I want to call the function, I need to provide an argument to the function.

An argument is the actual value you provide to the function that replaces the parameter.
"""

s='3cheers2allthere'
print(s.title())

# Lists
x = ['hi', 'hello', 'welcome'] 
print(x[2])

a = '123456789'
for i in range(len(a) - 1):
    print(a := a[:-1])
    print(a[-1])

"""
Output:
12345678
8
1234567
7
123456
6
12345
5
1234
4
123
3
12
2
1
1
"""

a = 'abcd'
print([i for i in a])

b = 'e', 'f', 'g'
print([i for i in b])

"""
Output:
['a', 'b', 'c', 'd']
['e', 'f', 'g']
"""
cmb = ['']
for each in a:
    print(each, 'testing: ', cmb := [i+j for i in cmb for j in a])

print("string" in "dfkjdkfjdstringdkfjkdjfkd")

import re

print(re.search("^string", "stringdfkjdkfjdstringdkfjkdjfkd"))
# Output: <re.Match object; span=(0, 6), match='string'>

print(re.search("^string", "dfkjdkfjdstringdkfjkdjfkd"))
#OUtput: None
print(re.search("^string", "kdkdkdkfjkdjfkd"))
# Output: None

print(re.search("\Astring", "stringdfkjdkfjdstringdkfjkdjfkd"))
# Output: <re.Match object; span=(0, 6), match='string'>

print(re.search("\Astring", "dfkjdkfjdstringdkfjkdjfkd"))
#OUtput: None
print(re.search("\Astring", "kdkdkdkfjkdjfkd"))
# Output: None

# https://www.geeksforgeeks.org/python-raw-strings/

# Python program to use raw strings
 
# Define string and assign to variable
s = '\n dkfjdkfjskdfj'
 
# Return object orientation in string format
# and truncating quotes
print(repr(s))
raw_string = repr(s)[1:-1]   # this is because of repr(), which will print the text with single quotes
print(s1 := r'\n dkfjdkfjskdfj')
print(s1 := r"\n dkfjdkfjskdfj")
# print(s1 := r''\n dkfjdkfjskdfj'')
"""
line 149              
SyntaxError: unexpected character after line continuation character
"""
# print(s1 := r""\n dkfjdkfjskdfj""")
"""
line 155
SyntaxError: unexpected character after line continuation character
"""
               
print(s1 := r'''\n dkfjdkfjskdfj''')
print(s1 := r"""\n dkfjdkfjskdfj""")
"""
\n dkfjdkfjskdfj
\n dkfjdkfjskdfj
"""

# Print the new string created
print(raw_string)
 
# Print the original string
print(s)
 
# Print the new string created
print(raw_string)

# s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
# note: a semicolon inside a quoted string, a quote is escaped using a backslash, \n escape is used, both single and double quotes are used)
s = r'''Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'''
print(s)
print(res := dict(item.split("=", 1) if len(item.split("=", 1)) == 2 else [item, None] for item in s.split(";")))

# from collections import defaultdict
# res = defaultdict()  # defaultdict doesn't help with the issue of ValueError: dictionary update sequence element #4 has length 1; 2 is required
# print(res := dict(item.split("=", 1) for item in s.split(";")))
"""
Output:
Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"
{'Name1': "'Value=2'", 'Name2': 'Value2', 'Name3': 'Value3', 'Name4': '"Va\\"lue', '\\n3"': None}

Note: made posible due to triple quotes around the raw string!!!
https://www.codevscolor.com/python-raw-string
"""


a = [1, 2, 3, 4, 5]
print(a[1:-1])

"""
'\n dkfjdkfjskdfj'
\n dkfjdkfjskdfj
\n dkfjdkfjskdfj

 dkfjdkfjskdfj
\n dkfjdkfjskdfj
[2, 3, 4]
"""
print(r"'")

# Python3 program introducing f-string
val = 'Geeks'
print(f"{val}for{val} is a portal for {val}.")
 
name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.")

import re

teststr = 'kristy1978'
print(re.split('\d+', teststr))    # ['kristy', '']
print(re.split('(\d+)', teststr))  # ['kristy', '1978', '']

teststr = 'kristy:1978:stockton'
print(teststr.split(':'))           # ['kristy', '1978', 'stockton']
print(teststr.split('(:)'))         # ['kristy:1978:stockton']
print(teststr.split(':', 1))        # ['kristy', '1978:stockton']
print(tmp := teststr.split(':', 2))        # ['kristy', '1978', 'stockton']
print(':'.join(tmp[:2]))            # kristy:1978

print(type(eval(str(('a', 1)))))
print(type(eval(str(['a', 1]))))

a = 'Beautiful, is; better*than\nugly'
print(' '.join(re.split('; |, |\*|\n',a)))   # remove all of following from a: '; , \* \n

"""
<class 'tuple'>
<class 'list'>
Beautiful is better than ugly
"""

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
from collections import Counter
def count_x_o(s1, s2):
    counter_1 = Counter(s1)
    counter_2 = Counter(s2)
    print(counter_1)
    print(counter_2)
    if (counter_1["x"] == counter_2['x']) or (counter_1["o"] == counter_2['o']):
        return True
    else:
        return False
    
print(count_x_o('dfjdkxjxo', 'dfkjxdfjkxkdjfo'))
print(count_x_o('dfkjk', 'dfkjkdj'))
print(count_x_o('dfkjjko', 'dkfjkx'))

def function(int1, func, int2):
    # if func == '*':
    if func in '+-/*':
        return eval(str(int1) + func + str(int2)) 
    else:
        return 'Invalid function.'
    
print(function(6, '*' ,4))
print(eval('6 * 4'))
"""
24
24
"""

from collections import Counter

arr = 'abcd'
print(sol := ''.join([c*2 for c in arr]))

s = 'dfjdk sfiweriwe dfjdk so wrekjwrk so kwerjwk so'
print(count := sum(map(lambda x: x == 's', s)))
# 4
print(list(map(lambda x: x == 'so', s.split())))
# [False, False, False, True, False, True, False, True]
print(s.split())
# ['dfjdk', 'sfiweriwe', 'dfjdk', 'so', 'wrekjwrk', 'so', 'kwerjwk', 'so']
print(sum(list(map(lambda x: x == 'so', s.split()))))
# 3
print(Counter(filter(lambda x: x == 'so', s.split())))
# Counter({'so': 3})

# # https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/
# initializing list
test_list = [ '4', '6', '7', '2', '1']
from itertools import combinations
print(list(combinations([int(x) for x in test_list], 3)))
# [(4, 6, 7), (4, 6, 2), (4, 6, 1), (4, 7, 2), (4, 7, 1), (4, 2, 1), (6, 7, 2), (6, 7, 1), (6, 2, 1), (7, 2, 1)]
val = 12
print([sol for sol in list(combinations([int(x) for x in test_list], 3)) if sum(sol) == val])
# [(4, 6, 2), (4, 7, 1)]
print(list(filter(lambda x: sum(x)==val, list(combinations([int(x) for x in test_list], 3)))))
# [(4, 6, 2), (4, 7, 1)]

