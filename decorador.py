# https://www.geeksforgeeks.org/decorators-in-python/

"""
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.

First Class Objects
In Python, functions are first class objects which means that functions in Python can be used or passed as arguments.
Properties of first class functions:
A function is an instance of the Object type.
You can store the function in a variable.
You can pass the function as a parameter to another function.
You can return the function from a function.
You can store them in data structures such as hash tables, lists, …
Consider the below examples for better understanding.

Example 1: Treating the functions as objects. 
"""

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))

"""
In the above example, we have assigned the function shout to a variable. This will not call the function instead it takes the function object referenced by a shout and creates a second name pointing to it, yell.

Example 2: Passing the function as an argument 
"""

# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)

"""
In the above example, the greet function takes another function as a parameter (shout and whisper in this case). The function passed as an argument is then called inside the function greet.

Example 3: Returning functions from another function.
"""

# Python program to illustrate functions
# Functions can return another function
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))

"""
In the above example, we have created a function inside of another function and then have returned the function created inside.
The above three examples depict the important concepts that are needed to understand decorators. After going through them let us now dive deep into decorators.

Decorators
As stated above the decorators are used to modify the behaviour of function or class. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

Syntax for Decorator: 

@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")    
hello_decorator = gfg_decorator(hello_decorator)'''

In the above code, gfg_decorator is a callable function, that will add some code on the top of some another callable function, hello_decorator function and return the wrapper function.

Decorator can modify the behaviour:  
"""

# defining a decorator
def hello_decorator(func):
 
    # inner1 is a Wrapper function in
    # which the argument is called
     
    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")
 
        # calling the actual function now
        # inside the wrapper function.
        func()
 
        print("This is after function execution")
         
    return inner1
 
 
# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")
 
 
# passing 'function_to_be_used' inside the
# decorator to control its behaviour
function_to_be_used = hello_decorator(function_to_be_used)
 
 
# calling the function
function_to_be_used()

"""
Output: 

Hello, this is before function execution
This is inside the function !!
This is after function execution
Let’s see the behaviour of the above code and how it runs step by step when the “function_to_be_used” is called.

Let’s jump to another example where we can easily find out the execution time of a function using a decorator.
"""

# importing libraries
import time
import math
 
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
     
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
 
        # storing time before function execution
        begin = time.time()
         
        func(*args, **kwargs)
 
        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
 
    return inner1
 
 
 
# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
 
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))
 
# calling the function.
factorial(10)

"""
Output: 

3628800
Total time taken in :  factorial 2.0061802864074707
What if a function returns something or an argument is passed to the function?
In all the above examples the functions didn’t return anything so there wasn’t an issue, but one may need the returned value.
"""

def hello_decorator(func):
    def inner1(*args, **kwargs):
         
        print("before Execution")
         
        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")
         
        # returning the value to the original frame
        return returned_value
         
    return inner1
 
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
 
a, b = 1, 2
 
# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

"""
Output: 

before Execution
Inside the function
after Execution
Sum = 3
In the above example, you may notice a keen difference in the parameters of the inner function. The inner function takes the argument as *args and **kwargs which means that a tuple of positional arguments or a dictionary of keyword arguments can be passed of any length. This makes it a general decorator that can decorate a function having any number of arguments.

Chaining Decorators
In simpler terms chaining decorators means decorating a function with multiple decorators.

Example: 
"""

# code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
@decor
@decor1
def num2():
    return 10
   
print(num())
print(num2())

"""
Output:

400
200
The above example is similar to calling the function as –
"""
decor1(decor(num))
decor(decor1(num2))

"""
https://www.geeksforgeeks.org/useful-cases-to-illustrate-decorators-in-python/?ref=rp

A decorator is a special kind of function that either takes a function and returns a function or takes a class and returns a class. Well, it can be any callable (i.e functions, classes, methods as they can be called) and it can return anything, it can also take a method. This is also called metaprogramming, as a part of the program tries to modify another part of the program at compile time.
Let’s dive into python decorators and find out what they can do. This will not be covering the basics or decorators with parameters, but some useful examples to illustrate the case.

Basically, a decorator takes in a callable, any object which implements the special method __call()__ is termed as callable, adds some functionality and returns a callable.

Example 1:
"""
# Python program to demonstrate
# decorators
  
  
# Creating a decorator
def decorated_func(func):
    def inner():
        print("This is decorated function")
        func()
    return inner()
  
  
def ordinary_func ():
    print("This is ordinary function")
  
decorated = decorated_func(ordinary_func)
decorated

"""
Output:

This is decorated function
This is ordinary function
In the example shown above, decorated_func() is a decorator. In short, a decorator acts as a wrapper that wraps an object (does not alter the original object) and adds an new functionality to original object. This is a common construct, so Python has a syntax feature (called Decorator) to simplify this. For example,

This:
@decorated_func
def ordinary_func():
     print("This is ordinary function")
is Equivalent to:

def ordinary_func():
    print("This is ordinary function")
decorated = decorated_func(ordinary_func)

A simple example would be:

Example 2:
Input:
"""
def mul_decorator(func):
    def wrapper(*args, **kwargs):
        print('function', func.__name__, 'called with args - ', 
              args, 'and kwargs - ', kwargs)
        result = func(*args, **kwargs)
        print('function', func.__name__, 'returns', result)
        return result
    return wrapper
  
  
@mul_decorator
def mul(a, b):
    return a * b
mul(3, 3)
mul(3, b = 6)

"""
Output:

function mul called with args -  (3, 3) and kwargs -  {}
function mul returns 9
function mul called with args -  (3,) and kwargs -  {'b': 6}
function mul returns 18

You can also use the built-ins as decorators

Example 3:
"""
# func will be func = type(func) -> <class 'function'>
@type
def func(): 
    return 42
  
print(func)
  
# print doesn't return anything, so func == None
@print
def func2(): 
    return 42
  
# Prints None
print(func2)

"""
Output:

<class 'function'>
<function func2 at 0x7f135f067f28>
None
You can replace decorated object with something else

Example 4:
"""

# Creating a decorator
class function_1:
    def __init__(self, func):
        self.func = func
        self.stats = []
  
    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            self.stats.append((args, kwargs, e))
            raise e
        else:
            self.stats.append((args, kwargs, result))
            return result
  
    @classmethod
    def function_2(cls, func):
        return cls(func)
  
  
@function_1.function_2
def func(x, y):
    return x / y
  
print(func(6, 2))
  
print(func(x = 6, y = 4))
  
try:
    func(5, 0)
    print(func.stats)
    print(func)
except ZeroDivisionError as err:
    print(f'{err}')

"""
Output:

3.0
1.5
Traceback (most recent call last):
  File "/home/1ba974e44c61e303979b3ee120b6b066.py", line 29, in 
    func(5, 0)
  File "/home/1ba974e44c61e303979b3ee120b6b066.py", line 11, in __call__
    raise e
  File "/home/1ba974e44c61e303979b3ee120b6b066.py", line 8, in __call__
    result = self.func(*args, **kwargs)
  File "/home/1ba974e44c61e303979b3ee120b6b066.py", line 23, in func
    return x / y
ZeroDivisionError: division by zero

Notice how the original "func" was replaced by an instance of "function_1", which can be used in the same way as the original function.
You can create relation with other objects in system

Example 5:
"""

def dict_from_func(func):
    return {func.__name__: func}
  
  
activity = {}
  
@activity.update
@dict_from_func
def mul(a, b):
    return a * b
  
  
@activity.update
@dict_from_func
def add(a, b):
    return a + b
  
  
print(mul)
print(activity)
print(activity['mul'](2, 5))

"""
Output:

None
{'mul': <function mul at 0x7f0d2209fe18>, 
 'add': <function add at 0x7f0d220a2158>}
10

Here, in the example 5, we have used dict.update method as a decorator, even if it is not intended for this. This, is possible because dict_from_func returns a dict, and dict.update takes a dict as an argument.

Actually, This:

@activity.update
@dict_from_func
def mul(a, b):
    return a * b

# Equals this –

def mul(a, b):
    return a * b
mul = activity.update(dict_from_func(mul))

Conclusion
Decorators is an interesting and amazing feature and can be used for variety of purposes. It’s not just “function or class that takes function or a class and returns a function or a class”.
"""

# https://www.geeksforgeeks.org/decorator-to-print-function-call-details-in-python/?ref=rp
# Decorator to print Function call details in Python

"""
Decorators in Python are the design pattern that allows the users to add new functionalities to an existing object 
without the need to modify its structure. Decorators are generally called before defining a function the user wants to decorate.

Example:
"""

# defining a decorator 
def hello_decorator(func): 
    
    # inner1 is a Wrapper function in  
    # which the argument is called 
        
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
    
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
    
        print("This is after function execution") 
            
    return inner1 
    
    
# defining a function, to be called inside wrapper 
def function_to_be_used(): 
    print("This is inside the function !!") 
    
    
# passing 'function_to_be_used' inside the 
# decorator to control its behavior 
function_to_be_used = hello_decorator(function_to_be_used) 
    
    
# calling the function 
function_to_be_used() 

"""
Output:
Hello, this is before function execution
This is inside the function !!
This is after function execution
"""

@hello_decorator
def function_to_be_used(): 
    print("This is inside the function !!") 
    
# calling the function 
function_to_be_used() 
"""
Output:
Hello, this is before function execution
This is inside the function !!
This is after function execution
"""