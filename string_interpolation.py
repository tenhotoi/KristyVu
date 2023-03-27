import json
import re

# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5}

with open('eye.txt', 'a+', encoding='utf-8') as f:
    json.dump(test_dict, f)
    # f.write(f'{test_dict}')  # <====== doesn't work
    # f.seek(0)
    # print('CONTENTS FROM READ(): ', f.read())
    # f.seek(0)
    # print('CONTENTS FROM READLINES(): ', f.readlines())
    # f.seek(0)
    # f.readlines()
    value = ('testing tuple', 42)
    f.write(f'\n{str(value)}')   # s = str(value)  # convert the tuple to string
    value = ['testing list', 42]
    f.write(f'\n{str(value)}')
    # json.dump(value,f)  # <====== doesn't work
    f.seek(0)
    contents = f.readlines()
    #contents = f.read().splitlines()
    print('CONTENTS FROM READ(): ', contents)
    # f.seek(0)
    # print(list(f))
    print(f'checking the last value {contents[-1]}')
    print('checking the last value {0} is of type {1}, where the key is \'{0[0]}\' and value is {0[1]}.'.format(eval(contents[-1]), type(eval(contents[-1]))))

    print(f'checking the second last value {contents[-2]}')
    print('checking the second last value {0} is of type {1}, where the key is \'{0[0]}\' and value is {0[1]}.'.format(eval(contents[-2]), type(eval(contents[-2])))) 
    # for each in contents:
    #    print(f'testing {each}')

    # https://docs.python.org/3/tutorial/inputoutput.html


# https://www.geeksforgeeks.org/python-string-interpolation/

"""
https://www.geeksforgeeks.org/string-formatting-in-python/?ref=rp

There are four different ways to perform string formatting in Python:
1. Formatting with % Operator.
2. Formatting with format() string method.
3. Formatting with string literals, called f-strings.
4. Formatting with String Template Class

1. METHOD 1:
% – Formatting
% – Formatting is a feature provided by Python which can be accessed with a % operator. This is similar to printf style function in C.

https://www.geeksforgeeks.org/string-formatting-in-python-using/

%d – integer %f – float %s – string %x – hexadecimal %o – octal 

Another useful Type Specifying 
%u unsigned decimal integer
%o octal integer
f – floating-point display
b – binary number
o – octal number
%x – hexadecimal with lowercase letters after 9
%X– hexadecimal with uppercase letters after 9
e – exponent notation

Example: Formatting string using % operator
"""

# Python program to demonstrate the use of formatting using %
 
# Initialize variable as a string
variable = '15'
string = "Variable as string = %s" %(variable)
print (string )
 
# Printing as raw data
# Thanks to Himanshu Pant for this
print ("Variable as raw data = %r" %(variable))
 
# Convert the variable to integer
# And perform check other formatting options
 
variable = int(variable) # Without this the below statement
                        # will give error.
string = "Variable as integer = %d" %(variable)
print (string)
print ("Variable as float = %f" %(variable))
 
# printing as any string or char after a mark
# here i use mayank as a string
print ("Variable as printing with special char = %c" %(variable))
 
print ("Variable as hexadecimal = %x" %(variable))
print ("Variable as octal = %o" %(variable))

"""
Output : 

Variable as string = 15
Variable as raw data = '15'
Variable as integer = 15
Variable as float = 15.000000
Variable as printing with special char = mayank
Variable as hexadecimal = f
Variable as octal = 17

# Python program to demonstrate
# string interpolation
""" 
# https://www.geeksforgeeks.org/python-string-format-method/
# Using %s – string conversion via str() prior to formatting
print("%20s" % ('geeksforgeeks', ))
print("%-20s" % ('Interngeeks', ))
print("%.5s" % ('Interngeeks', ))

"""
Output:

geeksforgeeks
Interngeeks         
Inter
"""
print("begin %20s end" % ('geeksforgeeks', ))
print("testing %-20s end" % ('Interngeeks', ))
print("begin with %.5s end here" % ('Interngeeks', ))

print("begin %20s end" % ('geeksforgeeks'))
print("testing %-20s end" % ('Interngeeks'))
print("begin with %.5s end here" % ('Interngeeks'))

print("begin %2s end" % ('geeksforgeeks', ))
print("testing %-2s end" % ('Interngeeks', ))
print("begin with %5s end here" % ('Interngeeks', ))

n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# for single substitution
print("Welcome to % s" % n2)
 
# for single and multiple substitutions()
# mandatory
print("% s ! This is % s." % (n1, n2))

"""
Output
Welcome to GeeksforGeeks
Hello ! This is GeeksforGeeks.

Let’s say it’s just a complicated version, but we can use it if we have a lot of variables to get substituted in the string as we don’t always want to use(“string” + variable + “string” + variable + variable + “string”) this representation. So for this purpose, we can go with %-formatting.

2. METHOD 2:
Str.format()
str.format()work by putting in one or more replacement fields and placeholders defined by a pair of curly braces { } into a string. The value we wish to put into the placeholders and concatenate with the string passed as parameters into the format function. 

https://www.geeksforgeeks.org/python-string-format-method/

Example: Formatting strings using format() method
"""

# Python program to demonstrate
# string interpolation
 
 
n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# for single substitution
print('{}, {}'.format(n1, n2))

"""
Output
Hello, GeeksforGeeks

We can also use the variable name inside the curly braces {}. This will allow us to use the parameters of format functions in any order we want.
Example: Format functions with variables inside curly braces.

The type can be used with format codes:

‘d’ for integers
‘f’ for floating-point numbers
‘b’ for binary numbers
‘o’ for octal numbers
‘x’ for octal hexadecimal numbers
‘s’ for string
‘e’ for floating-point in an exponent format
"""
print('The valueof pi is: %1.5f' %3.141592)
# vs.
print('The valueof pi is: {0:1.5f}'.format(3.141592))

"""
Output:

The valueof pi is: 3.14159
The valueof pi is: 3.14159
"""
# vs.
num = 3.14159
print(f"The valueof pi is: {num:{1}.{5}}")


print("This site is {0:f}% securely {1}!!".
      format(100, "encrypted"))
 
# To limit the precision
print("My average of this {0} was {1:.2f}%"
      .format("semester", 78.234876))
 
# For no decimal places
print("My average of this {0} was {1:.0f}%"
      .format("semester", 78.234876))
# vs.
print("My average of this %s was %.2f"
      % ("semester", 78.234876))
 
# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
      .format("binary", 100))
 
print("The {0} of 100 is {1:o}"
      .format("octal", 100))

txt = "I have {an:.2f} Ruppes!"
print(txt.format(an = 4))   # I have 4.00 Ruppes!

# using format option in a simple string
print("{}, A computer science portal for geeks."
      .format("GeeksforGeeks"))
 
# using format option for a
# value stored in a variable
str = "This article is written in {}"
print(str.format("Python"))
 
# formatting a string using a numeric constant
print("Hello, I am {} years old !".format(18))


# Multiple placeholders in format() function
my_string = "{}, is a {} science portal for {}"
print(my_string.format("GeeksforGeeks", "computer", "geeks"))
 
# different datatypes can be used in formatting
print("Hi ! My name is {} and I am {} years old"
      .format("User", 19))
 
# The values passed as parameters
# are replaced in order of their entry
print("This is {} {} {} {}"
      .format("one", "two", "three", "four"))

# parameters in format function.
my_string = "{}, is a {} {} science portal for {}"
 
try:
    print(my_string.format("GeeksforGeeks", "computer", "geeks"))
except IndexError as ie:
    print(ie, "Python program demonstrating Index error number of placeholders is four but there are only three values passed.")

"""
Formatting Strings using Escape Sequences
You can use two or more specially designated characters within a string to format a string or perform a command. These characters are called escape sequences. An Escape sequence in Python starts with a backslash (\). For example, \n is an escape sequence in which the common meaning of the letter n is literally escaped and given an alternative meaning – a new line.

Escape sequence	Description    	 Example      
\n	Breaks the string into a new line	print(‘I designed this rhyme to explain in due time\nAll I know’)
\t	Adds a horizontal tab	print(‘Time is a \tvaluable thing’)
\\	Prints a backslash	print(‘Watch it fly by\\as the pendulum swings’)
\’   	Prints a single quote	print(‘It doesn\’t even matter how hard you try’)
\”   	 Prints a double quote	print(‘It is so\”unreal\”‘)
\a	makes a sound like a bell	print(‘\a’) 
"""
print('I designed this rhyme to explain in due time\nAll I know')
print('Time is a \tvaluable thing')
print('Watch it fly by\\as the pendulum swings')
print('It doesn\’t even matter how hard you try')
print('It is so\”unreal\”')
print('\a') 

# >>>>>>>>> KRISTY trying double quotes <<<<<<<<<<<<<<<

print("I designed this rhyme to explain in due time\nAll I know")
print("Time is a \tvaluable thing")
print("Watch it fly by\\as the pendulum swings")
print("It doesn\’t even matter how hard you try")
print("It is so\”unreal\”")
print("\a") 

print(r'I designed this rhyme to explain in due time\nAll I know')
print(r'Time is a \tvaluable thing')
print(r'Watch it fly by\\as the pendulum swings')
print(r'It doesn\’t even matter how hard you try')
print(r'It is so\”unreal\”')
print(r'\a') 

print(s1 := r'\n dkfjdkfjskdfj')
print(s1 := r"\n dkfjdkfjskdfj")

# print(s1 := r''\n dkfjdkfjskdfj'')
"""
line 149              
SyntaxError: unexpected character after line continuation character
"""
# print(s1 := r""\n dkfjdkfjskdfj""")
"""
line 155
SyntaxError: unexpected character after line continuation character
"""
               
print(s1 := r'''\n dkfjdkfjskdfj''')
print(s1 := r"""\n dkfjdkfjskdfj""")
"""
\n dkfjdkfjskdfj
\n dkfjdkfjskdfj
"""

# s = r'Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'
# note: a semicolon inside a quoted string, a quote is escaped using a backslash, \n escape is used, both single and double quotes are used)
s = r'''Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"'''
print(s)
print(res := dict(item.split("=", 1) if len(item.split("=", 1)) == 2 else [item, None] for item in s.split(";")))
# from collections import defaultdict
# res = defaultdict()  # defaultdict doesn't help with the issue of ValueError: dictionary update sequence element #4 has length 1; 2 is required
# print(res := dict(item.split("=", 1) for item in s.split(";")))
"""
Output:
Name1='Value=2';Name2=Value2;Name3=Value3;Name4="Va\"lue;\n3"
{'Name1': "'Value=2'", 'Name2': 'Value2', 'Name3': 'Value3', 'Name4': '"Va\\"lue', '\\n3"': None}

Note: made posible due to triple quotes around the raw string!!!
https://www.codevscolor.com/python-raw-string
If there are an odd number of backslashes \ at the end of the text, an error will happen because backslashes escape the trailing ” or “. 
Note: Always use an even number of backslashes at the end of the text.
"""

# Positional arguments
# are placed in order
print("{0} love {1}!!".format("GeeksforGeeks",
                              "Geeks"))
 
# Reverse the index numbers with the
# parameters of the placeholders
print("{1} love {0}!!".format("GeeksforGeeks",
                              "Geeks"))
 
 
print("Every {} should know the use of {} {} programming and {}"
      .format("programmer", "Open", "Source",
              "Operating Systems"))
 
 
# Use the index numbers of the
# values to change the order that
# they appear in the string
print("Every {3} should know the use of {2} {1} programming and {0}"
      .format("programmer", "Open", "Source", "Operating Systems"))
 
 
# Keyword arguments are called
# by their keyword name
print("{gfg} is a {0} science portal for {1}"
      .format("computer", "geeks", gfg="GeeksforGeeks"))

"""
Output : 

GeeksforGeeks love Geeks!!

Geeks love GeeksforGeeks!!

Every programmer should know the use of Open Source programming and Operating Systems

Every Operating Systems should know the use of Source Open programming and programmer

GeeksforGeeks is a computer science portal for geeks
"""

"""
Padding Substitutions or Generating Spaces
Example: Demonstration of spacing when strings are passed as parameters
By default, strings are left-justified within the field, and numbers are right-justified. We can modify this by placing an alignment code just following the colon.

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
"""
# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("GeeksforGeeks", "geeks"))
 
# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format(40))
 
# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("GeeksforGeeks", 2009))
 
 
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:<16}!"
      .format("GeeksforGeeks", 2009))
 
print("{:*^20s}".format("Geeks"))

"""
Output : 

GeeksforGeeks, is the computer science portal for geeks   !
It is    40 degrees outside!
GeeksforGeeks was founded in             2009!
 GeeksforGeeks   was founded in 2009 !
*******Geeks********
"""

n1 = "Hello"
n2 = "GeeksForGeeks"
 
# for single or multiple substitutions
# let's say b1 and b2 are formal parameters
# and n1 and n2 are actual parameters
print("{b1}! This is {b2}.".format(b1=n1, b2=n2))
 
# we can also change the order of the
# variables in the string without changing
# the parameters of format function
print("{b2}! This is {b1}.".format(b1=n1, b2=n2))

"""
Output
Hello! This is GeeksForGeeks.
GeeksForGeeks! This is Hello.

3. METHOD 3:
f-strings
PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler. 

To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

Example: Formatting Strings using f-strings
"""

# Python program to demonstrate
# string interpolation
 
n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# f tells Python to restore the value of two
# string variable name and program inside braces {}
print(f"{n1}! This is {n2}")

"""
Output
Hello! This is GeeksforGeeks
(2 * 3)-10 = -4
We can also use f-strings to calculate some arithmetic operations and it will perform the inline arithmetic. See the below example – 

Example: Inline arithmetic using f-strings
"""
name = 'Ele'
print(f"My name is {name}.")
a = 5
b = 10
print(f"He said his age is {2 * (a + b)}.")
print(f"He said his age is {(lambda x: x*2)(3)}")
"""
He said his age is 30.
He said his age is 6
"""
num = 3.14159
print(f"The valueof pi is: {num:{1}.{5}}")
print(f"The valueof pi is: {num:1.5f}")
# vs.
print('The valueof pi is: %1.5f' %3.141592)
# vs.
print('The valueof pi is: {0:1.5f}'.format(3.141592))

"""
Output:

The valueof pi is: 3.1416
The valueof pi is: 3.14159
The valueof pi is: 3.14159
The valueof pi is: 3.14159
"""

# Prints today's date with help
# of datetime library
import datetime
 
today = datetime.datetime.today()
print(f"Today date is {today:%B %d, %Y}")
print(f"Month: {today:%B %Y}")
# vs.
print("Today date is {0:%B %d, %Y}".format(today))
print("Month: {0:%B %Y}".format(today))

"""
By default, the Python .format() method uses str(), but in some instances, you may want to force .format() 
to use one of the other two. You can do this with the <conversion> component of a replacement field. 
The possible values for <conversion> are shown in the table below:
https://realpython.com/python-formatted-output/

Value	Meaning
!s	Convert with str()
!r	Convert with repr()
!a	Convert with ascii()
The following examples force Python to perform string conversion using str(), repr(), and ascii(), respectively:
"""

'{0!s}'.format(42)
# '42'
'{0!r}'.format(42)
# '42'
'{0!a}'.format(42)
# '42'

"""
NOTES : Backslash Cannot be used in format string directly.
f"newline: {ord('\n')}"
Syntax Error: f-string expression part cannot include a backslash: , line 1, pos 0

But the documentation points out that we can put the backslash into a variable as a workaround though :
"""

newline = ord('\n')
print(f"newline: {newline}")

"""
Output : 

newline: 10
"""

a = 2
b = 3
c = 10
 
print(f"({a} * {b})-{c} = {(2 * 3)-10}")

"""
Output
(2 * 3)-10 = -4

4. METHOD 4:
String Template Class
In the String module, Template Class allows us to create simplified syntax for output specification. The format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). Surrounding the placeholder with braces allows it to be followed by more alphanumeric letters with no intervening spaces. Writing $$ creates a single escaped $:

https://www.geeksforgeeks.org/template-class-in-python/

Example: Formatting string using Template Class
"""

# Python program to demonstrate
# string interpolation
 
 
from string import Template
 
n1 = 'Hello'
n2 = 'GeeksforGeeks'
 
# made a template which we used to
# pass two variable so n3 and n4
# formal and n1 and n2 actual
n = Template('$n3 ! This is $n4.')
 
# and pass the parameters into the template string.
print(n.substitute(n3=n1, n4=n2))

"""
Output
Hello ! This is GeeksforGeeks.
"""

a = 1
b = 2
str1 = 'Kristy'
str2 = '130K'
makeupstr = Template('$person earned $salary last year!')

print('I want to do %d pushup(s)' % b)
print(f'but I can do only {a}')
print('maybe if I try hard, I can do {} instead of only {}'.format(b,a))
print('but my confident is so low; I keep thinking i can only do {x} instead of {y}'.format(x = a, y = b))
print('I want to do %d pushup(s)' % b, 'maybe if I try hard, I can do {} instead of only {}'.format(b,a), 
      'but my confident is so low; I keep thinking i can only do {x} instead of {y}'.format(x = a, y = b), 
      makeupstr.substitute(person = str1, salary = str2))
print(makeupstr.substitute(person = 'Kristy', salary = 130_000))

# https://docs.python.org/3/tutorial/inputoutput.html
print(yes_votes := 42_572_654)
print(no_votes := 43_132_495)
print(percentage := yes_votes / (yes_votes + no_votes))
print('There are {:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
print('There are {:9} YES votes  {:2.2%}'.format(yes_votes, percentage))

import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# The value of pi is approximately 3.142.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
    print('{:10s} ==> {:10d}'.format(name, phone))
"""
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""
    

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.')
# My hovercraft is full of 'eels'.

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
# Debugging bugs='roaches' count=13 area='living room'

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
# The story of Bill, Manfred, and Georg.

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))    # Jack: 4098; Sjoerd: 4127; Dcab: 8637678
print(table['Jack'])  # 4098
print(f"Jack: {table['Jack']}; Sjoerd: {table['Sjoerd']}; Dcab: {table['Dcab']}")  # Jack: 4098; Sjoerd: 4127; Dcab: 8637678


import json


print(json.dumps(table, indent=4, sort_keys=True))  # need to set indent value to get a beautiful display of dictionary
"""
{
    "Dcab": 8637678,
    "Jack": 4098,
    "Sjoerd": 4127
}
"""
sortedDic = json.dumps(table, sort_keys=True)
print(sortedDic)        # {"Dcab": 8637678, "Jack": 4098, "Sjoerd": 4127}

# https://www.geeksforgeeks.org/python-output-formatting/?ref=rp

# Python program to
# format a output using
# string() method
 
cstr = "I love geeksforgeeks"
   
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))

"""
Output: 
Center aligned string with fillchr: 
##########I love geeksforgeeks##########

The left aligned string is : 
I love geeksforgeeks--------------------

The right aligned string is : 
--------------------I love geeksforgeeks
"""

print('testing %5.2f' % 8.8282888888888)
print('testing %50.2f' % 8.8282888888888)
print('testing %10.2f' % 8.8282888888888)
"""
Output:
testing  8.83
testing                                               8.83
testing       8.83
"""
tmp = Template("f'testing {$piNumFloat:10.2f}'")  # this one already works
# tmp = Template(f'testing {$piNumFloat:10.2f}') # this one would send error: SyntaxError: f-string: invalid syntax
print('testing %10.2f' % math.pi)
print('testing {:10.2f}'.format(math.pi))
print(f'testing {math.pi:10.2f}')
print(f'testing {math.pi:{10}.{3}}')
print(eval(tmp.substitute(piNumFloat = math.pi)))
"""
Output:
testing       3.14
testing       3.14
testing       3.14
testing       3.14
testing       3.14
"""

# 543921.9354 becomes $543,921.94
# try: {{ "${:,.2f}".format(543921.9354) }}
print("testing ${:,.2f}".format(543921.9354))
# Output: testing $543,921.94

budget = Template('The $time budget for investment is $$$amount')
print(budget.substitute(time='monthly', amount='1,000.00'))
# 'The monthly budget for investment is $1,000.00'
# https://stackabuse.com/formatting-strings-with-the-python-template-class/

template = Template('[$exp for item in $coll]')
print(eval(template.substitute(exp='item ** 2', coll='[1, 2, 3, 4]')))
# [1, 4, 9, 16]
print(eval(template.substitute(exp='2 ** item', coll='[3, 4, 5, 6, 7, 8]')))
# [8, 16, 32, 64, 128, 256]
import math
print(eval(template.substitute(exp='math.sqrt(item)', coll='[9, 16, 25]')))
# [3.0, 4.0, 5.0]

from string import Template

_class_template = """
class ${klass}:
    def __init__(self, name):
        self.name = name

    def ${method}(self):
        print('Hi', self.name + ',', 'welcome to', '$site')
"""

template = Template(_class_template)
exec(template.substitute(klass='MyClass',
                         method='greet',
                         site='StackAbuse.com'))

obj = MyClass("John Doe")  
# Visual Studio complains that "'MyClass' is not defined", 
# but it's ok when we run test since we create this class in above test step
obj.greet()