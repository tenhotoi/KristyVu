# https://www.geeksforgeeks.org/how-to-read-dictionary-from-file-in-python/
# https://www.geeksforgeeks.org/read-json-file-using-python/

"""
We can read a dictionary from a file in 3 ways:

Using the json.loads() method : Converts the string of valid dictionary into json form.
Using the ast.literal_eval() method : Function safer than the eval function and can be used for interconversion of all data types other than dictionary as well.
Using the pickle.loads() method : We can also use Pickle module if the file is serialized into a character stream.

JSON OBJECT	PYTHON OBJECT
object	dict
array	list
string	str
null	None
(number (int))	int
(number (real))	float
true	True
false	False

1. Method 1 : Using json.loads() :
"""

# importing the module
import json

# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5}

# writing the data to the file
with open('dictionary.txt', 'w', encoding='utf-8') as f:
    json.dump(test_dict, f)

# reading the data from the file
with open('dictionary.txt') as f:
    data = f.read()
  
print("Method 1 - Using json.loads() : Data type before reconstruction : ", type(data))
print(data)                 # {"gfg": 1, "is": 2, "for": 4, "CS": 5}
print(json.dumps(data))     # "{\"gfg\": 1, \"is\": 2, \"for\": 4, \"CS\": 5}"

# reconstructing the data as a dictionary
js = json.loads(data)
  
print("Method 1 - Using json.loads() : Data type after reconstruction : ", type(js))
print(js)                   # {'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}
print(json.dumps(js))       # {"gfg": 1, "is": 2, "for": 4, "CS": 5}

# https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-json/
# convert into json
final = json.dumps(js, indent=2)  # need to set indent value to get a beautiful display of dictionary
  
# display
print(final)

with open('dictionary.txt') as f:
    jd = json.load(f)
    print('testing json.load(f) right after opening the file')
    print('this works since we did json.dump() with actual dict value, not text earlier')
    print("Type: {} \n Data: {}".format(type(jd), jd))

"""
Output :

Data type before reconstruction :  <class 'str'>
{"gfg": 1, "is": 2, "for": 4, "CS": 5}
"{\"gfg\": 1, \"is\": 2, \"for\": 4, \"CS\": 5}"
Data type after reconstruction :  <class 'dict'>
{'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}
{"gfg": 1, "is": 2, "for": 4, "CS": 5}
{
  "gfg": 1,
  "is": 2,
  "for": 4,
  "CS": 5
}
testing json.load(f) right after opening the file
this works since we did json.dump() with actual dict value, not text earlier
Type: <class 'dict'>
 Data: {'gfg': 1, 'is': 2, 'for': 4, 'CS': 5}

2. Method 2 : Using ast.literal_eval() :
"""
# importing the module
import ast
  
# reading the data from the file
with open('dictionary.txt') as f:
    data = f.read()
  
print("Method 2 - Using ast.literal_eval() : Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
d = ast.literal_eval(data)
  
print("Method 2 - Using ast.literal_eval() : Data type after reconstruction : ", type(d))
print(d)
print(json.dumps(d, indent=2))

"""
Output :

Data type before reconstruction :  <class 'str'>
Data type after reconstruction :  <class 'dict'>
{'Name': 'John', 'Age': 21, 'Id': 28}

3, Method 3 : We can use the Pickle module for the same purpose, but this method will only work if the file is serialized into a character stream and not in text format. To know more about Pickling in Python click here
"""
# importing the module
import pickle
  
# opening file in write mode (binary)
file = open("dictionary.txt", "wb")
  
my_dict = {"Name": "John",
           "Age": 21,
           "Id": 28}
  
# serializing dictionary 
pickle.dump(my_dict, file)
  
# closing the file
file.close()
  
# reading the data from the file
with open('dictionary.txt', 'rb') as handle:
    data = handle.read()
  
print("Method 3 - Pickle module: Data type before reconstruction : ", type(data))
  
# reconstructing the data as dictionary
d = pickle.loads(data)
  
print("Method 3 - Pickle module: Data type after reconstruction : ", type(d))
print(d)
print(json.dumps(d, indent=2))

"""
Output :

Data type before reconstruction :  <class 'bytes'>
Data type after reconstruction :  <class 'dict'>
{'Name': 'John', 'Age': 21, 'Id': 28}
"""

# importing the module
import json
from string import Template

data = []
test_dict_template = Template('{' + "'gfg$val' : 1$val, 'is$val' : 2$val, 'for$val' : 4$val, 'CS$val' : 5$val" + '}')
for i in range(5):
    data.append((eval(test_dict_template.substitute(val = i + 1))))
print(data)
"""
Output:
[{'gfg1': 11, 'is1': 21, 'for1': 41, 'CS1': 51}, {'gfg2': 12, 'is2': 22, 'for2': 42, 'CS2': 52}, {'gfg3': 13, 'is3': 23, 'for3': 43, 'CS3': 53}, {'gfg4': 14, 'is4': 24, 'for4': 44, 'CS4': 54}, {'gfg5': 15, 'is5': 25, 'for5': 45, 'CS5': 55}]
"""

# https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-json/
# convert into json
final = json.dumps(data, indent=2)
  
# display
print(final)
"""
Output:
[
  {
    "gfg1": 11,
    "is1": 21,
    "for1": 41,
    "CS1": 51
  },
  {
    "gfg2": 12,
    "is2": 22,
    "for2": 42,
    "CS2": 52
  },
  {
    "gfg3": 13,
    "is3": 23,
    "for3": 43,
    "CS3": 53
  },
  {
    "gfg4": 14,
    "is4": 24,
    "for4": 44,
    "CS4": 54
  },
  {
    "gfg5": 15,
    "is5": 25,
    "for5": 45,
    "CS5": 55
  }
]
"""
# convert into json
# file name is mydata
with open("mydata.json", "w") as final:
    json.dump(data, final)
  
# from google.colab import files
# download the json file
# files.download('mydata.json')

# reading the data from the file
with open('mydata.json') as f:
    # print(json.load(f)) # error on terminal; this does NOT work since we did json.dump() with text earlier, not actual dict value
    data = f.read()
  
print("Data type before reconstruction : ", type(data))
      
# reconstructing the data as a dictionary
js = json.loads(data)
  
print("Data type after reconstruction : ", type(js))
print(js)

# https://www.geeksforgeeks.org/python-convert-list-of-dictionaries-to-json/
# convert into json
final = json.dumps(js, indent=2)
  
# display
print(final)

"""
[{'gfg1': 11, 'is1': 21, 'for1': 41, 'CS1': 51}, {'gfg2': 12, 'is2': 22, 'for2': 42, 'CS2': 52}, {'gfg3': 13, 'is3': 23, 'for3': 43, 'CS3': 53}, {'gfg4': 14, 'is4': 24, 'for4': 44, 'CS4': 54}, {'gfg5': 15, 'is5': 25, 'for5': 45, 'CS5': 55}]
[
  {
    "gfg1": 11,
    "is1": 21,
    "for1": 41,
    "CS1": 51
  },
  {
    "gfg2": 12,
    "is2": 22,
    "for2": 42,
    "CS2": 52
  },
  {
    "gfg3": 13,
    "is3": 23,
    "for3": 43,
    "CS3": 53
  },
  {
    "gfg4": 14,
    "is4": 24,
    "for4": 44,
    "CS4": 54
  },
  {
    "gfg5": 15,
    "is5": 25,
    "for5": 45,
    "CS5": 55
  }
]
"""

# convert into json
# file name is mydata
with open("mydata_eval.json", "w") as final:
    json.dump(eval(data), final)

# reading the data from the file
with open('mydata_eval.json') as f:
    print(jd_eval := json.load(f)) # error on terminal; this does WORK since we did json.dump() with actual dict value, not text earlier
    print('testing json.load(f) right after opening the file')
    print('this works since we did json.dump() with actual dict value, not text earlier')
    print("Type: {} \n Data: {}".format(type(jd_eval), jd_eval))
    print(nice_layout := json.dumps(jd_eval, indent= 2))   

"""
>>>>>>>>>>>>>     NOTES: This WORKS!!!!   <<<<<<<<<<<<<<<<<<<<<<<<<<<<
LESSION LEARNED: We should use always include 'eval' just in case!!!!!

Output:

[{'gfg1': 11, 'is1': 21, 'for1': 41, 'CS1': 51}, {'gfg2': 12, 'is2': 22, 'for2': 42, 'CS2': 52}, {'gfg3': 13, 'is3': 23, 'for3': 43, 'CS3': 53}, {'gfg4': 14, 'is4': 24, 'for4': 44, 'CS4': 54}, {'gfg5': 15, 'is5': 25, 'for5': 45, 'CS5': 55}]
testing json.load(f) right after opening the file
this works since we did json.dump() with actual dict value, not text earlier
Type: <class 'list'>
 Data: [{'gfg1': 11, 'is1': 21, 'for1': 41, 'CS1': 51}, {'gfg2': 12, 'is2': 22, 'for2': 42, 'CS2': 52}, {'gfg3': 13, 'is3': 23, 'for3': 43, 'CS3': 53}, {'gfg4': 14, 'is4': 24, 'for4': 44, 'CS4': 54}, {'gfg5': 15, 'is5': 25, 'for5': 45, 'CS5': 55}]
[
  {
    "gfg1": 11,
    "is1": 21,
    "for1": 41,
    "CS1": 51
  },
  {
    "gfg2": 12,
    "is2": 22,
    "for2": 42,
    "CS2": 52
  },
  {
    "gfg3": 13,
    "is3": 23,
    "for3": 43,
    "CS3": 53
  },
  {
    "gfg4": 14,
    "is4": 24,
    "for4": 44,
    "CS4": 54
  },
  {
    "gfg5": 15,
    "is5": 25,
    "for5": 45,
    "CS5": 55
  }
]
"""
with open('eye.txt', 'w+') as f:
    f.write(nice_layout)
    f.seek(0)
    # print(df_read := f.read())        # it prints out beautiful layout
    # print(type(df_read))              # <class 'str'>
    print(df_jload := json.load(f))
    print(type(df_jload))               # <class 'list'>

"""
[{'gfg1': 11, 'is1': 21, 'for1': 41, 'CS1': 51}, {'gfg2': 12, 'is2': 22, 'for2': 42, 'CS2': 52}, {'gfg3': 13, 'is3': 23, 'for3': 43, 'CS3': 53}, {'gfg4': 14, 'is4': 24, 'for4': 44, 'CS4': 54}, {'gfg5': 15, 'is5': 25, 'for5': 45, 'CS5': 55}]
<class 'list'>

NOTES: CAN'T have both f.read() and json.load() used at the same time!!!

https://www.geeksforgeeks.org/python-difference-between-json-load-and-json-loads/

json.load() takes a file object and returns the json object. It is used to read JSON encoded data from a file and convert it into a Python dictionary and deserialize a file itself i.e. it accepts a file object.

json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
"""
