# https://www.geeksforgeeks.org/inheritance-in-python/?ref=rp

"""
One of the core concepts in object-oriented programming (OOP) languages is inheritance. It is a mechanism that allows you to create a hierarchy of classes that share a set of properties and methods by deriving a class from another class. Inheritance is the capability of one class to derive or inherit the properties from another class. 

Benefits of inheritance are: 
It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Inheritance offers a simple, understandable model structure. 
Less development and maintenance expenses result from an inheritance. 
Python Inheritance Syntax
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
Creating a Parent Class
Creating a Person class with Display methods.
"""

# A Python program to demonstrate inheritance
 
class Person(object):
   
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
 
    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
 
 
# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

"""
Output:

Satyam 102
Creating a Child Class
Here Emp is another class which is going to inherit the properties of the Person class(base class).
"""

class Emp(Person):
   
    def Print(self):
        print("Emp class called")
     
Emp_details = Emp("Mayank", 103)
 
# calling parent class function
Emp_details.Display()
 
# Calling child class function
Emp_details.Print()

"""
Output:

Mayank 103
Emp class called
Example of Inheritance in Python 
"""

# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
 
class Person(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
    # To check if this person is an employee
    def isEmployee(self):
        return False
 
 
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
 
    # Here we return true
    def isEmployee(self):
        return True
 
 
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
 
emp = Employee("Geek2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())

"""
Output: 
Geek1 False
Geek2 True
What is object class?
Like the Java Object class, in Python (from version 3. x), the object is the root of all classes. 

In Python 3.x, “class Test(object)” and “class Test” are same. 
In Python 2. x, “class Test(object)” creates a class with the object as a parent (called a new-style class), and “class Test” creates an old-style class (without an objecting parent). 
Subclassing (Calling constructor of parent class)
A child class needs to identify which class is its parent class. This can be done by mentioning the parent class name in the definition of the child class. 

Eg: class subclass_name (superclass_name): 
"""

# Python code to demonstrate how parent constructors
# are called.
 
# parent class
class Person(object):
 
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
 
    def display(self):
        print(self.name)
        print(self.idnumber)
 
# child class
 
 
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
 
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
 
 
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")
 
# calling a function of the class Person using its instance
a.display()

"""
Output: 

Rahul
886012

‘a’ is the instance created for the class Person. It invokes the __init__() of the referred class. 
You can see ‘object’ written in the declaration of the class Person. In Python, every class inherits 
from a built-in basic class called ‘object’. The constructor i.e. the ‘__init__’ function of a class is invoked 
when we create an object variable or an instance of the class.
The variables defined within __init__() are called the instance variables or objects. 
Hence, ‘name’ and ‘idnumber’ are the objects of the class Person. Similarly, ‘salary’ and ‘post’ are 
the objects of the class Employee. Since the class Employee inherits from class Person, ‘name’ 
and ‘idnumber’ are also the objects of class Employee.

Python program to demonstrate error if we forget to invoke __init__() of the parent
If you forget to invoke the __init__() of the parent class then its instance variables would not be available to the child class. 

The following code produces an error for the same reason. 
"""

class Test1:
    def __init__(self, n):
        self.name = n
        print(' in parent class')
 
class Test2(Test1):
    def __init__(self, n, roll):
        Test1.__init__(self, n)
        self.roll = roll
        print(' in child class')

 
kristy = Test2('kristy', 23)
print(kristy.name)

"""
class A:
    def __init__(self, n='Rahul'):
        self.name = n
 
class B(A):
    def __init__(self, roll):
        self.roll = roll

try:
    object = B(23)
    print(object.name)
except AttributeError as err:
    print(err)



Output : Python program to demonstrate error if we forget to invoke __init__() of the parent (missing line 182)

Traceback (most recent call last):
  File "/home/de4570cca20263ac2c4149f435dba22c.py", line 12, in 
    print (object.name)
AttributeError: 'B' object has no attribute 'name'
Different types of Inheritance:
Single inheritance: When a child class inherits from only one parent class, it is called single inheritance. We saw an example above.
Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 
Unlike java, python shows multiple inheritances.
"""

# Python example to show the working of multiple
# inheritance
 
 
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")
 
 
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")
 
 
class Derived(Base1, Base2):
    def __init__(self):
 
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
 
    def printStrs(self):
        print(self.str1, self.str2)
 
 
ob = Derived()
ob.printStrs()

"""
Output: 

Base1
Base2
Derived
Geek1 Geek2
Multilevel inheritance: When we have a child and grandchild relationship. 
"""

# A Python program to demonstrate inheritance
 
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"
 
 
class Base(object):
 
    # Constructor
    def __init__(self, name):
        self.name = name
 
    # To get name
    def getName(self):
        return self.name
 
 
# Inherited or Sub class (Note Person in bracket)
class Child(Base):
 
    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
 
    # To get name
    def getAge(self):
        return self.age
 
# Inherited or Sub class (Note Person in bracket)
 
 
class GrandChild(Child):
 
    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
 
    # To get address
    def getAddress(self):
        return self.address
 
 
# Driver code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())

"""
Output: 

Geek1 23 Noida
Hierarchical inheritance More than one derived class are created from a single base.
Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than one type of inheritance.
For more details please read this article: Types of inheritance in Python

Private members of the parent class 
We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class. 
We can make an instance variable private by adding double underscores before its name. For example,
"""

# Python program to demonstrate private members
# of the parent class
 
 
class C(object):
    def __init__(self):
        self.c = 21
 
        # d is private instance variable
        self.__d = 42
 
 
class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)
 
 
object1 = D()
 
# produces an error as d is private instance variable
try:
     print(object1.d)
except AttributeError as err:
     print(err)

"""
Output : 

  File "/home/993bb61c3e76cda5bb67bd9ea05956a1.py", line 16, in 
    print (object1.d)                     
AttributeError: type object 'D' has no attribute 'd'
Since ‘d’ is made private by those underscores, it is not available to the child class ‘D’ and hence the error.
"""

# https://www.geeksforgeeks.org/inheritance-in-python-set-2/?ref=rp
# Python code to demonstrate issubclass()
class A():
      def __init__(self, a):
            self.a = a
class B(A):
      def __init__(self, a, b):
            self.b = b
            A.__init__(self, a)
  
print(issubclass(B, A))

# https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/?ref=rp
# Python code to demonstrate multiple inheritance
  
# first parent class
class Person(object):                  
      def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
  
# second parent class      
class Employee(object):                
      def __init__(self, salary, post):
            self.salary = salary
            self.post = post
  
# inheritance from both the parent classes      
class Leader(Person, Employee):        
      def __init__(self, name, idnumber, salary, post, points):
            self.points = points
            Person.__init__(self, name, idnumber)
            Employee.__init__(self, salary, post)  

# first parent class
class Person(object):                 
      def __init__(self, name, idnumber):
            self.name = name
            self.idnumber = idnumber
  
# second parent class      
class Employee(object):                
      def __init__(self, salary, post):
            self.salary = salary
            self.post = post
  
# inheritance from both the parent classes      
class Leader(Person, Employee):        
      def __init__(self, name, idnumber, salary, post, points):
            self.points = points
            Person.__init__(self, name, idnumber)
            Employee.__init__(self, salary, post)
            print(self.salary)
        
ins = Leader('Rahul', 882016, 'Assistant Manager', 75000, 560)

# Base Class
class A(object):                
        def __init__(self):
                constant1 = 1
        def method1(self):
                print('method1 of class A')
  
class B(A):
        def __init__(self):
                constant2 = 2
                self.calling1()
                A. __init__(self)
        def method1(self):
                print('method1 of class B')
        def calling1(self):
                self.method1()
                A.method1(self)
b = B()

class A(object):
        def function1(self):
                print('function of class A')
class B(A):
        def function1(self):
                print('function of class B')
                super(B, self).function1()
class C(B):
        def function1(self):
                print('function of class C') 
                super(C, self).function1()
j = C()
j.function1()

# A Python program to demonstrate inheritance 
  
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)"
class Person(object):
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
    # To check if this person is employee
    def isEmployee(self):
        return False
  
  
# Inherited or Sub class (Note Person in bracket)
class Employee(Person):
  
    # Here we return true
    def isEmployee(self):
        return True
  
# Driver code
emp = Person("Geek1")  # An Object of Person
print(emp.getName(), emp.isEmployee())
  
emp = Employee("Geek2") # An Object of Employee
print(emp.getName(), emp.isEmployee())

"""
Output:
('Geek1', False)
('Geek2', True)
"""

# Python example to check if a class is
# subclass of another
  
class Base(object):
    pass   # Empty Class
  
class Derived(Base):
    pass   # Empty Class
  
# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))
  
d = Derived()
b = Base()
  
# b is not an instance of Derived
print(isinstance(b, Derived))
  
# But d is an instance of Base
print(isinstance(d, Base))

"""
Output:
True
False
False
True
"""

# Python example to show working of multiple 
# inheritance
class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1") 
  
class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"        
        print("Base2") 
  
class Derived(Base1, Base2):
    def __init__(self):
          
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived") 
          
    def printStrs(self):
        print(self.str1, self.str2)
         
  
ob = Derived()
ob.printStrs()

"""
Output:
Base1
Base2
Derived
('Geek1', 'Geek2')


How to access parent members in a subclass?

Using Parent class name
"""

# Python example to show that base
# class members can be accessed in
# derived class using base class name
class Base(object):
  
    # Constructor
    def __init__(self, x):
        self.x = x    
  
class Derived(Base):
  
    # Constructor
    def __init__(self, x, y):
        Base.x = x 
        self.y = y
  
    def printXY(self):
       
       # print(self.x, self.y) will also work
       print(Base.x, self.y)
  
  
# Driver Code
d = Derived(10, 20)
d.printXY()

"""
Output:
(10, 20)
Using super()
We can also access parent class members using super.
"""

# Python example to show that base
# class members can be accessed in
# derived class using super()
class Base(object):
  
    # Constructor
    def __init__(self, x):
        self.x = x    
  
class Derived(Base):
  
    # Constructor
    def __init__(self, x, y):
          
        ''' In Python 3.x, "super().__init__(name)"
            also works''' 
        super(Derived, self).__init__(x)
        self.y = y
  
    def printXY(self):
  
       # Note that Base.x won't work here
       # because super() is used in constructor
       print(self.x, self.y)
  
  
# Driver Code
d = Derived(10, 20)
d.printXY()

"""
Output:
(10, 20)
Note that the above two methods are not exactly the same. In the next article on inheritance, we will covering following topics.
1) How super works? How accessing a member through super and parent class name are different?
2) How Diamond problem is handled in Python?

 

Exercise:
Predict the output of following Python programs
"""
  
class X(object):
    def __init__(self, a):
        self.num = a
    def doubleup(self):
        self.num *= 2
  
class Y(X):
    def __init__(self, a):
        X.__init__(self, a)
    def tripleup(self):
        self.num *= 3
  
obj = Y(4)
print(obj.num)
  
obj.doubleup()
print(obj.num)
  
obj.tripleup()
print(obj.num)

"""
Output:
4
8
24
"""

# Base or Super class
class Person(object):
    def __init__(self, name):
        self.name = name
          
    def getName(self):
        return self.name
      
    def isEmployee(self):
        return False
  
# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
    def __init__(self, name, eid):
  
        ''' In Python 3.0+, "super().__init__(name)"
            also works''' 
        super(Employee, self).__init__(name)
        self.empID = eid
          
    def isEmployee(self):
        return True
          
    def getID(self):
        return self.empID
  
# Driver code
emp = Employee("Geek1", "E101") 
print(emp.getName(), emp.isEmployee(), emp.getID())

"""
Output:
('Geek1', True, 'E101')
"""

# https://www.geeksforgeeks.org/python-super/
# Example of super() function in Python
class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add
 
# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails
 
Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "KKK@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)

"""
Output:

The ID is: 103
The Name is: Suraj kr gupta
The Address is: Noida
The Emails is: KKK@gmails
Solving the first problem using super
"""

# code
# A Python program to demonstrate inheritance

class Person:
 
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
 
    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
     
 
class Emp(Person):
     
    def __init__(self, name, id):
        self.name_ = name
        super().__init__(name, id)
 
    def Print(self):
        print("Emp class called")
 
Emp_details = Emp("Mayank", 103)
 
# calling parent class function
print(Emp_details.name_, Emp_details.name)

"""
Output
Mayank Mayank
"""

# Python program to demonstrate
# super function
 
class Animals:
    # Initializing constructor
    def __init__(self):
        self.legs = 4
        self.domestic = True
        self.tail = True
        self.mammals = True
 
    def isMammal(self):
        if self.mammals:
            print("It is a mammal.")
 
    def isDomestic(self):
        if self.domestic:
            print("It is a domestic animal.")
 
class Dogs(Animals):
    def __init__(self):
        super().__init__()
 
    def isMammal(self):
        super().isMammal()
 
class Horses(Animals):
    def __init__(self):
        super().__init__()
 
    def hasTailandLegs(self):
        if self.tail and self.legs == 4:
            print("Has legs and tail")
 
# Driver code
Tom = Dogs()
Tom.isMammal()
Bruno = Horses()
Bruno.hasTailandLegs()

"""
Output:
It is a mammal.
Has legs and tail

Super function in multiple inheritances
Let’s take another example of a super function, Suppose a class canfly and canswim inherit from a mammal class and these classes are inherited by the animal class. So the animal class inherits from the multiple base classes. Let’s see the use of Python super with arguments in this case
"""

class Mammal():
 
    def __init__(self, name):
        print(name, "Is a mammal")
 
class canFly(Mammal):
 
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")
 
        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)
 
class canSwim(Mammal):
 
    def __init__(self, canSwim_name):
 
        print(canSwim_name, "cannot swim")
 
        super().__init__(canSwim_name)
 
class Animal(canFly, canSwim):
 
    def __init__(self, name):
        super().__init__(name)
 
# Driver Code
Carol = Animal("Dog")

"""
Output:

The class Animal inherits from two-parent classes – canFly and canSwim. So, the subclass instance Carol can access both of the parent class constructors. 

Dog cannot fly
Dog cannot swim
Dog Is a mammal

MRO in Multiple Inheritance
"""

class A:
    def age(self):
        print("Age is 21")
class B:
    def age(self):
        print("Age is 23")
class C(A, B):
    def age(self):
        super(C, self).age()
     
c = C()
print(C.__mro__)
print(C.mro())

"""
Output:

(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
Multi-Level inheritance
Let’s take another example of a super function, suppose a class canSwim is inherited by canFly, canFly from mammal class. So the mammal class inherits from the Multi-Level inheritance. Let’s see the use of Python super with arguments in this case
"""

class Mammal():
 
    def __init__(self, name):
        print(name, "Is a mammal")
 
 
class canFly(Mammal):
 
    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")
 
        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)
 
 
class canSwim(canFly):
 
    def __init__(self, canSwim_name):
 
        print(canSwim_name, "cannot swim")
 
        super().__init__(canSwim_name)
 
 
class Animal(canSwim):
 
    def __init__(self, name):
 
        # Calling the constructor
        # of both the parent
        # class in the order of
        # their inheritance
        super().__init__(name)
 
 
# Driver Code
Carol = Animal("Dog")

"""
Output:

Dog cannot swim
Dog cannot fly
Dog Is a mammal
"""

# https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/?ref=rp
# Program to define the use of super()
# function in multiple inheritance
class GFG1:
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG1)')
  
    def sub_GFG(self, b):
        print('Printing from class GFG1:', b)
  
# class GFG2 inherits the GFG1
class GFG2(GFG1):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG2)')
        super().__init__()
  
    def sub_GFG(self, b):
        print('Printing from class GFG2:', b)
        super().sub_GFG(b + 1)
  
# class GFG3 inherits the GFG1 ang GFG2 both
class GFG3(GFG2):
    def __init__(self):
        print('HEY !!!!!! GfG I am initialised(Class GEG3)')
        super().__init__()
  
    def sub_GFG(self, b):
        print('Printing from class GFG3:', b)
        super().sub_GFG(b + 1)
  
  
# main function
if __name__ == '__main__':
  
    # created the object gfg
    gfg = GFG3()
  
    # calling the function sub_GFG3() from class GHG3
    # which inherits both GFG1 and GFG2 classes
    gfg.sub_GFG(10)

"""
Output:
HEY !!!!!! GfG I am initialised(Class GEG3)
HEY !!!!!! GfG I am initialised(Class GEG2)
HEY !!!!!! GfG I am initialised(Class GEG1)
Printing from class GFG3: 10
Printing from class GFG2: 11
Printing from class GFG1: 12
"""
