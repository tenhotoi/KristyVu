# pip install bidict
# Python implementation for bidirectional
# hash table or two way dictionary.
 
# import the bidict class of the bidict module
from bidict import bidict
 
# creating a dictionary mapping commonly used
# IT short forms to their full forms
dict_it_fullforms = {'APK': 'Android Application Package',
                     'CPU': 'Central Processing Unit',
                     'SMS': 'Short Message Service',
                     'USB': 'Universal Serial Bus',
                     'WIFI': 'Wireless Fidelity',
                     'WWW': 'World Wide Web'}
 
# Creating a bidict object
bidict_it_fullforms = bidict(dict_it_fullforms)
 
# Lookup using short forms
print(bidict_it_fullforms['APK'])
print(bidict_it_fullforms['SMS'])
print(bidict_it_fullforms['WIFI'])
 
# Inverse attribute of bidict object
bidict_it_shortforms = bidict_it_fullforms.inverse
 
# Lookup using full forms
print(bidict_it_shortforms['Central Processing Unit'])
print(bidict_it_shortforms['Universal Serial Bus'])
print(bidict_it_shortforms['World Wide Web'])
 
# Adding SIM : Subscriber Identity Module to the bi-dictionary
bidict_it_shortforms['Subscriber Identity Module'] = 'SIM'
print(bidict_it_fullforms['SIM'])