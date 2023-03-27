# https://www.geeksforgeeks.org/the-most-occurring-number-in-a-string-using-regex-in-python/?ref=rp

# your code goes here# Python program to 
# find the most occurring element 
"""
Examples:
Input :geek55of55geeks4abc3dr2 
Output :55

Input :abcd1def2high2bnasvd3vjhd44
Output :2
"""
import re 
from collections import Counter 
  
def most_occr_element(word):
      
    # re.findall will extract all the elements 
    # from the string and make a list
    arr = re.findall(r'[0-9]+', word)    
      
    # to store maxm frequency
    maxm = 0  
  
    # to store maxm element of most frequency
    max_elem = 0
      
    # counter will store all the number with 
    # their frequencies
    # c = counter((55, 2), (2, 1), (3, 1), (4, 1))    
    c = Counter(arr)
    
    # Store all the keys of counter in a list in
    # which first would we our required element    
    for x in list(c.keys()):
  
        if c[x]>= maxm:
            maxm = c[x]
            max_elem = int(x)
                  
    return max_elem
  
# Driver program 
if __name__ == "__main__": 
    word = 'geek55of55gee4ksabc3dr2x'
    print(most_occr_element(word))

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

# https://www.geeksforgeeks.org/python-check-if-string-matches-regex-list/?ref=rp
# Python3 code to demonstrate working of
# Check if string matches regex list
# Using join regex + loop + re.match()
import re
 
# initializing list
test_list = ["gee*", "gf*", "df.*", "re"]
 
# printing list
print("The original list : " + str(test_list))
 
# initializing test_str
test_str = "geeksforgeeks"
 
# Check if string matches regex list
# Using join regex + loop + re.match()
print(temp := '(?:% s)' % '|'.join(test_list))
res = False
if re.match(temp, test_str):
    res = True

print(re.match(temp, test_str))
# Output: <re.Match object; span=(0, 3), match='gee'>
 
# Printing result
print("Does string match any of regex in list ? : {}".format(str(res)))

"""
Output
The original list : ['gee*', 'gf*', 'df.*', 're']
(?:gee*|gf*|df.*|re)
<re.Match object; span=(0, 3), match='gee'>
Does string match any of regex in list ? : True
"""

import fnmatch
 
# initializing list
regex_list = ["gee*", "gf*", "df.*", "re"]

# printing list
print("The original list : " + str(regex_list))
   
# initializing test_str
test_str = "geeksforgeeks"
   
# Check if string matches regex list
# Using filter + fnmatch
res = bool(list(filter(lambda x: fnmatch.fnmatch(test_str, x), regex_list)))
 
# Printing result
print(f"Does string match any of regex in list ? : {str(res)}")

print(list(filter(lambda x: fnmatch.fnmatch(test_str, x), regex_list)))

for x in regex_list:
    print(fnmatch.fnmatch(test_str, x))

print([x for x in test_str if x in regex_list])
print(re.match("gee*", test_str))
print(bool(re.match("gee*", test_str)))
print(re.match("geedfjkdjfdk*", test_str))
print(bool(re.match("geedfjkdjfdk*", test_str)))

"""
https://regexpattern.com/first-letter-uppercase/
A regular expression to match and validate if the first letter of a string is uppercase.
/^[A-Z][a-z0-9_-]{3,19}$/

https://regexpattern.com/uppercase-letter/
A regular expression to match all uppercase letters in text.
/[A-Z\s]+/

https://regexpattern.com/4-6-digits/
Regular Expressions that exactly match 4 or 6 digits, which are typically used in Pin Code.
4 Digits Regex:
/^[0-9]{4}$/

https://regexpattern.com/one-digit-number/
A regular expression that allows you to match all one-digit numbers in a string.
/\b\d\b/g

https://www.geeksforgeeks.org/python-program-to-check-if-lowercase-letters-exist-in-a-string/
https://www.w3schools.com/python/python_regex.asp

Character	Description	Example	Try it
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 

A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

Character	Description	Example	Try it
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	

A set is a set of characters inside a pair of square brackets [] with a special meaning:

Set	Description	Try it
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""

"""
Output
The original list : ['gee*', 'gf*', 'df.*', 're']
Does string match any of regex in list ? : True
"""

print(regex_str := '(?:%s)' % '|'.join(regex_list))
print(re.match(regex_str, test_str))
print(bool(re.match(regex_str, test_str)))

print(bool(list(filter(lambda x: fnmatch.fnmatch(test_str,x), regex_list))))

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

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