# https://leetcode.com/problems/valid-anagram/
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

"""
An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, “abcd” and “dabc” are an anagram of each other.

Examples:

Input: str1 = “listen”  str2 = “silent”
Output: “Anagram”
Explanation: All characters of “listen” and “silent” are the same.

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    # def __init__(self) -> None:
    #    pass

    def isAnagram_Kristy(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        print(re.findall('[a-z]', s))
        print(re.findall('[a-z]', t))
        if (l_s == 0) or (l_t == 0) or (l_s > 5 * 104) or (l_t > 5 * 104) or (len(re.findall('[a-z]', s)) != l_s) or (len(re.findall('[a-z]', t)) != l_t):
            print('Invalid input string(s)!'.center(60, '!'))
            return False
        
        for char in s:
            if char not in t:
                return False
            
        for char in t:
            if char not in s:
                return False
            
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        l_s = len(s)
        l_t = len(t)
        print(re.findall('[a-z]', s))
        print(re.findall('[a-z]', t))
        if (l_s == l_t == 0) or (l_s > 5 * 104) or (l_t > 5 * 104) or (len(re.findall('[a-z]', s)) != l_s) or (len(re.findall('[a-z]', t)) != l_t):
            print('Invalid input string(s)!'.center(60, '!'))
            return False
        
        # https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
        if sorted(s) == sorted(t):
            return True
        else: 
            return False
        
# https://www.geeksforgeeks.org/check-if-a-string-contains-uppercase-lowercase-special-characters-and-numeric-values/
# Python3 program for the
# above approach
"""
Given string str of length N, the task is to check whether the given string contains uppercase alphabets, lowercase alphabets, special characters, and numeric values or not. If the string contains all of them, then print “Yes”. Otherwise, print “No”. 

Examples: 

Input: str = “#GeeksForGeeks123@” 
Output: Yes 
Explanation: 
The given string contains uppercase characters(‘G’, ‘F’), lowercase characters(‘e’, ‘k’, ‘s’, ‘o’, ‘r’), special characters( ‘#’, ‘@’), and numeric values(‘1’, ‘2’, ‘3’). Therefore, the output is Yes. 
 

Input: str = “GeeksForGeeks” 
Output: No 
Explanation: 
The given string contains only uppercase characters and lowercase characters. Therefore, the output is No.
"""
import re
 
# Function that checks if a string
# contains uppercase, lowercase
# special character & numeric value
def isAllPresent(str):
 
    # ReGex to check if a string
    # contains uppercase, lowercase
    # special character & numeric value
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")
     
    # Compile the ReGex
    print(p := re.compile(regex))
 
    # If the string is empty
    # return false
    if (str == None):
        print("No")
        return
 
    # Print Yes if string
    # matches ReGex
    if(re.search(p, str)):
        print("Yes")
    else:
        print("No")
 
def isUpper(s):
    return re.search(r'/^[^a-z]*$/', s)

def isLower(s): 
    return re.search(r'/^[^A-Z]*$/', s)

# Driver code
if __name__ == '__main__':
    # Given string
    str = "#GeeksForGeeks123@"
    
    #Function Call
    isAllPresent(str)
    
    # This code is contributed by avanitrachhadiya2155

    """
    Output:
    Yes
    """

    s = Solution()
    print(s.isAnagram('fjdkd', 'dfjds'))
    print(s.isAnagram('listen', 'silent'))

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
    """