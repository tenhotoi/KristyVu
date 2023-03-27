# https://www.w3schools.com/python/python_classes.asp

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

print('=======================================================================')
class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person1("John", 36)

print(p1.name)
print(p1.age)

print('=======================================================================')
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person2("John", 36)

print(p1)

print('=======================================================================')
class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person3("John", 36)

print(p1)

print('=======================================================================')
class Person4:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person4("John", 36)
p1.myfunc()

print('=======================================================================')
# Use the words mysillyobject and abc instead of self:
class Person5:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person5("John", 36)
p1.myfunc()

# Set the age of p1 to 40:
p1.age = 40

# Delete the age property from the p1 object:
del p1.age

# Delete the p1 object:
del p1

print('=======================================================================')
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass

# https://www.geeksforgeeks.org/class-method-vs-static-method-python/?ref=rp
# One simple Example :
# class method:
class MyClass:
    def __init__(self, value):
        self.value = value
 
    def get_value(self):
        return self.value
 
# Create an instance of MyClass
obj = MyClass(10)
 
# Call the get_value method on the instance
print(obj.get_value())  # Output: 10

# Static method:-
class MyClass:
    def __init__(self, value):
        self.value = value
 
    @staticmethod
    def get_max_value(x, y):
        return max(x, y)
 
# Create an instance of MyClass
obj = MyClass(10)
 
print(MyClass.get_max_value(20, 30)) 
print(obj.get_max_value(20, 30))

# ==========================================================================================
# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))

# https://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/?ref=rp
# Python program to show that the variables with a value
# assigned in class declaration, are class variables

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "Geek"
print(b.name) # prints "Nerd"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"

# Now if we change the stream for just a it won't be changed for b
# a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

# To change the stream for all instances of the class we can change it 
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'ece'
print(b.stream) # prints 'mech'

# ====================================================================================
class MyClass:
    static_var = 0
 
    def __init__(self):
        MyClass.static_var += 1
        self.instance_var = MyClass.static_var
 
obj1 = MyClass()
print(obj1.instance_var)  # Output: 1
print(obj1.static_var)  
print(MyClass.static_var)  

obj2 = MyClass()
print(obj2.instance_var)  # Output: 2
print(obj2.static_var)  
print(MyClass.static_var)  # Output: 2

obj3 = MyClass()
print(obj3.instance_var)  
print(obj3.static_var)  
print(MyClass.static_var)  

"""
Consider the case where we want a class to behave like a list. For
example, we’d like to be able to append to the list and access items by
their index, but we don’t want any of the other list stuff. In this case, it
would be wrong to use inheritance. Instead, we would make our class store
a list internally (composition). Then, the public interface to our class would
contain the methods we want while making calls to the stored list instance
to avoid duplicating the list implementation. Here is an example.
"""
class MyLimitedList:
  def __init__(self):
    self._L = []
  def append(self, item):
    self._L.append(item)
  
  def __getitem__(self, index):
    return self._L[index]

"""
Here, the magic method getitem will allow us to use the square
bracket notation with our class. As with other magic methods, we don’t call
it directly.
"""
L = MyLimitedList()
L.append(1)
L.append(10)
L.append(100)
print(L[2])

class Doubler:
  def __init__(self, n):
    self._n = 2 * n

  def n(self):
    return self._n

if __name__ == '__main__':
  x = Doubler(5)
  assert(x.n() == 10)
  y = Doubler(-4)
  assert(y.n() == -8)

import unittest
from dayoftheweek import DayOfTheWeek
class TestDayOfTheWeek(unittest.TestCase):
  def testinitwithabbreviation(self):
    d = DayOfTheWeek('F')
    self.assertEquals(d.name(), 'Friday')
    d = DayOfTheWeek('Th')
    self.assertEquals(d.name(), 'Thursday')

unittest.main()

