# https://www.geeksforgeeks.org/random-numbers-in-python/

import random

num = random.random()
print(num)
print('round: ', round(num))

import math
print('math.floor: ', math.floor(num))
print('math.ceiling: ', math.ceil(num))

# Python3 program to demonstrate the use of
# choice() method
 
# import random
import random
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
 
# prints a random item from the string
string = "striver"
print(random.choice(string))

# Python code to demonstrate the working of
# choice() and randrange()
 
# importing "random" for random operations
import random
 
# using choice() to generate a random number from a
# given list of numbers.
print("A random number from list is : ", end="")
print(random.choice([1, 4, 8, 10, 3]))
 
# using randrange() to generate in range from 20
# to 50. The last parameter 3 is step size to skip
# three numbers when selecting.
print("A random number from range is : ", end="")
print(random.randrange(20, 50, 3))

# Python code to demonstrate the working of
# random() and seed()
 
# importing "random" for random operations
import random
 
# using random() to generate a random number
# between 0 and 1
print("A random number between 0 and 1 is : ", end="")
print(random.random())
 
# using seed() to seed a random number
random.seed(5)
 
# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())
 
# using seed() to seed different random number
random.seed(7)
 
# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())
 
# using seed() to seed to 5 again
random.seed(5)
 
# printing mapped random number
print("The mapped random number with 5 is : ", end="")
print(random.random())
 
# using seed() to seed to 7 again
random.seed(7)
 
# printing mapped random number
print("The mapped random number with 7 is : ", end="")
print(random.random())

# import the random module
import random
 
 
# declare a list
sample_list = ['A', 'B', 'C', 'D', 'E']
 
print("Original list : ")
print(sample_list)
 
# first shuffle
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
 
# second shuffle
random.shuffle(sample_list)
print("\nAfter the second shuffle : ")
print(sample_list)

# Python code to demonstrate the working of
# shuffle() and uniform()
 
# importing "random" for random operations
import random
 
# Initializing list
li = [1, 4, 5, 10, 2]
 
# Printing list before shuffling
print("The list before shuffling is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")
print("\r")
 
# using shuffle() to shuffle the list
random.shuffle(li)
 
# Printing list after shuffling
print("The list after shuffling is : ", end="")
for i in range(0, len(li)):
    print(li[i], end=" ")
print("\r")
 
# using uniform() to generate random floating number in range
# prints number between 5 and 10
print("The random floating point number between 5 and 10 is : ", end="")
print(random.uniform(5, 10))

"""
0.8605116525782779
round:  1
math.floor:  0
math.ceiling:  1
3
i
A random number from list is : 10
A random number from range is : 23
A random number between 0 and 1 is : 0.8756888411873854
The mapped random number with 5 is : 0.6229016948897019
The mapped random number with 7 is : 0.32383276483316237
The mapped random number with 5 is : 0.6229016948897019
The mapped random number with 7 is : 0.32383276483316237
Original list :
['A', 'B', 'C', 'D', 'E']

After the first shuffle :
['E', 'A', 'C', 'D', 'B']

After the second shuffle :
['C', 'D', 'A', 'B', 'E']
The list before shuffling is : 1 4 5 10 2
The list after shuffling is : 10 5 1 4 2
The random floating point number between 5 and 10 is : 7.168228418311929
"""

"""
https://www.glassdoor.com/Interview/ChargePoint-Interview-Questions-E722356.htm
1. Write code where one thread generates a random number every second and another thread calculates the byte sum of the random number, and if the byte sum is an even, print the count of total even bytes sums so far. 
2. code to parse the strings, which were files/forlders path in Unix format.
"""

# https://www.pragmaticlinux.com/2022/04/how-to-create-an-array-of-strings-in-python/
import random

my_pets = ['Dog', 'Cat', 'Bunny', 'Fish']
my_pet_index = random.randint(0, 3)
my_pet = my_pets[my_pet_index]
print(my_pet)
