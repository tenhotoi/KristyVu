# https://www.geeksforgeeks.org/python-count-display-vowels-string/

# Python code to count and display number of vowels
# Simply using for and comparing it with a
# string containing all vowels

def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
     
# Driver Code
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);

"""
Output:
5
['e', 'e', 'o', 'e', 'e']

Time complexity: O(n)
Auxiliary Space: O(n)
"""

# Count vowels in a different way
# Using dictionary
def Check_Vow(string, vowels):
     
    # casefold has been used to ignore cases
    string = string.casefold()
     
    # Forms a dictionary with key as a vowel
    # and the value as 0
    count = {}.fromkeys(vowels, 0)
     
    # To count the vowels
    for character in string:
        if character in count:
            count[character] += 1   
    return count
     
# Driver Code
vowels = 'aeiou'
string = "Geeks for Geeks"
print (Check_Vow(string, vowels))

"""
Output
{'a': 0, 'e': 4, 'i': 0, 'o': 1, 'u': 0}

Time complexity: O(n)
Auxiliary Space: O(n)
"""

import re
# Count vowels in a different way
# Using re.findall
def Check_Vow(string, vowels):
     
    # Using re.findall in string
    str_list = re.findall(f'[{vowels}]', string, re.I)
     
    # printing length of string
    print(len(str_list))
     
    # Returning the list of matched element
    return str_list
     
# Driver Code
vowels = 'aeiou'
string = "Geeks for Geeks"
print (Check_Vow(string, vowels))

"""
Output
5
['e', 'e', 'o', 'e', 'e']

Time complexity: O(n), where n is the length of the input string. The time complexity of re.findall() method is O(n) because it scans the entire string once.
Auxiliary space: O(m), where m is the number of vowels in the input string. The space complexity is proportional to the number of vowels in the input string because we are storing all the matched vowels in a list.
"""

from collections import Counter
 
def count_and_display_vowels(string):
    vowels = 'aeiouAEIOU'
    vowels_list = filter(lambda c: c in vowels, string)
    count = Counter(vowels_list)
    return count
 
string = "Geeks for Geeks"
print(count_and_display_vowels(string))
print(max(count_and_display_vowels(string).values()))

"""
Output
Counter({'e': 4, 'o': 1})
5
"""

#defining recursive function
def Check_Vow(start,string,newlist):
    if start==len(string):   #base condition
        return len(newlist),newlist
    if string[start] in ['a','e','i','o','u']:   #check whether element is vowel or not
        newlist.append(string[start])
    return Check_Vow(start+1,string,newlist)  #recursive calling
#driver code
string = "Geeks for Geeks"
#calling recursive function
res=Check_Vow(0,string,[])
#printing result
print(*res,sep='\n')

"""
Output
5
['e', 'e', 'o', 'e', 'e']

Time complexity: O(n)
Auxiliary Space: O(n)
"""

# Python code to count and display number of vowels
# Simply using for and comparing it with a
# string containing all vowels and operator.countOf() method
import operator as op
 
 
def Check_Vow(string, vowels):
    final = [each for each in string if op.countOf(vowels, each) > 0]
    print(len(final))
    print(final)
 
 
# Driver Code
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)

"""
Output
5
['e', 'e', 'o', 'e', 'e']

Time Complexity: O(n)
Auxiliary Space: O(n)
"""

from functools import reduce
 
def check_vow(string, vowels):
    vowel_list = reduce(lambda x, y: x + [y] if y in vowels else x, string, [])
    print(len(vowel_list))
    print(vowel_list)
 
string = "Geeks for Geeks"
vowels = "AaEeIiOoUu"
check_vow(string, vowels)
#This code is contributed by Jyothi pinjala

"""
Output
5
['e', 'e', 'o', 'e', 'e']

Time Complexity: O(n), where n is the length of the given string. The reduce function iterates over each character in the string, so the time complexity is linear with respect to the length of the string.

Auxiliary Space: O(m), where m is the number of vowels in the given string. The reduce function creates a list of vowels in the string, which is stored in memory. The space complexity is linear with respect to the number of vowels in the string.
"""

print(map(lambda c: c in 'aeoiuAEOIU', 'DFJKDLSriuerieuti'))
print(list(map(lambda c: c in 'aeoiuAEOIU', 'DFJKDLSriuerieuti')))
print(sum(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(filter(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti'))
print(list(filter(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(list(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(sum(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(any(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(all(map(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))
print(Counter(filter(lambda c: c in "aeoiuAEOIU", 'DFJKDLSriuerieuti')))


"""
<map object at 0x0000020289DF2F50>   <========== 'map' and 'filter' returns something like this !!!
[False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, False, True]
7
<filter object at 0x0000025A4AAE33A0>
['i', 'u', 'e', 'i', 'e', 'u', 'i']
[False, False, False, False, False, False, False, False, True, True, True, False, True, True, True, False, True]
7
True
False
Counter({'i': 3, 'u': 2, 'e': 2})
"""

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/

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