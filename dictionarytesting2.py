
def testingStr():
    #s1 = "r'Name1='Value=2" + ';Name2=Value2;Name3=Value3;Name4="Va \" + lue; + \n + 3"' 

    # s = "r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4=" + r'"Va\"lue;\n3' + "\"\'"  # this one was used before

    # print(s)
    # s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
    # note: a semicolon inside a quoted string, a quote is escaped using a backslash, \n escape is used, both single and double quotes are used)
    
    # res = dict(item.split("=", 1) for item in s.split(";") if len(item.split("=", 1)) == 2)
    # ressub = dict([item, None] for item in s.split(";") if len(item.split("=", 1)) == 1)
    # print(type(ressub))
    # print(ressub)
    s = ''''Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'''
    res = dict(item.split("=", 1) if len(item.split("=", 1)) == 2 else [item, None] for item in s.split(";"))
    print(type(res))
    print(res)
    
    return res

if __name__ == '__main__':
    testingStr()

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

    a = dict.fromkeys(config_file)  # Or [*dict.fromkeys(a)] if you prefer
    print('\n config_file contents is below: \n')
    {print(line) for line in a}
    print('Items in a are: ', a.items())
    print('Keys in a are: ', a.keys())
    print('Values in a are: ', a.values())
    print('Type of a is: ', type(a))

    b = list(dict.fromkeys(port_mappings))  # Or [*dict.fromkeys(a)] if you prefer
    print('\n port_mappings contents: \n')
    {print(line) for line in b}

    # https://media.licdn.com/dms/document/C561FAQEJx0ldqomlFg/feedshare-document-pdf-analyzed/0/1678350857950?e=1679529600&v=beta&t=e6OTy2CQhrOZ5M_VSeATiBV5sJBiZUUiyeIM92qqzs0
    # Store people's favorite languages.
    fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    # Show each person's favorite language.
    for name, language in fav_languages.items():
        print(name + ": " + language)

    # https://bobbyhadz.com/blog/python-valueerror-update-sequence-element-0-has-length
    my_dict = {'name': 'Alice'}

    # ✅ passing a dict to update()
    my_dict.update({'name': 'Bobby'})
    print(my_dict)  # {'name': 'Bobby'}

    my_dict = {'name': 'Alice'}

    # ✅ passing a list of key-value pairs to update()
    a_list = [('name', 'Bobby'), ('age', 30)]
    my_dict.update(a_list)

    print(my_dict)  # {'name': 'Bobby', 'age': 30}

    my_dict = {'name': 'Alice'}

    # ✅ pass dictionary to the update() method
    my_dict.update({'name': 'Bobby', 'age': 30})

    print(my_dict)  # 👉️ {'name': 'Bobby', 'age': 30}

    my_dict = {'name': 'Alice', 'age': 29}

    my_list = [('name', 'Bob'), ('age', 30)]

    my_dict.update(my_list)

    print(my_dict)  # 👉️ {'name': 'Bob', 'age': 30}

    my_keys = ['name', 'age']

    my_values = ['Bobby', 29]

    my_dict = dict(zip(my_keys, my_values))

    print(my_dict)  # 👉️ {'name': 'Bobby', 'age': 29}

    # Here are all the different ways to create a dictionary.
    a = dict(name='Alice', age=29)
    b = {'name': 'Alice', 'age': 29}
    c = dict(zip(['name', 'age'], ['Alice', 29]))
    d = dict([('name', 'Alice'), ('age', 29)])
    e = dict({'name': 'Alice', 'age': 29})
    f = dict({'name': 'Alice'}, age=29)

    print(a == b == c == d == e == f)  # 👉️ True

    # https://www.geeksforgeeks.org/python-convert-key-value-pair-comma-separated-string-into-dictionary/?ref=rp
    # Python3 code to demonstrate
    # converting comma separated string
    # into dictionary
    
    # Initialising string
    ini_string1 = 'name = akshat, course = btech, branch = computer'


    for item in ini_string1.split(", "):
        trying = dict([item.split("=")])
        print('trying value is: ', trying)
    
    
    # Printing initial string
    print("Initial String", ini_string1)
    
    # Converting string into dictionary
    # using dict comprehension
    res = dict(item.split("=") for item in ini_string1.split(", "))
    
    # Printing resultant string
    print("Resultant dictionary", res)
    print(type(res))
    k = v = None
    for k in res:
        print(k, type(k), 'and ', res[k], type(res[k]))
    """
    for index, record in enumerate(res):
                k, v = record
                print(k, type(k), 'and ', v, type(v))
    """
    # Input: Initial String name = akshat, course = btech, branch = computer
    # Output: Resultant dictionary {'name ': ' akshat', 'course ': ' btech', 'branch ': ' computer'}

    pairs = { 
    1: "apple", 
    "orange": [2, 3, 4], 
    True: False, 
    12: "True", 
    } 

    print(pairs.get(1)) 
    print(pairs[1]) 
    print(pairs[12]) 

    test_dict = dict(name='John', age=30, city='New York')
    test_dict['name'] = test_dict['name'] + ', Kristy'
    test_dict.update({'now2':'Kristy2'})
    print(test_dict)

    test_dict = {'now2':[1, 2, 3]}
    # test_dict.update({'now2':'Kristy2'})    
    test_dict['now2'].extend('Kristy2')
    # Output: {'now2': [1, 2, 3, 'K', 'r', 'i', 's', 't', 'y', '2']}
    print(test_dict)
    test_dict['now2'].append('Kristy2')
    # Output: {'now2': [1, 2, 3, 'K', 'r', 'i', 's', 't', 'y', '2', 'Kristy2']}
    print(test_dict)
    test_dict['now2'].append((k, v))
    # Output: {'now2': [1, 2, 3, 'K', 'r', 'i', 's', 't', 'y', '2', 'Kristy2', ('branch ', None)]}
    print(test_dict)

    key, value = test_dict['now2'][11]
    print(key, value)
    # Output: branch  None

    
    # KRISTY testing
    dicttest = {}
    print('dicttest is : ', dicttest)
    dicttest.update({'key1':'value1'})
    print('dicttest is : ', dicttest)
    dicttest.update(key2 ='value2')
    print('dicttest is : ', dicttest)
    dicttest.update([('key3', 'value3')])
    print('dicttest is : ', dicttest)
    dicttest.update({'k1':'v1', 'k2':'v2'})
    print('dicttest is : ', dicttest)
    dicttest.update(k={'k1':'v1', 'k2':'v2'})
    print('dicttest is : ', dicttest)
    item = 'key4:value4'
    dicttest.update(dict([item.split(':')]))
    print('dicttest is : ', dicttest)

    def select_choice():
        i = 1
        card = "Driver licence"
        return i, card # or [i, card]

    dicttest.update([select_choice()])
    print('dicttest is : ', dicttest)

    print(dict.fromkeys([1,2,3]))
    print(dict.fromkeys((1,2,3)))
    """
    Output:
    {1: None, 2: None, 3: None}
    {1: None, 2: None, 3: None}
    """
    print(list(dict.fromkeys([1,2,3])))
    print(list(dict.fromkeys((1,2,3))))
    """
    Output:
    [1, 2, 3]
    [1, 2, 3]
    """
    print(list(dict.fromkeys([1,2,3, 3, 8, 9])))
    print(list(dict.fromkeys((1,2,3, 4, 3, 7))))
    """
    Output:
    [1, 2, 3, 8, 9]
    [1, 2, 3, 4, 7]
    """

    mydict = {1: 'a', 2: 'b'}
    for i, (k, v) in enumerate(mydict.items()):
        print("index: {}, key: {}, value: {}".format(i, k, v))
        # print(f"index: {i}, key: {k}, value: {v}")

    # which will print:
    # -----------------
    # index: 0, key: 1, value: a
    # index: 1, key: 2, value: b

    for i, (k, v) in enumerate(mydict.items()):
        # print("index: {}, key: {}, value: {}".format(i, k, v))
        print(f"index: {i}, key: {k}, value: {v}")

    print(config_headers := [item for i, item in enumerate(config_file) if item.count('__')])
    print(config_headersIndex := [i for i, item in enumerate(config_file) if item.count('__')])
    print(config_headers)
    print(config_headersIndex)

    print(map_headers := [item for i, item in enumerate(port_mappings) if item.count('__')])
    print(map_headersIndex := [i for i, item in enumerate(port_mappings) if item.count('__')])
    print(map_headers)
    print(map_headersIndex)

    """
    Input: 
    s[] = {1, 3, 0, 5, 8, 5}, 
    f[] = {2, 4, 6, 7, 9, 9} 
    Output: 1 2 4 5
    """
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    # Output : 6 7 1
    # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

    countNum = 1 # first meeting is always counted
    meetNum = [1]
    j = 0
    for i in range(len(s) - 1):
        if s[i + 1] > f [j]:
            meetNum.append(i + 2)
            print('s, f: ', s[i + 1], f[i+1])
            countNum +=1
            j = i + 1
    
    print("Max num of meetings is: ", countNum)
    print("Meeting numbers: ", meetNum)

    dictionary = {}
    for i in range(len(s) - 1):
        dictionary.update({s[i]: f[i]})

    print('dictionary is: ', dictionary)
    # sort by values:
    print({k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])})
    print(dict(sorted(dictionary.items(), key=lambda item: item[1])))
    # more methods of sorting dictionary are discussed here: https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
    """
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    Output: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
    or

    dict(sorted(x.items(), key=lambda item: item[1]))
    Output: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
    """
    # https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

    # Sort by keys:
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}    
    print(sorted_dict)
    # another way to sort by keys:
    dict1 = dict(sorted(dictionary.items()))
    print(dict1)
    dict1[75250] += 1000000000
    print(dict1)

    import json

    print(json.dumps(dictionary, indent=4, sort_keys=True))
    sortedDic = json.dumps(dictionary, sort_keys=True)
    print(sortedDic)

    """
    # https://www.geeksforgeeks.org/python-increment-value-in-dictionary/
    # Python3 code to demonstrate working of
    # Increment value in dictionary
    # Using get()
    """
    # Initialize dictionary
    test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5}
    
    # printing original dictionary
    print("The original dictionary : " + str(test_dict))
    
    # Using get()
    # Increment value in dictionary
    test_dict['best'] = test_dict.get('best', 0) + 3
        
    # printing result
    print("Dictionary after the increment of key : " + str(test_dict))

    # Python3 code to demonstrate working of
    # Increment value in dictionary
    # Using defaultdict()
    from collections import defaultdict
    
    # Initialize dictionary
    test_dict = defaultdict(int)
    
    # printing original dictionary
    print("The original dictionary : " + str(dict(test_dict)))
    
    # Using defaultdict()
    # Increment value in dictionary
    test_dict['best'] += 3
        
    # printing result
    print("Dictionary after the increment of key : " + str(dict(test_dict)))


    tmpDict = {}

    for i in range(3):
        # tmpDict['test'] = tmpDict.get('test',[]) + [7,8]
        tmpDict.update({'test':[4, 5]})
        try:
            tmpDict['test'].append([1, 2, 3])
        except KeyError:
            # tmpDict.update({'test':[9, 0]}) 
            # tmpDict['test'] = [9, 0]
            # tmpDict['test'] = [[9, 0]] 
            # raise Exception("Sorry") # https://www.w3schools.com/python/gloss_python_raise.asp
            raise KeyError("cannot append when dic is empty")
        print(tmpDict)
        print([(i, each) for i, each in enumerate(tmpDict.items())])

    # https://www.edureka.co/blog/hash-tables-and-hashmaps-in-python/
    my_dict={'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
    print(my_dict)
    del my_dict['Dave']  #removes key-value pair of 'Dave'
    print(my_dict)
    my_dict.pop('Ava')   #removes the value of 'Ava'
    print(my_dict)
    my_dict.popitem()    #removes the last inserted item
    print(my_dict)

    """
    Output:
    {'Dave': '004', 'Ava': '002', 'Joe': '003', 'Chris': '005'}
    {'Ava': '002', 'Joe': '003', 'Chris': '005'}
    {'Joe': '003', 'Chris': '005'}
    {'Joe': '003'}
    """
    # Converting Dictionary into a dataframe:
    import pandas as pd
    emp_details = {'Employee': {'Dave': {'ID': '001',
                                        'Salary': 2000,
                                        'Designation':'Python Developer'},
                                'Ava': {'ID':'002',
                                        'Salary': 2300,
                                        'Designation': 'Java Developer'},
                                'Joe': {'ID': '003',
                                        'Salary': 1843,
                                        'Designation': 'Hadoop Developer'}}}
    df=pd.DataFrame(emp_details['Employee'])
    print(df)
 
    XYZ_web= {'Day':[1,2,3,4,5,6], "Visitors":[1000, 700,6000,1000,400,350], "Bounce_Rate":[20,20, 23,15,10,34]}   
    df= pd.DataFrame(XYZ_web)
    print(df)

    """
    Output:
                            Dave             Ava               Joe
    ID                        001             002               003
    Salary                   2000            2300              1843
    Designation  Python Developer  Java Developer  Hadoop Developer

    Day  Visitors  Bounce_Rate
    0    1      1000           20
    1    2       700           20
    2    3      6000           23
    3    4      1000           15
    4    5       400           10
    5    6       350           34
    """

# https://www.geeksforgeeks.org/how-to-use-a-list-as-a-key-of-a-dictionary-in-python-3/
# Problems if lists were used as a key of dictionaries. Lists are mutable objects which means that we can change values inside a list append or delete values of the list . 
# Solution:

# Declaring a dictionary
d = {} 
  
# This is the list which we are 
# trying to use as a key to
# the dictionary
a =[1, 2, 3, 4, 5]
  
# converting the list a to a string
p = str(a)
d[p]= 1
  
# converting the list a to a tuple
q = tuple(a) 
d[q]= 1
  
for key, value in d.items():
    print(key, ':', value)

tmp = [(6, 7)]
d.update(tmp)
d[8] = 9
d.update({10:11})
print(d)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import re
sums = dict()
fh= open(r'my_new_folder/test.txt','r')
for line in fh:
    words = [word.lower() for word in re.findall(r'\b\w+\b', line)]
    for word in (words):
        if word in sums:
            sums[word] += 1
        else:
            sums[word] = 1
print(sums)
fh.close

from pprint import pprint
pprint(sums)

print(maxVal := max([x for x in sums.values()]))


# https://pythonguides.com/python-dictionary-find-a-key-by-value/
mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)]) # Prints george

print(maxKeys := list(sums.keys())[list(sums.values()).index(maxVal)])  # retrun key value from known maxVal, but only the 1st key found
"""
{'hello': 2, 'this': 6, 'is': 6, 'delhi': 2, 'paris': 2, 'london': 2}
{'delhi': 2, 'hello': 2, 'is': 6, 'london': 2, 'paris': 2, 'this': 6}
6
george
this
"""
maxKeys = []
for k, v in sums.items():
    if v == maxVal:
        maxKeys.append(k)
print(maxKeys)                                                          # retrun all key values from known maxVal

print([k for k, v in sums.items() if v == maxVal])                      # retrun all key values from known maxVal

"""
['this', 'is']
['this', 'is']
"""


