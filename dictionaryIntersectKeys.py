# https://www.geeksforgeeks.org/python-intersect-two-dictionaries-through-keys/?ref=rp

# Method #1: Using dict comprehension 

# Python code to demonstrate
# intersection of two dictionaries
# using dict comprehension
 
# inititialising dictionary
ini_dict1 = {'nikhil': 1, 'vashu' : 5,
             'manjeet' : 10, 'akshat' : 15}
ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' : 56}
 
# printing initial json
print ("initial 1st dictionary", ini_dict1)
print ("initial 2nd dictionary", ini_dict2)
 
# intersecting two dictionaries
final_dict = {x:ini_dict1[x] for x in ini_dict1
                              if x in ini_dict2}
 
# printing final result
print ("final dictionary", str(final_dict))

#Method #2: Using & operator 

# Python code to demonstrate
# intersection of two dictionaries
# using dict comprehension
 
# inititialising dictionary
ini_dict1 = {'nikhil': 1, 'vashu' : 5,
             'manjeet' : 10, 'akshat' : 15}
ini_dict2 = {'akshat' :15, 'nikhil' : 1, 'me' : 56}
 
# printing initial json
print ("initial 1st dictionary", ini_dict1)
print ("initial 2nd dictionary", ini_dict2)
 
# intersecting two dictionaries
final_dict = dict(ini_dict1.items() & ini_dict2.items())
 
# printing final result
print ("final dictionary", str(final_dict))


# Method #3: Using intersection method

# Initialize dictionaries
dict1 = {'nikhil': 1, 'vashu': 5,
         'manjeet': 10, 'akshat': 15}
dict2 = {'akshat': 15, 'nikhil': 1, 'me': 56}
 
 
# Find intersection of dictionaries
intersection = {i: dict1[i]
                for i in set(dict1.keys()).intersection(set(dict2.keys()))}
 
print(intersection)
# This code is contributed by Edula Vinay Kumar Reddy

