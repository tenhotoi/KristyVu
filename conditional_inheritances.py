# https://www.geeksforgeeks.org/conditional-inheritance-in-python/?ref=rp

class A(object): 
    def __init__(self, x): 
        self.x = x
      
    def getX(self): 
        return self.X
    
class B(object): 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    def getSum(self): 
        return self.X + self.y
  
# inherits from A  
class C_A(A):
    def isA(self):
        return True
      
    def isB(self):
        return False
  
# inherits from B  
class C_B(B):
    def isA(self):
        return False
    
    def isB(self):
        return True
  
# return required Object of C based on cond  
def getC(cond):
    if cond:
        return C_A(1)
    else:
        return C_B(1,2)
  
# Object of C_A
ca = getC(True)
print(ca.isA())
print(ca.isB())  
    
# Object of C_B  
cb = getC(False)
print(cb.isA())
print(cb.isB())

"""
Output:

True
False
False
True

Example 2: For Either inheriting or not from A:

The approach is to use conditional statements while declaring the classes the given class C inherits. The below code executes and returns True
"""

class A(object): 
    def __init__(self, x): 
        self.x = x
      
    def getX(self): 
        return self.X
  
# Based on condition C inherits 
# from A or it inherits from 
# object i.e. does not inherit A
cond = True  
  
# inherits from A or B
class C(A if cond else object):
    def isA(self):
        return True
  
# Object of C_A
ca = C(1)
print(ca.isA())

"""
Output:

True

Example 3: The following code won’t run, as C does not inherit from A, thus has a default constructor that does not take any argument
"""

class A(object): 
    def __init__(self, x): 
        self.x = x
      
    def getX(self): 
        return self.X
  
# Based on condition C inherits from
# A or it inherits from object i.e.
# does not inherit A
cond = False
  
## inherits from A or B
class C(A if cond else object):
    def isA(self):
        return True
  
# Object of C_A
ca = C(1)
print(ca.isA())

"""
Output:

TypeError                                 Traceback (most recent call last)
<ipython-input-16-f0efc5a814d9> in <module>
    17
    18 # Object of C_A
—> 19 ca = C(1)
    20 print(ca.isA())
    21

TypeError: object() takes no parameters
"""