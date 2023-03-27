# https://builtin.com/software-engineering-perspectives/convert-list-to-dictionary-python

# 10 DIFFERENT WAYS TO CONVERT A PYTHON LIST TO A DICTIONARY
# 1. Converting a list of tuples to a dictionary.
# Converting list of tuples to dictionary by using dict() constructor
color=[('red',1),('blue',2),('green',3)]
d=dict(color)
print (d)#Output:{'red': 1, 'blue': 2, 'green': 3}

# 2. Converting two lists of the same length to a dictionary.
l1=[1,2,3,4]
l2=['a','b','c','d']
d1=zip(l1,l2)
print (d1)#Output:<zip object at 0x01149528>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 3. Converting two lists of different length to a dictionary.
l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d']
d1=zip(l1,l2)
print (d1)#Output:<zip object at 0x01149528>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

from itertools import zip_longest
l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d']
d1=zip_longest(l1,l2)
print (d1)#Output:<itertools.zip_longest object at 0x00993C08>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: None, 6: None, 7: None}

from itertools import zip_longest
l1=[1,2,3,4,5,6,7]
l2=['a','b','c','d']
d1=zip_longest(l1,l2,fillvalue='x')
print (d1)#Output:<itertools.zip_longest object at 0x00993C08>
#Converting zip object to dict using dict() contructor.
print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'x', 6: 'x', 7: 'x'}

# 4. Converting a list of alternative key, value items to a dictionary.
l1=[1,'a',2,'b',3,'c',4,'d']
#Creating list containing keys alone by slicing
l2=l1[::2]
#Creating list containing values alone by slicing
l3=l1[1::2]
#merging two lists uisng zip()
z=zip(l2,l3)
#Converting zip object to dict using dict() constructor.
print (dict(z))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 5. Converting a list of dictionaries to a single dictionary.
l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
d1={}
for i in l1:
    d1.update(i)

print (d1)
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
d1={k:v for e in l1 for (k,v) in e.items()}
print (d1)
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 6. Converting a list into a dictionary using enumerate().
l1=['a','b','c','d']
d1=dict(enumerate(l1))
print (d1)#Output:{0: 'a', 1: 'b', 2: 'c', 3: 'd'}

# 7. Converting a list into a dictionary using dictionary comprehension.
l1=[1,2,3,4]
d1={k:"a" for k in l1}
print (d1)
#Output:{1: 'a', 2: 'a', 3: 'a', 4: 'a'}

# 8. Converting a list to a dictionary using dict.fromkeys().
l1=['red','blue','orange']
d1=dict.fromkeys(l1,"colors")
print (d1)
#Output:{'red': 'colors', 'blue': 'colors', 'orange': 'colors'}

# 9. Converting a nested list to a dictionary using dictionary comprehension.
l1 = [[1,2],[3,4],[5,[6,7]]]
d1={x[0]:x[1] for x in l1}
print(d1)#Output:{1: 2, 3: 4, 5: [6, 7]}

# 10. Converting a list to a dictionary using Counter().
from collections import Counter
c1=Counter(['c','b','a','b','c','a','b'])
#key are elements and corresponding values are their frequencies
print (c1)#Output:Counter({'b': 3, 'c': 2, 'a': 2})
print (dict(c1))#Output:{'c': 2, 'b': 3, 'a': 2}

i = ['k', 'v']
print(dict({i[0]:i[1]}))

#s1 = "r'Name1='Value=2" + ';Name2=Value2;Name3=Value3;Name4="Va \" + lue; + \n + 3"' 
s = "r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4=" + r'"Va\"lue;\n3' + "\"\'"
# print(s)
# s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
# note: a semicolon inside a quoted string, a quote is escaped using a backslash, \n escape is used, both single and double quotes are used)

# res = dict(item.split("=", 1) for item in s.split(";") if len(item.split("=", 1)) == 2)
# ressub = dict([item, None] for item in s.split(";") if len(item.split("=", 1)) == 1)
res = dict(item.split("=", 1) if len(item.split("=", 1)) == 2 else [item, None] for item in s.split(";"))
# print(type(ressub))
# print(ressub)
# print(type(res))
# print(res)
# res.update(ressub)
print(type(res))
print(res)

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/