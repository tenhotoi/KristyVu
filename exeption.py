# Python program to demonstrate finally
  
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
  
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
  
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')


# Program to depict Raising Exception
try: 
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    # raise  # To determine whether the exception was raised or not

# https://www.geeksforgeeks.org/python-exception-handling/


# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def AbyB(a , b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print ("a/b result in 0")
    else:
        print (c)
    finally:
        print("JUST TESTING 'FINALLY'")
  
# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

# Python program to handle simple runtime error
#Python 3
  
a = [1, 2, 3]
try: 
    print ("Second element = %d" %(a[1]))
  
    # Throws error since there are only 3 elements in array
    print ("Fourth element = %d" %(a[3]))
  
except:
    print ("An error occurred")

print(3//1)
print(3//2)

try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
finally:
   print("Error: can\'t find file or read data")



# https://www.askpython.com/python/examples/exceptions-in-python
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
print("a/b results in : ")
print(a/b)

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print(a/b)
except ZeroDivisionError:
    print("Denominator is zero")
