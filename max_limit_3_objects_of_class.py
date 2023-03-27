# https://stackoverflow.com/questions/43324267/program-to-restrict-object-creation-in-python

class A(object):

    _count = 0 

    def __new__(cls):
        if cls._count >= 3:  # @Wilfred fix
            raise Exception('Too many instances were created')
        cls._count += 1
        return super(A, cls).__new__(cls)  # returning the instance

    def __init__(self):
        pass

    def testing(sefl):
        print('just print...')

print(asd := A()) 
print(asd := A()) 
print(asd := A()) 

try:
    print(asd := A()) 
except Exception as err:
    print(err)

asd.testing()
asd.testing()
asd.testing()
asd.testing()
asd.testing()

"""
output:

<__main__.A object at 0x000002A9AD5DD2D0>
<__main__.A object at 0x000002A9AD5DC250>
<__main__.A object at 0x000002A9AD5DCB90>
Too many instances were created
"""

# https://stackoverflow.com/questions/11458477/limit-number-of-class-instances-with-python

"""
There are a couple ways to do this, you can use a Class attribute to store all the instances -- 
If you do it this way, you may want to store them as weak references via the weakref module to prevent issues with garbage collecting:
"""
class MyClass(object):
    _instances=[]
    def __init__(self):
        print(len(self._instances))
        if(len(self._instances) >= 3):
            self._instances.pop(0).kill() #kill the oldest instance
        else:
            self._instances.append(self)

    def kill(self):
        # pass #Do something to kill the instance
        raise Exception('Too many instances were created')
    
    def printNum(self, x, y):
        return x + y

print(test := MyClass())
print(test := MyClass())
print(test := MyClass())
try:
    print(test := MyClass())
except Exception as err:
    print(err)
print('testing... ', sol1 := test.printNum(1, 2))
print('testing... ', sol1 := test.printNum(3, 4))
print('testing... ', sol1 := test.printNum(5, 6))
print('testing... ', sol1 := test.printNum(7, 8))

"""
0
<__main__.MyClass object at 0x00000267A413CA10>
1
<__main__.MyClass object at 0x00000267A413CA90>
2
<__main__.MyClass object at 0x00000267A413CAD0>
3
Too many instances were created
"""

"""
This is a little ugly though. You might also want to consider using some sort of Factory which (conditionally) creates a new instance. 
This method is a little more general.
"""
import weakref
class MyClassLimit(object):
    def __init__(self, str1, str2) -> None:
        self.str1 = str1
        self.str2 = str2

    def my_method(self):
        print(self.str1, self.str2)

class Factory(object):
     def __init__(self,cls,nallowed):
         self.product_class=cls  #What class this Factory produces
         self.nallowed=nallowed  #Number of instances allowed
         self.products=[]

     def __call__(self,*args,**kwargs):
         self.products=[x for x in self.products if x() is not None] #filter out dead objects
         print(self.products)
         print(len(self.products))
         print(self.nallowed)
         if(len(self.products) < self.nallowed):
             newproduct=self.product_class(*args,**kwargs)
             self.products.append(weakref.ref(newproduct))
             return newproduct
         else:
             # return None
             raise Exception('Too many instances were created')

#This factory will create up to 3 instances of MyClass
#and refuse to create more until at least one of those 
#instances have died.
print(factory := Factory(MyClassLimit,3))   
print(i1 := factory("foo","bar"))      #instance of MyClass
print(i2 := factory("bar","baz"))      #instance of MyClass
print(i3 := factory("baz","chicken"))  #instance of MyClass
try:
    print(i3 := factory("baz","dog"))  #None
except Exception as err:
    print(err)
i1.my_method()
i1.my_method()
i1.my_method()
i1.my_method()
i1.my_method()

"""
Output:

<__main__.Factory object at 0x00000297A7B5DD90>
[]
0
3
<__main__.MyClassLimit object at 0x00000297A7B70F50>
[<weakref at 0x00000297A7B8C860; to 'MyClassLimit' at 0x00000297A7B70F50>]
1
3
<__main__.MyClassLimit object at 0x00000297A7B90FD0>
[<weakref at 0x00000297A7B8C860; to 'MyClassLimit' at 0x00000297A7B70F50>, <weakref at 0x00000297A7B8C7C0; to 'MyClassLimit' at 0x00000297A7B90FD0>]    
2
3
<__main__.MyClassLimit object at 0x00000297A7B91010>
[<weakref at 0x00000297A7B8C860; to 'MyClassLimit' at 0x00000297A7B70F50>, <weakref at 0x00000297A7B8C7C0; to 'MyClassLimit' at 0x00000297A7B90FD0>, <weakref at 0x00000297A7B8C8B0; to 'MyClassLimit' at 0x00000297A7B91010>]
3
3
Too many instances were created
"""