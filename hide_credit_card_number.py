# https://www.educative.io/answers/how-to-mask-a-credit-card-number-with-asterisks-in-python

import re


def mask_cc_number(cc_string, digits_to_keep=4, mask_char='*'):
   cc_string_total = sum(map(str.isdigit, cc_string))

   if digits_to_keep >= cc_string_total:
       print("Not enough numbers. Add 10 or more numbers to the credit card number.")

   digits_to_mask = cc_string_total - digits_to_keep
   masked_cc_string = re.sub('\d', mask_char, cc_string, digits_to_mask)

   return masked_cc_string


print(mask_cc_number("4259 9826 4026 9299"))
print(mask_cc_number("4259 982& 4026 9299"))
print(mask_cc_number("4259 9826 40p6 9299"))

"""
Explanation
Line 1: Import the re module.
Line 4: Define cc_string_total to hold the total of the characters in the string.
Line 7–8: Check if digits_to_keep >= cc_string_total is true and provide an error message.
Line 10: Define digits_to_mask as the difference between cc_string_total and digits_to_keep.
Line 11: Define masked_cc_string as the value of the regex sub() function call.
Line 13: Return the value of masked_cc_string.
Note: if the character is not a digit, such as a letter or a symbol, the character will not be masked by an asterisk. However, the character will be counted towards the total number of characters in the credit card string.
"""

# How to validate a credit card number in Python
"""
https://www.codespeedy.com/python-program-to-validate-a-credit-card-number/
conditions to validate a credit card number

It must contain exactly 16 digits.
It should only contain 0-9 digits.
It must start with either 9 or 7 or 3.
It may have digits in a group of 4 with a separator (-).
It must not contain any other symbols such as _ or space(‘ ‘).
These conditions are just for our convenience’s sake only just for understanding purposes.
First, let us see some examples of valid and invalid credit card numbers with our conditions applied to it for a python program to validate a given credit card number.

92136258797157867 #17 digits in card number -> Invalid
7123456789123456 ->Valid
3123-7754-9978-2343 ->Valid
4997-5624-9832-2211 Starting with digit 4 -> Invalid
9675 – 7756-8864-9075 contains space in between ->Invalid
"""
import re
sample_list=['3123456789123456','9123-4567-8912-3456','5123456789123456','7123 - 4567-8912 -3456','44244x4424442444','0525362587961578']
pattern = '^[973][0-9]{15}|[973][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
for eachnumber in sample_list:
    result = re.match(pattern, eachnumber)
    if result:
        print(eachnumber+"->"+"Valid card")
    else:
        print(eachnumber+"->"+"Invalid card")

"""
output:

3123456789123456->Valid card

9123-4567-8912-3456->Valid card

5123456789123456->Invalid card

7123 - 4567-8912 -3456->Invalid card

44244x4424442444->Invalid card

0525362587961578->Invalid card
"""
# https://www.codespeedy.com/validate-email-in-python/
"""
https://www.codespeedy.com/validate-email-in-python/
Here we have calculated the length of email passed in the function and the position of “@” and “.” in the email.

Basic validations for an email are:

It must contain at least one alphabet.
Email cannot start with @
@ and dot cannot exist together.
There must be at least one character before @ and after the dot.
"""
def email_validation(x):
    pattern = '^(!@)[a-zA-Z]!(@.)'
    a=0
    y=len(x)
    dot=x.find(".")
    at=x.find("@")
    for i in range (0,at):
        if((x[i]>='a' and x[i]<='z') or (x[i]>='A' and x[i]<='Z')):
            a=a+1
    if(a>0 and at>0 and (dot-at)>0 and (dot+1)<y):
        print("Valid Email")
    else:
        print("Invalid Email")

email_validation("njh@gmail.co")

print('fjdkfj'.find('k99'))
if 'fjdkfj'.find('k99'):
    print('see if it prints when -1')
print('fjdkfj'.index('d00'))
"""
-1
see if it prints when -1
Traceback (most recent call last):
  File "c:\Users\tenho\OneDrive\Desktop\pythonpractice\hide_credit_card_number.py", line 108, in <module>
    print('fjdkfj'.index('d00'))
          ^^^^^^^^^^^^^^^^^^^^^
ValueError: substring not found
"""

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
