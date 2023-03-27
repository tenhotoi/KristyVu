"""
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def valid_parentheses(s):
    parenttheses = r'()[]{}'
    l = len(s)
    if l == 0 or l > 104:
        print("Invalid string input:  Length should be between 1 and 104.")
        return False
    
    print(' Dictionary contents '.center(60, '-'))              # print at the center of 60 range
    dic = dict(zip(parenttheses, [0]*len(parenttheses)))        # print at the center of 60 range
    print('{:^60}'.format(str(dic)))                            # print at the center of 60 range
    print(f'{str(dic):^60}')
    print(' Checking string '.center(60, '='))                  # print at the center of 60 range
    print(dic['['])
    for each in s:
        if each not in parenttheses:
            return r"Invalid string: string consists of parentheses only '()[]{}'" 
        elif ((each == ')') and (dic['('] == 0)) or ((each == ']') and (dic['['] == 0)) or ((each == '}') and (dic['{'] == 0)):
                print("Invalid string: Open brackets must be closed in the correct order.") 
                return False
        elif (each == '(') or (each == '[') or (each == '{'):
            dic[each] = 1
        elif (each == ')') or (each == ']') or (each == '{'):
            dic[each] = 0

    return True

print(valid_parentheses('[][](})'))

s = "()[]{}"
print(valid_parentheses(s))

s = "(]"
print(valid_parentheses(s))

"""
Output:

{'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
0
Invalid string: Open brackets must be closed in the correct order.
False
{'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
0
True
{'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
0
Invalid string: Open brackets must be closed in the correct order.
False
"""
# https://medium.com/nerd-for-tech/leetcode-valid-parentheses-772565465fe7
# https://www.techgeekbuzz.com/blog/python-dictionary-get/

"""
Example: Get a value from a Python Dictionary
Now let's create a dictionary and access its elements using the get() method.
"""
customer = {
            "name": "Nancy",
            "balance": "$2,481.32",
            "age": 26,
            "gender": "female",
            "email": "Nancy@mail.com",
            }
#print("--------Customer Details----------")
print("Customer Details".center(60, '-'))
print("Name:", customer.get('name'))
print("Age:", customer.get('age'))
print("Email:", customer.get('email'))
print("Balance:", customer.get('balance'))
print("Loan:", customer.get('loan'))  #no loan key in the  dictionary
# print(''.center(60,'-'))
# print('-'.center(60, '-'))

"""
Output

--------Customer Details----------
Name: Nancy
Age: 26
Email: Nancy@mail.com
Balance: $2,481.32
Loan: None
In the above example, we are accessing the customer dictionary details using the get() method.  In this example, we have accessed the customer's Name, Age, Email, Balance, and Loan using name , age , email , balance and loan keys. But in the customer dictionary we have no key with loan name, in that statement, the customer.get('loan') statement returns None . If a dictionary does not have the specified key passed in the get() method as an argument, the method returns the None value. If you do not want the None value, you can also specify the default argument value for non-existent keys.

Example

Now, let's define a default argument for the customer.get('loan') statement for which we were getting the None value in the above example.
"""
customer = {
            "name": "Nancy",
            "balance": "$2,481.32",
            "age": 26,
            "gender": "female",
            "email": "Nancy@mail.com",
            }
#print("--------Customer Details----------")
print("Customer Details".center(60, '-'))
print("Name:", customer.get('name'))
print("Age:", customer.get('age'))
print("Email:", customer.get('email'))
print("Balance:", customer.get('balance'))
print("Loan:", customer.get('loan', "No Loan Amount"))  #no loan key in the  dictionary

"""
Output

--------Customer Details----------
Name: Nancy
Age: 26
Email: Nancy@mail.com
Balance: $2,481.32
Loan: No Loan Amount
Python Dictionary get(key) method Vs Square bracket Notation dict[key]
We can either use the square brackets or get() method to access an individual dictionary value using a key name. But there are some differences between them that you should know before using one. The get() method accepts the key name as an argument and returns its associative value if the key is present in the dictionary.

If the key does not exist in the dictionary, the get() method returns the None value or the value specified as a default argument. With square bracket notation, dict[key] we can also access the dictionary value using a key. But in the square bracket, if we pass a key name that does not exist in the dictionary the square bracket notation return the KeyError.

Example(Invalid key with get() method)
"""
customer = {
            "name": "Nancy",
            "balance": "$2,481.32",
            "age": 26,
            "gender": "female",
            "email": "Nancy@mail.com",
            }

print(''.ljust(60, '-'))
print("Name:",customer.get('Name')) #invalid Name key

"""
Output

Name: None
Example(Invalid key with Square brackets)
"""
customer = {
            "name": "Nancy",
            "balance": "$2,481.32",
            "age": 26,
            "gender": "female",
            "email": "Nancy@mail.com",
            }

try:
     print("Name:",customer['Name'])   #invalid Name key
except KeyError as err:
     print(err)

print(''.rjust(60, '-'))

"""
Output

Traceback (most recent call last):
  File "main.py", line 9, in 
    print("Name:",customer['Name'])   #invalid Name key
KeyError: 'Name'

Conclusion
The Python dictionary's get method is used to retrieve a specific value from a dictionary by passing the key name as the argument. The get() method is error-free and more efficient as compared to the square bracket notation. The get() method does not return an error if the passed key name does not exist in the dictionary. Instead, it returns None.
"""