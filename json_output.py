# https://www.geeksforgeeks.org/json-formatting-python/?ref=rp

"""
Functions:
json.dump(obj, fileObj): Serializes obj as a JSON formatted stream to fileObj.
json.dumps(obj) : Serializes obj as JSON formatted string.
json.load(JSONfile) : De-serializes JSONfile to a Python object.
json.loads(JSONfile) : De-serializes JSONfile(type: string) to a Python object.

Classes:
JSONEncoder: An encoder class to convert Python objects to JSON format.
JSONDecoder: A decoder class to convert JSON format file into Python obj.
The conversions are based on this conversion table.

Implementation:
Encoding
We will be using dump(), dumps() and JSON.Encoder class.
"""

#Code will run in Python 3
  
from io import StringIO
import json
  
fileObj = StringIO()
json.dump(["Hello", "Geeks"], fileObj)
print("Using json.dump(): "+str(fileObj.getvalue()))
  
class TypeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, type):
            return str(obj)
  
print("Using json.dumps(): "+str(json.dumps(type(str), cls=TypeEncoder)))
print("Using json.JSONEncoder().encode"+
      str(TypeEncoder().encode(type(list))))
print("Using json.JSONEncoder().iterencode"+
      str(list(TypeEncoder().iterencode(type(dict)))))

"""
Output:
Using json.dump(): ["Hello", "Geeks"]
Using json.dumps(): ""
Using json.JSONEncoder().encode""
Using json.JSONEncoder().iterencode['""']

Decoding
We will be using load(), loads() and JSON.Decoder class.
"""

#Code will run in Python 3
  
from io import StringIO
import json
  
fileObj = StringIO('["Geeks for Geeks"]')
print("Using json.load(): "+str(json.load(fileObj)))
print("Using json.loads(): "+str(json.loads('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().decode(): " +
    str(json.JSONDecoder().decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))
print("Using json.JSONDecoder().raw_decode(): " +
    str(json.JSONDecoder().raw_decode('{"Geeks": 1, "for": 2, "Geeks": 3}')))

"""
Output:
Using json.load(): ['Geeks for Geeks']
Using json.loads(): {'for': 2, 'Geeks': 3}
Using json.JSONDecoder().decode(): {'for': 2, 'Geeks': 3}
Using json.JSONDecoder().raw_decode(): ({'for': 2, 'Geeks': 3}, 34)

Reference:
https://docs.python.org/3/library/json.html

Javascript Object Notation abbreviated as JSON is a light-weight data interchange format. It Encode Python objects as JSON strings, and decode JSON strings into Python objects .

Many of the APIs like Github. send their results in this format. JSON is probably most widely used for communicating between the web server and client in an AJAX application, but is not limited to that problem domain.
For example, if you are trying to build an exciting project like this, we need to format the JSON output to render necessary results. So lets dive into json module which Python offers for formatting JSON output.
"""