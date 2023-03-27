# https://www.geeksforgeeks.org/conditional-decorators-in-python/?ref=rp

condition = True
  
def conditional_decorator(func):
      
    def wrapper():
        oldstring = func()
          
        if condition:
            newstring = oldstring.upper()
        else:
            newstring = oldstring.lower()
          
        return newstring
      
    return wrapper
  
@conditional_decorator
def func():
    return 'geeKSfoRGEEks'
  
print(func())

"""
Output:

'GEEKSFORGEEKS'
Method 2: In this, decorators are called only if a certain condition is met.

In the following program, the program takes user input to decide on the condition. If the user enters 1, the decorator is called and the string is returned in uppercase. If the user enters 2, again a decorator is called and the given string is returned in lowercase. Apart from this if any other number is entered the function is returned as it is without any modification.
"""

def decorator1(func):
      
    def wrapper():
        oldstring = func()
        newstring = oldstring.upper()
        return newstring
      
    return wrapper
  
def decorator2(func):
      
    def wrapper():
        oldstring = func()
        newstring = oldstring.lower()
        return newstring
      
    return wrapper
  
cond = 1
  
if cond == 1:
    @decorator1
    def func():
        return 'GeeksFORGeeKs'
elif cond == 2:
    @decorator2
    def func():
        return 'GeeksFORGeeKs'
else:
    def func():
        return 'GeeksFORGeeKs'
      
print(func())

"""
Output:

GEEKSFORGEEKS
"""
