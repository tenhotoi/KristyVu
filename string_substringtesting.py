# https://stackoverflow.com/questions/13779526/finding-a-substring-within-a-list-in-python
# 

mylist = ['abc123', 'def456', 'ghi789']
sub = 'abc'
print("\n".join(s for s in mylist if sub in s))

port_mappings = [
"__10.1.1.1|10.2.2.2__",
"portA:member1_port3",
"portB:member2_port27",
"portC:member1_port14",
"__10.3.3.3__",
"portA:port4",
"portB:port15"
"__10.3.3.4__",
"portA:port40",
"portB:port150"
]
sub = 'port4'
print("\n".join(s for s in port_mappings if sub in s))
dup = [s for s in port_mappings if sub in s and s.endswith(sub)]
if len(dup) > 1:
    print('WARNING: Duplicated ports found!')
    print(dup)

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

import re
s = ['hello1', 'hello9', 'hello99', 'hello12', 'hello22']
def toi(c):
    return int(c) if c.isdigit() else c
def key_natural(word):
    return [toi(c) for c in re.split('(\d+)', word)]
print(s_sorted := sorted(s, key=key_natural))


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
print(sort_s := sorted(s, key= function))                                 # key doesn't alter original values

"""
Output:
['hello1', 'hello9', 'hello12', 'hello22', 'hello99']
['hello1', 'hello9', 'hello12', 'hello22', 'hello99']
"""