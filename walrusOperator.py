"""
The "walrus operator" is a new syntax feature introduced in Python 3.8. It is denoted by the := symbol and is used for inline variable assignment.

Before the walrus operator, you would have to declare a variable and then assign it a value like this:
"""

# Before the walrus operator:
number = int(input("Enter a number: "))
if number > 10:
    print('The number is greater than 10.')

# With walrus operator:
if (number := int(input('Enter a number: '))) > 10:
    print('The number is greater than 10.')

if (int(input('Enter a number: '))) > 10:
    print('The number is greater than 10.')