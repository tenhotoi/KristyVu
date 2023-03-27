# Python program to illustrate
print('>>>>>> enumerate function')
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
  
print('>>>>>> creating enumerate objects')
obj1 = enumerate(l1)
obj2 = enumerate(s1)
  
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
  
print('>>>>>> changing start index to 2 from 0')
print (list(enumerate(s1, 2)))

print('>>>>>> Python program to illustrate enumerate function in loops')
l1 = ["eat", "sleep", "repeat"]
  
print('>>>>>> printing the tuples in object directly')
for ele in enumerate(l1):
    print (ele)
  
print('>>>>>> changing index and printing separately')
for count, ele in enumerate(l1, 100):
    print (count, ele)
  
print('>>>>>> getting desired output from tuple')
for count, ele in enumerate(l1):
    print(count)
    print(ele)

config_file = [
"__10.1.1.1|10.2.2.2__",
"portA:enabled=true",
"portB:vlan=10",
"portC:vlan=200",
"__10.3.3.4__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15",
"__10.3.3.3__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15",
"__Switch1A|Switch1B__",
"portA:enabled=true",
"portA:poe=false",
"portA:speed=100mbps",
"portB:vlan=15"
]

port_mappings = [
"__10.1.1.1|10.2.2.2__",
"portA:member1_port3",
"portB:member2_port27",
"portC:member1_port14",
"__10.3.3.3__",
"portA:port4",
"portB:port15",
"__Switch1A|Switch1B__",
"portA:port4",
"portB:port15"
]
config_headers = [item for i, item in enumerate(config_file) if item.count('__')]
config_headersIndex = [i for i, item in enumerate(config_file) if item.count('__')]
print(config_headers)
print(config_headersIndex)

map_headers = [item for i, item in enumerate(port_mappings) if item.count('__')]
map_headersIndex = [i for i, item in enumerate(port_mappings) if item.count('__')]
print(map_headers)
print(map_headersIndex)

"""
Output:
['__10.1.1.1|10.2.2.2__', '__10.3.3.3__', '__Switch1A|Switch1B__']
[0, 4, 9]
['__10.1.1.1|10.2.2.2__', '__10.3.3.3__', '__Switch1A|Switch1B__']
[0, 4, 7]
"""

initial = [1, 1, 9, 1, 9, 6, 9, 7]
print('Original list is: ', initial)
result = [y for x, y in enumerate(initial)]
print(result)
"""
Output:
[1, 1, 9, 1, 9, 6, 9, 7]
"""

