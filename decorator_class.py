# Class as decorator in python

"""
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 
We can define a decorator as a class in order to do that, we have to use a __call__ method of classes. When a user needs to create an object that acts as a function then function decorator needs to return an object that acts like a function, so __call__ can be useful. For Example 
""" 

# Python program showing
# use of __call__() method
 
class MyDecorator:
    def __init__(self, function):
        self.function = function
     
    def __call__(self):
 
        # We can add some code
        # before function call
 
        self.function()
 
        # We can also add some code
        # after function call.
 
 
# adding class decorator to the function
@MyDecorator
def function():
    print("GeeksforGeeks")
 
function()

"""
Output: 
GeeksforGeeks
 
Class Decorator with *args and **kwargs : 
In order to use class decorator with argument *args and **kwargs we used a __call__ function and passed both the argument in a given function 
"""

# Python program showing
# class decorator with *args
# and **kwargs
 
class MyDecorator:
    def __init__(self, function):
        self.function = function
     
    def __call__(self, *args, **kwargs):
 
        # We can add some code
        # before function call
 
        self.function(*args, **kwargs)
 
        # We can also add some code
        # after function call.
     
 
# adding class decorator to the function
@MyDecorator
def function(name, message ='Hello'):
    print("{}, {}".format(message, name))
 
function("geeks_for_geeks", "hello")

"""
Output: 
hello, geeks_for_geeks
   
Class Decorator with return statement : 
In the given example the functions did not return anything so there is not any issue, but one may need the returned value. So we use return statement with the class decorator. 
"""

# Python program showing
# class decorator with
# return statement
 
class SquareDecorator:
 
    def __init__(self, function):
        self.function = function
 
    def __call__(self, *args, **kwargs):
 
        # before function
        result = self.function(*args, **kwargs)
 
        # after function
        return result
 
 # adding class decorator to the function
@SquareDecorator
def get_square(n):
    print("given number is:", n)
    return n * n
 
print("Square of number is:", get_square(195))

"""
Output: 
given number is: 195
Square of number is: 38025
   
Using class Decorators to print Time required to execute a program : 
In order to print time required to execute a program, we use __call__ function and use a time module so that we can get a execute time of a program 
"""

# Python program to execute
# time of a program
 
# importing time module
from time import time
class Timer:
 
    def __init__(self, func):
        self.function = func
 
    def __call__(self, *args, **kwargs):
        start_time = time()
        result = self.function(*args, **kwargs)
        end_time = time()
        print("Execution took {} seconds".format(end_time-start_time))
        return result
 
 
# adding a decorator to the function
@Timer
def some_function(delay):
    from time import sleep
 
    # Introducing some time delay to
    # simulate a time taking function.
    sleep(delay)
 
some_function(3)

"""
Output: 
Execution took 3.003122091293335 seconds
  
Checking error parameter using class decorator : 
This type of class decorator is most frequently used. This decorator checks parameters before executing the function preventing the function to become overloaded and enables it to store only logical and necessary statements.
"""
# Python program checking
# error parameter using
# class decorator
 
class ErrorCheck:
 
    def __init__(self, function):
        self.function = function
 
    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError("parameter cannot be a string !!")
        else:
            return self.function(*params)
 
@ErrorCheck
def add_numbers(*numbers):
    return sum(numbers)

#  returns 6
print(add_numbers(1, 2, 3))

try: 
    # raises Error. 
    print(add_numbers(1, '2', 3)) 
except TypeError as err:
    print(err)

"""
Output : 
 
6
TypeError: parameter cannot be a string !!

# https://www.geeksforgeeks.org/creating-decorator-inside-a-class-in-python/?ref=rp
Creating Decorator inside a class in Python
We can easily create decorators inside a class and it is easily accessible for its child classes. During Decorator creation, we must take care that the function that we are defining inside the decorator must take current object reference (self) as a parameter, and while we are accessing that decorator from child class that time we must call that decorator using the class name(class in which Decorator is present).

Example 1: Here in this example we are creating a decorator function inside Class A. Inside Class A “fun1” Instance Method is calling the decorator function “Decorators” inside Class B “fun2”. Instance Method is calling the decorator function of Class A. To use the decorator of Class A, we must require using Class name in which decorator is present that’s why we use “@A.Decorators” here.
"""

# creating class A
class A :
    def Decorators(func) :
        def inner(self) :
            print('Decoration started.')
            func(self)
            print('Decoration of function completed.\n')
        return inner
  
    @Decorators
    def fun1(self) :
        print('Decorating - Class A methods.')
  
# creating class B
class B(A) :
    @A.Decorators
    def fun2(self) :
        print('Decoration - Class B methods.')
  
obj = B()
obj.fun1()
obj.fun2()

"""
Output:

Decoration started.
Decorating - Class A methods.
Decoration of function completed.

Decoration started.
Decoration - Class B methods.
Decoration of function completed.
Example 2: Checking number is Even or Odd using Decorator.
"""
class Check_no :   
    # decorator function
    def decor(func) :            
        def check(self, no) :
            func(self, no)
            if no % 2 == 0 :
                print('Yes, it\'s EVEN Number.')
            else :
                print('No, it\'s ODD Number.')
        return check
  
    @decor      
    #instance method
    def is_even(self, no) :            
        print('User Input : ', no)
  
obj = Check_no()
obj.is_even(45)
obj.is_even(2)
obj.is_even(7)

"""
Output:

User Input :  45
No, it's ODD Number.
User Input :  2
Yes, it's EVEN Number.
User Input :  7
No, it's ODD Number.
Example 3: Checking Grade from Marks.
"""

# parent class
class Student :            
    
    # decorator function
    def decor(func) :                
        def grade(self,marks) :
            func(self,marks)
            if marks < 35 :
                print('Grade : F')
            elif marks < 50 :
                print('Grade : E')
            elif marks < 60 :
                print('Grade : D')
            elif marks < 70 :
                print('Grade : C')
            elif marks < 80 :
                print('Grade : B')
            elif marks < 100 :
                print('Grade : A')
        return grade
  
# child class
class Result(Student) :            
    @Student.decor
      
    # instance method
    def result(self,marks) :            
        print('Your Score : ',marks)
  
# creating object of parent class
obj = Result()        
obj.result(89) 
obj.result(34)

"""
Output:

Your Score :  89
Grade : A
Your Score :  34
Grade : F
"""