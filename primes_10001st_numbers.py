

"""
# https://howchoo.com/python/generate-a-list-of-primes-numbers-in-python
Generating a list of non-primes is much simpler than generating a list of primes. 
To begin, we need to think about what a prime number is. 
A prime number is one that is only divisible by 1 and itself. 
Therefore, if we want to generate a list of non-primes under 50 we can do so by generating multiples.
"""
print(noprimes := set(j for i in range(2, 8) for j in range(i*2, 50, i)))
# non-primes is much simpler than generating a list of primes
# range(4, 50, 2). This produces: 4, 6, 8, 10, etc until we hit 50
# range(6, 50, 3) which will add 6, 9, 12, 15, etc to our noprimes set
# Once we calculate all the multiples through 7 we can be sure that we've generated all of the multiples. 
# Anything 8 or higher will simply duplicate the work we've already done.
print(primes := [x for x in range(2, 50) if x not in noprimes])

"""
We are using a set in this case because we only want to include each multiple once. The function range(2, 8) will generate the numbers 2-7. In this example we are using set comprehension to iterate through the numbers 2 through 7. During each iteration we will use the number to iterate through the range 2i through 50 with an interval of i.

Hopefully that isn't too complicated! As an example, the first time we iterate through the outer loop, we generate the number 2. Then we iterate through the inner loop using 2 to produce this range: range(4, 50, 2). This produces: 4, 6, 8, 10, etc until we hit 50. Each of these numbers will be added to our noprimes set.

The next time through we generate the number 3. Then in our inner loop we will produce range(6, 50, 3) which will add 6, 9, 12, 15, etc to our noprimes set.

As you can see, this simply generates multiples. Once we calculate all the multiples through 7 we can be sure that we've generated all of the multiples. Anything 8 or higher will simply duplicate the work we've already done.
"""

# Now for 10001st prime numbers:

def list_primes(primes, low, high): 
    if low < high:
        print(f'low is {low}')
        print(f'high is {high}')
        # print(mid := (high - low) // 2)   <========== this causes infinite loop when low = 8 and high = 23, mid would be 7 which is incorret. mid should be 8 + 7 = 15
        print(mid := low + (high - low) // 2)
        # if mid > 2:
        if (high - low) > 2:        
            list_primes(primes, low, mid - 1)
            list_primes(primes, mid + 1, high)           
            print(tmp_noprimes := set(j for i in range(2, 8) for j in range(i*2, high, i) if low < j < high))
            print(tmp_primes := [x for x in range(low, high) if x not in noprimes])
            print(primes := primes + tmp_primes)
            return primes    # remember: it worked before this line, so if it doesn't work, remove this line !!!

    # return primes  # <============ this one causes a lot of problems !!!!!!!!!!!

# primes = []
# print(list_primes(primes, 2, 10))
# print(f' primes are {primes}')

"""
Before the fix on line 35:

low is 2
high is 10
4
low is 2
high is 3
0
low is 5
high is 10
2                       <========== wrong mid with if statement on line 36, but only cause issue with higher range, like 50
{8, 9, 4, 6}
[2, 3, 5, 7]
[2, 3, 5, 7]
[2, 3, 5, 7]            <=========== WOO HOO !!!! return statement on line 43 works !!! 
 primes are []          <=========== ????????? not sure how to get prime list from the function ????????
"""

# primes = []
# print(list_primes(primes, 1, 10))
# print(f' primes are {primes}')

"""
Before the fix on line 35:

None    <============ the function doesn't return anything, since 'return' there would cause a lot of issue
low is 1
high is 10
4
low is 1
high is 3
1
low is 5
high is 10
2
{8, 9, 4, 6}
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]         <=========== WOO HOO !!!! return statement on line 43 works !!! 
None    <============ the function doesn't return anything, since 'return' there would cause a lot of issue
 primes are []          <=========== ????????? not sure how to get prime list from the function ????????
"""

# primes = []
# print(list_primes(primes, 1, 50))
# print(f' primes are {primes}')

"""
infinite loop happens when low was NOT added to mid values (line 34):
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
high is 23
7
low is 8
"""


"""
After the fix on line 35:

low is 2
high is 10
6
low is 2
high is 5
3
low is 4
high is 5
4
set()
[]
[]
{4}
[2, 3]
[2, 3]
low is 7
high is 10
8
low is 9
high is 10
9
set()
[]
[]
{8, 9}
[7]
[7]
{8, 9, 4, 6}
[2, 3, 5, 7]
[2, 3, 5, 7]
[2, 3, 5, 7]
 primes are []


low is 1
high is 10
5
low is 1
high is 4
2
low is 6
high is 10
8
low is 6
high is 7
6
set()
[]
[]
low is 9
high is 10
9
set()
[]
[]
{8, 9}
[7]
[7]
{8, 9, 4, 6}
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
 primes are []


low is 1
high is 50
25
low is 1
high is 24
12
low is 1
high is 11
6
low is 1
high is 5
3
low is 1
high is 2
1
low is 4
high is 5
4
set()
[]
[]
{4}
[1, 2, 3]
[1, 2, 3]
low is 7
high is 11
9
low is 7
high is 8
7
set()
[7]
[7]
low is 10
high is 11
10
set()
[]
[]
{8, 9, 10}
[7]
[7]
{4, 6, 8, 9, 10}
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
low is 13
high is 24
18
low is 13
high is 17
15
low is 13
high is 14
13
set()
[13]
[13]
low is 16
high is 17
16
set()
[]
[]
{16, 14, 15}
[13]
[13]
low is 19
high is 24
21
low is 19
high is 20
19
set()
[19]
[19]
low is 22
high is 24
23
set()
[23]
[23]
{20, 21, 22}
[19, 23]
[19, 23]
{14, 15, 16, 18, 20, 21, 22}
[13, 17, 19, 23]
[13, 17, 19, 23]
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22}
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
low is 26
high is 50
38
low is 26
high is 37
31
low is 26
high is 30
28
low is 26
high is 27
26
set()
[]
[]
low is 29
high is 30
29
set()
[29]
[29]
{27, 28}
[29]
[29]
low is 32
high is 37
34
low is 32
high is 33
32
set()
[]
[]
low is 35
high is 37
36
{36}
[]
[]
{33, 34, 35, 36}
[]
[]
{32, 33, 34, 35, 36, 27, 28, 30}
[29, 31]
[29, 31]
low is 39
high is 50
44
low is 39
high is 43
41
low is 39
high is 40
39
set()
[]
[]
low is 42
high is 43
42
set()
[]
[]
{40, 42}
[41]
[41]
low is 45
high is 50
47
low is 45
high is 46
45
set()
[]
[]
low is 48
high is 50
49
{49}
[]
[]
{48, 49, 46}
[47]
[47]
{40, 42, 44, 45, 46, 48, 49}
[41, 43, 47]
[41, 43, 47]
{32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 27, 28, 30}
[29, 31, 37, 41, 43, 47]
[29, 31, 37, 41, 43, 47]
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
 primes are []
"""

# primes = list_primes([], 1, 10)
# print(f' primes are {primes}')

"""
WITH CORRECT MID with if statement on line 37:

low is 1
high is 10
5
low is 1
high is 4
2
low is 3
high is 4
3
set()
[1, 2, 3]
[1, 2, 3]
low is 6
high is 10
8
low is 6
high is 7
6
low is 9
high is 10
9
{8, 9}
[7]
[7]
{8, 9, 4, 6}
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
 primes are [1, 2, 3, 5, 7]
"""

# primes = list_primes([], 1, 50)
# print(f' primes are {primes}')

"""
low is 1
high is 50
25
low is 1
high is 24
12
low is 1
high is 11
6
low is 1
high is 5
3
low is 1
high is 2
1
low is 4
high is 5
4
{4}
[1, 2, 3]
[1, 2, 3]
low is 7
high is 11
9
low is 7
high is 8
7
low is 10
high is 11
10
{8, 9, 10}
[7]
[7]
{4, 6, 8, 9, 10}
[1, 2, 3, 5, 7]
[1, 2, 3, 5, 7]
low is 13
high is 24
18
low is 13
high is 17
15
low is 13
high is 14
13
low is 16
high is 17
16
{16, 14, 15}
[13]
[13]
low is 19
high is 24
21
low is 19
high is 20
19
low is 22
high is 24
23
{20, 21, 22}
[19, 23]
[19, 23]
{14, 15, 16, 18, 20, 21, 22}
[13, 17, 19, 23]
[13, 17, 19, 23]
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22}
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
low is 26
high is 50
38
low is 26
high is 37
31
low is 26
high is 30
28
low is 26
high is 27
26
low is 29
high is 30
29
{27, 28}
[29]
[29]
low is 32
high is 37
34
low is 32
high is 33
32
low is 35
high is 37
36
{33, 34, 35, 36}
[]
[]
{32, 33, 34, 35, 36, 27, 28, 30}
[29, 31]
[29, 31]
low is 39
high is 50
44
low is 39
high is 43
41
low is 39
high is 40
39
low is 42
high is 43
42
{40, 42}
[41]
[41]
low is 45
high is 50
47
low is 45
high is 46
45
low is 48
high is 50
49
{48, 49, 46}
[47]
[47]
{40, 42, 44, 45, 46, 48, 49}
[41, 43, 47]
[41, 43, 47]
{32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 27, 28, 30}
[29, 31, 37, 41, 43, 47]
[29, 31, 37, 41, 43, 47]
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""

# primes = list_primes([], 1, 10001)
# print(f' primes are {primes}')

"""
https://www.pythonpool.com/check-if-number-is-prime-in-python/
6 Best Ways To Check If Number Is Prime In Python

The following methods are available:

isprime() function
If-else statements
Math module
Sympy library
PrimePy library
is_integer function

1: Using isprime()
Example:
"""
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
print(isprime(7))
print(isprime(8))

def isprime(num):
    if num==2 or num==3:
        return True
    if num % 2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True
print(isprime(13))
print(isprime(18))

def isprime(num):
  if num == 2 or num == 3:
      return True
  if num < 2 or num%2 == 0:
      return False
  if num < 9:
      return True
  if num%3 == 0:
      return False
  a = int(num**0.5)
  b = 5
  while b <= a:
    print ('\t',b)
    if num%b == 0:
        return False
    if num%(b+2) == 0:
        return False
    b=b+6
  return True
print(isprime(15))
print(isprime(2))

def isprime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False
print(isprime(64))
print(isprime(5))

"""
2: Using if-else statements


n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n//2):
        if(n%i)==0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print(n,"is neither prime nor composite")


3: Using math function to check if number is prime python
"""

import math
def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return num>1
print(isprime(14))
print(isprime(7))

"""
4: Using sympy module


import sympy
print(sympy.isprime(90))

from sympy import *
print(isprime(19))

import sympy.ntheory as nt
print(nt.isprime(8))


5: Using primePy library to check if a number is prime or not


from primePy import primes
print(primes.check(63))


6: Using is_integer function
"""

def prime(num):
    a=[]
    for i in range (1, num+1):
        if (num/i).is_integer():
            a.append(i)
    if len(a)==2:
        print("Prime")
    else:
        print("Not Prime")
prime(2)

"""
Learn Something New: How to generate a random prime number?
"""

import random
def range_primes(a, b):
    prime = []
    for i in range(a, b):
        is_prime = True
        for n in range(2, i):
            if i % n == 0:
                is_prime = False
        if is_prime:
            prime.append(i)
    return prime
prime= range_primes(1,100)
random_prime = random.choice(prime)
print("Random Prime Number is:", random_prime)

class Primes:
    def __init__(self, primes = []) -> None:
        self.primes = primes
        self.count = 0

    def list_primes_2nd(self, primes, low, high):
        # high += 1   # trying to include the last number of the range which is high
                    # but this caused: RecursionError: maximum recursion depth exceeded while calling a Python object
        if (high - low) > 2:
            print(f'low is {low}')
            print(f'high is {high}')
            # print(mid := (high - low) // 2)   <========== this causes infinite loop when low = 8 and high = 23, mid would be 7 which is incorret. mid should be 8 + 7 = 15
            print(mid := low + (high - low) // 2)
            # if mid > 2:
            self.list_primes_2nd(primes, low, mid)
            self.list_primes_2nd(primes, mid, high)   
            # print(f' primes in the function are now {primes}')    
            tmp_primes = []  
            if (high - low) <= 4:      
                print(f' (high - low) is {high - low} '.center(60, '='))                   
                print(f'low is {low}')
                print(f'high is {high}')                
         
                print(tmp_noprimes := set(j for i in range(2, 8) for j in range(i*2, high, i) if low <= j <= high))
                print(tmp_primes := [x for x in range(low, high) if x not in tmp_noprimes])
                """
                a = []
                for i in range (low, high):
                    if (num/i).is_integer():
                            a.append(i)
                if len(a)==2:
                    print("Prime")
                    tmp_primes += a
                else:
                    print("Not Prime")
                """
                print(f' tmp_primes in the function in if statement are now {tmp_primes}') 
            self.count += 1
            print(f'  self.count is now {self.count}  '.center(60, '-'))
            self.primes += tmp_primes
            # print(f' primes in the function after if statement are now {primes}') 
            # print('  why does not print here?  '.center(60, '?'))
            return self.primes    # remember: it worked before this line, so if it doesn't work, remove this line !!!

# sol = Primes()
# primes = sol.list_primes_2nd([], 1, 50)
# print(f' primes are {primes}')

"""
low is 1
high is 50
25
low is 1
high is 25
13
low is 1
high is 13
7
low is 1
high is 7
4
low is 1
high is 4
2
==================== (high - low) is 3 =====================
set()
[1, 2, 3]
 tmp_primes in the function in if statement are now [1, 2, 3]
low is 4
high is 7
5
==================== (high - low) is 3 =====================
{6}
[5]
 tmp_primes in the function in if statement are now [5]
low is 7
high is 13
10
low is 7
high is 10
8
==================== (high - low) is 3 =====================
{8, 9}
[7]
 tmp_primes in the function in if statement are now [7]
low is 10
high is 13
11
==================== (high - low) is 3 =====================
{12}
[11]
 tmp_primes in the function in if statement are now [11]
low is 13
high is 25
19
low is 13
high is 19
16
low is 13
high is 16
14
==================== (high - low) is 3 =====================
{14, 15}
[13]
 tmp_primes in the function in if statement are now [13]
low is 16
high is 19
17
==================== (high - low) is 3 =====================
{18}
[17]
 tmp_primes in the function in if statement are now [17]
low is 19
high is 25
22
low is 19
high is 22
20
==================== (high - low) is 3 =====================
{20, 21}
[19]
 tmp_primes in the function in if statement are now [19]
low is 22
high is 25
23
==================== (high - low) is 3 =====================
{24}
[23]
 tmp_primes in the function in if statement are now [23]
low is 25
high is 50
37
low is 25
high is 37
31
low is 25
high is 31
28
low is 25
high is 28
26
==================== (high - low) is 3 =====================
{26, 27}
[]
 tmp_primes in the function in if statement are now []
low is 28
high is 31
29
==================== (high - low) is 3 =====================
{30}
[29]
 tmp_primes in the function in if statement are now [29]
low is 31
high is 37
34
low is 31
high is 34
32
==================== (high - low) is 3 =====================
{32, 33}
[31]
 tmp_primes in the function in if statement are now [31]
low is 34
high is 37
35
==================== (high - low) is 3 =====================
{35, 36}
[]
 tmp_primes in the function in if statement are now []
low is 37
high is 50
43
low is 37
high is 43
40
low is 37
high is 40
38
==================== (high - low) is 3 =====================
{38, 39}
[37]
 tmp_primes in the function in if statement are now [37]
low is 40
high is 43
41
==================== (high - low) is 3 =====================
{42}
[41]
 tmp_primes in the function in if statement are now [41]
low is 43
high is 50
46
low is 43
high is 46
44
==================== (high - low) is 3 =====================
{44, 45}
[43]
 tmp_primes in the function in if statement are now [43]
low is 46
high is 50
48
==================== (high - low) is 4 =====================
{48, 49}
[47]
 tmp_primes in the function in if statement are now [47]
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
 """

# sol2 = Primes()

# primes = sol2.list_primes_2nd([], 1, 100)
# print(f' primes are {primes}')

"""
low is 96
high is 100
{96, 98, 99}
[97]
 tmp_primes in the function in if statement are now [97]
-------------------  self.count is now 58-------------------
-------------------  self.count is now 59-------------------
-------------------  self.count is now 60-------------------
-------------------  self.count is now 61-------------------
-------------------  self.count is now 62-------------------
-------------------  self.count is now 63-------------------
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
 """

# primes = sol2.list_primes_2nd([], 1, 10001)
# print(f' primes are {primes}')

"""
------------------  self.count is now 5892------------------
------------------  self.count is now 5893------------------
------------------  self.count is now 5894------------------
------------------  self.count is now 5895------------------
------------------  self.count is now 5896------------------
------------------  self.count is now 5897------------------
------------------  self.count is now 5898------------------
------------------  self.count is now 5899------------------
------------------  self.count is now 5900------------------
------------------  self.count is now 5901------------------
------------------  self.count is now 5902------------------
------------------  self.count is now 5903------------------
 primes are [1, 2, 3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 61, 67, 71, 73, 79, 97, 101, 107, 121, 131, 139, 149, 151, 157, 163, 169, 173, 179, 193, 197, 199, 209, 223, 227, 229, 233, 241, 247, 251, 253, 257, 263, 271, 277, 281, 307, 311, 313, 319, 331, 341, 349, 353, 359, 373, 379, 383, 389, 391, 397, 403, 407, 409, 419, 431, 433, 437, 443, 451, 457, 461, 463, 467, 481, 487, 491, 509, 521, 529, 541, 547, 559, 563, 569, 583, 589, 593, 599, 613, 619, 629, 643, 647, 649, 653, 659, 667, 671, 673, 677, 683, 691, 697, 701, 703, 727, 731, 737, 743, 751, 761, 769, 779, 781, 793, 799, 803, 809, 821, 823, 827, 829, 839, 853, 857, 859, 863, 871, 877, 881, 883, 887, 893, 899, 901, 907, 911, 937, 941, 949, 961, 971, 977, 979, 983, 989, 1003, 1009, 1013, 1019, 1027, 1033, 1037, 1039, 1049, 1061, 1063, 1067, 1073, 1081, 1087, 1091, 1093, 1097, 1111, 1117, 1121, 1133, 1139, 1151, 1159, 1171, 1189, 1193, 1199, 1213, 1219, 1223, 1229, 1243, 1249, 1259, 1273, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1313, 1321, 1327, 1331, 1357, 1361, 1367, 1369, 1381, 1391, 1399, 1409, 1423, 1429, 1433, 1439, 1447, 1453, 1457, 1459, 1469, 1483, 1487, 1493, 1501, 1507, 1511, 1513, 1517, 1523, 1531, 1537, 1541, 1571, 1579, 1591, 1601, 1609, 1613, 1619, 1633, 1639, 1643, 1649, 1657, 1663, 1667, 1669, 1679, 1681, 1691, 1693, 1697, 1703, 1711, 1717, 1721, 1727, 1741, 1747, 1751, 1759, 1769, 1781, 1789, 1819, 1823, 1829, 1843, 1849, 1853, 1859, 1873, 1877, 1879, 1889, 1903, 1907, 1909, 1913, 1921, 1927, 1931, 1933, 1937, 1943, 1951, 1957, 1961, 1987, 1991, 1993, 1999, 2011, 2021, 2029, 2033, 2039, 2053, 2059, 2063, 2069, 2071, 2077, 2083, 2087, 2089, 2099, 2111, 2113, 2117, 2123, 2131, 2137, 2141, 2143, 2147, 2161, 2167, 2171, 2189, 2201, 2209, 2221, 2227, 2239, 2243, 2249, 2263, 2267, 2269, 2273, 2279, 2287, 2293, 2297, 2299, 2311, 2321, 2323, 2327, 2333, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2399, 2411, 2419, 2423, 2449, 2453, 2459, 2473, 2479, 2483, 2489, 2501, 2503, 2507, 2509, 2519, 2533, 2537, 2539, 2543, 2551, 2557, 2561, 2563, 2567, 2573, 2579, 2581, 2587, 2591, 2617, 2621, 2629, 2641, 2651, 2657, 2659, 2663, 2669, 2683, 2689, 2693, 2699, 2707, 2713, 2717, 2719, 2729, 2741, 2743, 2747, 2753, 2761, 2767, 2771, 2773, 2777, 2791, 2797, 2801, 2813, 2819, 2831, 2839, 2851, 2869, 2873, 2879, 2893, 2897, 2899, 2903, 2909, 2917, 2923, 2927, 2929, 2941, 2951, 2953, 2957, 2963, 2969, 2971, 2977, 2981, 2987, 3001, 3007, 3011, 3019, 3029, 3041, 3047, 3049, 3053, 3079, 3083, 3089, 3103, 3109, 3113, 3119, 3127, 3133, 3137, 3139, 3149, 3163, 3167, 3173, 3181, 3187, 3191, 3193, 3197, 3203, 3211, 3217, 3221, 3251, 3259, 3271, 3281, 3289, 3293, 3299, 3313, 3319, 3323, 3329, 3337, 3343, 3347, 3349, 3359, 3361, 3371, 3373, 3377, 3383, 3391, 3397, 3401, 3407, 3421, 3427, 3431, 3439, 3449, 3461, 3469, 3499, 3503, 3509, 3517, 3523, 3527, 3529, 3533, 3539, 3547, 3553, 3557, 3571, 3581, 3583, 3587, 3593, 3601, 3607, 3611, 3617, 3631, 3641, 3649, 3659, 3671, 3673, 3679, 3683, 3709, 3713, 3719, 3733, 3739, 3743, 3749, 3751, 3757, 3763, 3767, 3769, 3779, 3791, 3793, 3797, 3803, 3811, 3817, 3821, 3823, 3827, 3841, 3847, 3851, 3869, 3881, 3889, 3901, 3907, 3919, 3923, 3929, 3943, 3947, 3949, 3953, 3959, 3967, 3973, 3977, 3979, 3991, 4001, 4003, 4007, 4013, 4021, 4027, 4031, 4037, 4051, 4057, 4061, 4063, 4069, 4079, 4091, 4099, 4103, 4129, 4133, 4139, 4141, 4147, 4153, 4157, 4159, 4163, 4169, 4177, 4181, 4183, 4187, 4201, 4211, 4213, 4217, 4219, 4231, 4237, 4241, 4247, 4259, 4261, 4271, 4279, 4289, 4297, 4303, 4309, 4313, 4339, 4343, 4349, 4363, 4369, 4373, 4379, 4387, 4393, 4397, 4399, 4409, 4421, 4423, 4427, 4433, 4441, 4447, 4451, 4453, 4457, 4471, 4477, 4481, 4493, 4499, 4511, 4519, 4531, 4549, 4553, 4559, 4573, 4577, 4579, 4583, 4589, 4597, 4603, 4607, 4609, 4621, 4631, 4633, 4637, 4643, 4649, 4651, 4657, 4661, 4667, 4681, 4687, 4691, 4699, 4709, 4721, 4727, 4729, 4733, 4759, 4763, 4769, 4777, 4783, 4787, 4789, 4793, 4799, 4807, 4811, 4813, 4817, 4831, 4841, 4843, 4847, 4861, 4867, 4871, 4877, 4883, 4889, 4891, 4901, 4909, 4919, 4933, 4939, 4943, 4969, 4973, 4979, 4993, 4999, 5003, 5009, 5017, 5023, 5027, 5029, 5039, 5041, 5051, 5053, 5057, 5063, 5071, 5077, 5081, 5087, 5101, 5107, 5111, 5119, 5129, 5141, 5149, 5179, 5183, 5189, 5197, 5203, 5207, 5209, 5213, 5219, 5227, 5233, 5237, 5251, 5261, 5263, 5267, 5273, 5281, 5287, 5291, 5297, 5311, 5321, 5329, 5339, 5351, 5353, 5359, 5363, 5389, 5393, 5399, 5407, 5413, 5417, 5419, 5423, 5429, 5431, 5437, 5441, 5443, 5447, 5461, 5471, 5477, 5491, 5497, 5501, 5507, 5519, 5521, 5531, 5539, 5549, 5563, 5569, 5573, 5599, 5603, 5609, 5623, 5627, 5629, 5633, 5639, 5647, 5653, 5657, 5659, 5671, 5681, 5683, 5687, 5693, 5701, 5707, 5711, 5717, 5731, 5737, 5741, 5743, 5749, 5759, 5771, 5779, 5783, 5809, 5813, 5819, 5821, 5827, 5833, 5837, 5839, 5843, 5849, 5857, 5861, 5863, 5867, 5881, 5891, 5893, 5897, 5899, 5911, 5917, 5921, 5927, 5939, 5941, 5951, 5959, 5969, 5977, 5983, 5989, 5993, 6017, 6019, 6023, 6029, 6037, 6043, 6047, 6049, 6053, 6061, 6067, 6071, 6073, 6077, 6091, 6101, 6107, 6121, 6127, 6131, 6133, 6149, 6151, 6161, 6169, 6173, 6179, 6193, 6199, 6203, 6229, 6233, 6239, 6253, 6257, 6259, 6263, 6269, 6277, 6283, 6287, 6289, 6301, 6311, 6313, 6317, 6323, 6329, 6331, 6337, 6341, 6347, 6361, 6367, 6371, 6379, 6389, 6401, 6407, 6409, 6413, 6439, 6443, 6449, 6457, 6463, 6467, 6469, 6473, 6479, 6487, 6491, 6493, 6497, 6511, 6521, 6523, 6527, 6541, 6547, 6551, 6557, 6563, 6569, 6571, 6581, 6589, 6599, 6613, 6619, 6623, 6641, 6647, 6649, 6653, 6659, 6667, 6673, 6677, 6679, 6683, 6691, 6697, 6701, 6703, 6707, 6719, 6721, 6731, 6737, 6751, 6757, 6761, 6779, 6781, 6791, 6799, 6803, 6809, 6823, 6829, 6833, 6859, 6863, 6869, 6877, 6883, 6887, 6889, 6893, 6899, 6907, 6913, 6917, 6931, 6941, 6943, 6947, 6953, 6961, 6967, 6971, 6977, 6991, 7001, 7009, 7019, 7031, 7033, 7039, 7043, 7069, 7073, 7079, 7087, 7093, 7097, 7099, 7103, 7109, 7111, 7117, 7121, 7123, 7127, 7141, 7151, 7157, 7171, 7177, 7181, 7187, 7199, 7201, 7211, 7219, 7229, 7243, 7249, 7253, 7267, 7277, 7279, 7283, 7289, 7297, 7303, 7307, 7313, 7321, 7327, 7331, 7333, 7337, 7351, 7361, 7367, 7381, 7391, 7409, 7411, 7421, 7423, 7429, 7433, 7439, 7453, 7459, 7463, 7489, 7493, 7499, 7501, 7507, 7513, 7517, 7519, 7523, 7529, 7537, 7541, 7543, 7547, 7561, 7571, 7573, 7577, 7579, 7591, 7597, 7601, 7607, 7619, 7621, 7631, 7639, 7649, 7657, 7663, 7669, 7673, 7697, 7699, 7703, 7709, 7717, 7723, 7727, 7729, 7733, 7741, 7747, 7751, 7753, 7757, 7771, 7781, 7787, 7801, 7807, 7811, 7813, 7829, 7831, 7841, 7849, 7853, 7859, 7873, 7879, 7883, 7891, 7897, 7907, 7909, 7913, 7919, 7927, 7933, 7937, 7943, 7951, 7957, 7961, 7963, 7967, 7969, 7981, 7991, 7997, 8009, 8011, 8021, 8039, 8041, 8047, 8053, 8059, 8063, 8069, 8083, 8089, 8093, 8119, 8123, 8129, 8137, 8143, 8147, 8149, 8153, 8159, 8167, 8171, 8173, 8177, 8191, 8201, 8203, 8207, 8221, 8227, 8231, 8237, 8243, 8249, 8251, 8261, 8269, 8279, 8293, 8299, 8303, 8321, 8327, 8329, 8333, 8339, 8347, 8353, 8357, 8359, 8363, 8371, 8377, 8381, 8383, 8387, 8399, 8401, 8411, 8417, 8431, 8437, 8441, 8459, 8461, 8471, 8479, 8483, 8489, 8503, 8509, 8513, 8527, 8537, 8539, 8543, 8549, 8557, 8563, 8567, 8573, 8581, 8587, 8591, 8593, 8597, 8611, 8621, 8627, 8633, 8639, 8641, 8651, 8669, 8671, 8683, 8689, 8693, 8699, 8713, 8719, 8723, 8749, 8753, 8759, 8767, 8773, 8777, 8779, 8783, 8789, 8791, 8797, 8801, 8803, 8807, 8821, 8831, 8837, 8851, 8857, 8861, 8867, 8879, 8881, 8891, 8899, 8909, 8923, 8929, 8933, 8947, 8957, 8959, 8963, 8969, 8977, 8983, 8987, 8993, 9001, 9007, 9011, 9013, 9017, 9031, 9041, 9047, 9061, 9071, 9089, 9091, 9101, 9103, 9109, 9113, 9119, 9133, 9139, 9143, 9157, 9167, 9169, 9173, 9179, 9181, 9187, 9193, 9197, 9203, 9211, 9217, 9221, 9227, 9241, 9251, 9257, 9259, 9269, 9271, 9281, 9299, 9313, 9319, 9323, 9329, 9343, 9349, 9353, 9377, 9379, 9383, 9389, 9397, 9403, 9407, 9409, 9413, 9421, 9427, 9431, 9433, 9437, 9451, 9461, 9467, 9481, 9487, 9491, 9493, 9509, 9511, 9521, 9529, 9533, 9539, 9553, 9559, 9563, 9571, 9577, 9587, 9589, 9593, 9599, 9607, 9613, 9617, 9623, 9631, 9637, 9641, 9643, 9647, 9649, 9661, 9671, 9677, 9689, 9691, 9701, 9719, 9721, 9727, 9733, 9739, 9743, 9749, 9763, 9767, 9769, 9773, 9787, 9797, 9799, 9803, 9811, 9817, 9823, 9827, 9833, 9841, 9847, 9851, 9857, 9871, 9881, 9883, 9889, 9899, 9901, 9911, 9923, 9929, 9943, 9949, 9953, 9959, 9973, 9979, 9983]
"""

# sol2 = Primes()
# primes = sol2.list_primes_2nd([], 1, 99)
# print(f' primes are {primes}')

"""
low is 95
high is 99
{96, 98, 95}
[97]
 tmp_primes in the function in if statement are now [97]
------------------  self.count is now 58  ------------------
------------------  self.count is now 59  ------------------
------------------  self.count is now 60  ------------------
------------------  self.count is now 61  ------------------
------------------  self.count is now 62  ------------------
------------------  self.count is now 63  ------------------
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
"""

# sol2 = Primes()
# primes = sol2.list_primes_2nd([], 1, 1001)
# print(f' primes are {primes}')

"""
-----------------  self.count is now 508  ------------------
-----------------  self.count is now 509  ------------------
-----------------  self.count is now 510  ------------------
-----------------  self.count is now 511  ------------------
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199, 209, 211, 221, 223, 227, 229, 233, 239, 241, 247, 251, 253, 257, 263, 269, 271, 277, 281, 283, 289, 293, 299, 307, 311, 313, 317, 319, 323, 331, 337, 341, 347, 349, 353, 359, 361, 367, 373, 377, 379, 383, 389, 391, 397, 401, 403, 407, 409, 419, 421, 431, 433, 437, 439, 443, 449, 451, 457, 461, 463, 467, 473, 479, 481, 487, 491, 493, 499, 503, 509, 517, 521, 523, 527, 529, 533, 541, 547, 551, 557, 559, 563, 569, 571, 577, 583, 587, 589, 593, 599, 601, 607, 611, 613, 617, 619, 629, 631, 641, 643, 647, 649, 653, 659, 661, 667, 671, 673, 677, 683, 689, 691, 697, 701, 703, 709, 713, 719, 727, 731, 733, 737, 739, 743, 751, 757, 761, 767, 769, 773, 779, 781, 787, 793, 797, 799, 803, 809, 811, 817, 821, 823, 827, 829, 839, 841, 851, 853, 857, 859, 863, 869, 871, 877, 881, 883, 887, 893, 899, 901, 907, 911, 913, 919, 923, 929, 937, 941, 943, 947, 949, 953, 961, 967, 971, 977, 979, 983, 989, 991, 997]
"""

# sol2 = Primes()
# primes = sol2.list_primes_2nd([], 1, 53)
# print(f' primes are {primes}')

"""
low is 49
high is 53
{49, 50, 51, 52}
[]
 tmp_primes in the function in if statement are now []
------------------  self.count is now 27  ------------------
------------------  self.count is now 28  ------------------
------------------  self.count is now 29  ------------------
------------------  self.count is now 30  ------------------
------------------  self.count is now 31  ------------------
 primes are [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
 """

"""
SymPy is another choice. It is a Python library for symbolic mathematics. It provides several functions for prime.

isprime(n)              # Test if n is a prime number (True) or not (False).

primerange(a, b)        # Generate a list of all prime numbers in the range [a, b).
randprime(a, b)         # Return a random prime number in the range [a, b).
primepi(n)              # Return the number of prime numbers less than or equal to n.

prime(nth)              # Return the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.
prevprime(n, ith=1)     # Return the largest prime smaller than n
nextprime(n)            # Return the ith prime greater than n

sieve.primerange(a, b)  # Generate all prime numbers in the range [a, b), implement
"""
import sympy

print(isprime(10001)) # Test if n is a prime number (True) or not (False).

print(list(sympy.primerange(5, 10))) # Generate a list of all prime numbers in the range [a, b).
print(sympy.randprime(9, 100)) # Return a random prime number in the range [a, b).
print(sympy.primepi(50)) # Return the number of prime numbers less than or equal to n.

print(sympy.prime(10)) # Return the nth prime, with the primes indexed as prime(1) = 2. The nth prime is approximately n*log(n) and can never be larger than 2**n.

"""
False
[<generator object primerange at 0x00000251394234C0>]
29
15
29
"""

# print(noprimes := set(j for i in range(2, 8) for j in range(i*2, 10001, i)))
# print(primes := [x for x in range(2, 10001) if x not in noprimes])

# non-primes is much simpler than generating a list of primes
# range(4, 50, 2). This produces: 4, 6, 8, 10, etc until we hit 50
# range(6, 50, 3) which will add 6, 9, 12, 15, etc to our noprimes set
# Once we calculate all the multiples through 7 we can be sure that we've generated all of the multiples. 
# Anything 8 or higher will simply duplicate the work we've already done.

"""

{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 102, 104, 105, 106, 108, 110, 111, 112, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 128, 129, 130, 132, 133, 134, 135, 136, 138, 140, 141, 142, 144, 145, 146, 147, 148, 150, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 164, 165, 166, 168, 170, 171, 172, 174, 175, 176, 177, 178, 180, 182, 183, 184, 185, 186, 188, 189, 190, 192, 194, 195, 196, 198, 200, 201, 202, 203, 204, 205, 206, 207, 208, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 224, 225, 226, 228, 230, 231, 232, 234, 235, 236, 237, 238, 240, 242, 243, 244, 245, 246, 248, 249, 250, 252, 254, 255, 256, 258, 259, 260, 261, 262, 264, 265, 266, 267, 268, 270, 272, 273, 274, 275, 276, 278, 279, 280, 282, 284, 285, 286, 287, 288, 290, 291, 292, 294, 295, 296, 297, 298, 300, 301, 302, 303, 304, 305, 306, 308, 309, 310, 312, 314, 315, 316, 318, 320, 321, 322, 324, 325, 326, 327, 328, 329, 330, 332, 333, 334, 335, 336, 338, 339, 340, 342, 343, 344, 345, 346, 348, 350, 351, 352, 354, 355, 356, 357, 358, 360, 362, 363, 364, 365, 366, 368, 369, 370, 371, 372, 374, 375, 376, 378, 380, 381, 382, 384, 385, 386, 387, 388, 390, 392, 393, 394, 395, 396, 398, 399, 400, 402, 404, 405, 406, 408, 410, 411, 412, 413, 414, 415, 416, 417, 418, 420, 422, 423, 424, 425, 426, 427, 428, 429, 430, 432, 434, 435, 436, 438, 440, 441, 442, 444, 445, 446, 447, 448, 450, 452, 453, 454, 455, 456, 458, 459, 460, 462, 464, 465, 466, 468, 469, 470, 471, 472, 474, 475, 476, 477, 478, 480, 482, 483, 484, 485, 486, 488, 489, 490, 492, 494, 495, 496, 497, 498, 500, 501, 502, 504, 505, 506, 507, 508, 510, 511, 512, 513, 514, 515, 516, 518, 519, 520, 522, 524, 525, 526, 528, 530, 531, 532, 534, 535, 536, 537, 538, 539, 540, 542, 543, 544, 545, 546, 548, 549, 550, 552, 553, 554, 555, 556, 558, 560, 561, 562, 564, 565, 566, 567, 568, 570, 572, 573, 574, 575, 576, 578, 579, 580, 581, 582, 584, 585, 586, 588, 590, 591, 592, 594, 595, 596, 597, 598, 600, 602, 603, 604, 605, 606, 608, 609, 610, 612, 614, 615, 616, 618, 620, 621, 622, 623, 624, 625, 626, 627, 628, 630, 632, 633, 634, 635, 636, 637, 638, 639, 640, 642, 644, 645, 646, 648, 650, 651, 652, 654, 655, 656, 657, 658, 660, 662, 663, 664, 665, 666, 668, 669, 670, 672, 674, 675, 676, 678, 679, 680, 681, 682, 684, 685, 686, 687, 688, 690, 692, 693, 694, 695, 696, 698, 699, 700, 702, 704, 705, 706, 707, 708, 710, 711, 712, 714, 715, 716, 717, 718, 720, 721, 722, 723, 724, 725, 726, 728, 729, 730, 732, 734, 735, 736, 738, 740, 741, 742, 744, 745, 746, 747, 748, 749, 750, 752, 753, 754, 755, 756, 758, 759, 760, 762, 763, 764, 765, 766, 768, 770, 771, 772, 774, 775, 776, 777, 778, 780, 782, 783, 784, 785, 786, 788, 789, 790, 791, 792, 794, 795, 796, 798, 800, 801, 802, 804, 805, 806, 807, 808, 810, 812, 813, 814, 815, 816, 818, 819, 820, 822, 824, 825, 826, 828, 830, 831, 832, 833, 834, 835, 836, 837, 838, 840, 842, 843, 844, 845, 846, 847, 848, 849, 850, 852, 854, 855, 856, 858, 860, 861, 862, 864, 865, 866, 867, 868, 870, 872, 873, 874, 875, 876, 878, 879, 880, 882, 884, 885, 886, 888, 889, 890, 891, 892, 894, 895, 896, 897, 898, 900, 902, 903, 904, 905, 906, 908, 909, 910, 912, 914, 915, 916, 917, 918, 920, 921, 922, 924, 925, 926, 927, 928, 930, 931, 932, 933, 934, 935, 936, 938, 939, 940, 942, 944, 945, 946, 948, 950, 951, 952, 954, 955, 956, 957, 958, 959, 960, 962, 963, 964, 965, 966, 968, 969, 970, 972, 973, 974, 975, 976, 978, 980, 981, 982, 984, 985, 986, 987, 988, 990, 992, 993, 994, 995, 996, 998, 999, 1000, 1001, 1002, 1004, 1005, 1006, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1018, 1020, 1022, 1023, 1024, 1025, 1026, 1028, 1029, 1030, 1032, 1034, 1035, 1036, 1038, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1050, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1062, 1064, 1065, 1066, 1068, 1070, 1071, 1072, 1074, 1075, 1076, 1077, 1078, 1080, 1082, 1083, 1084, 1085, 1086, 1088, 1089, 1090, 1092, 1094, 1095, 1096, 1098, 1099, 1100, 1101, 1102, 1104, 1105, 1106, 1107, 1108, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1119, 1120, 1122, 1124, 1125, 1126, 1127, 1128, 1130, 1131, 1132, 1134, 1135, 1136, 1137, 1138, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1148, 1149, 1150, 1152, 1154, 1155, 1156, 1158, 1160, 1161, 1162, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1172, 1173, 1174, 1175, 1176, 1178, 1179, 1180, 1182, 1183, 1184, 1185, 1186, 1188, 1190, 1191, 1192, 1194, 1195, 1196, 1197, 1198, 1200, 1202, 1203, 1204, 1205, 1206, 1208, 1209, 1210, 1211, 1212, 1214, 1215, 1216, 1218, 1220, 1221, 1222, 1224, 1225, 1226, 1227, 1228, 1230, 1232, 1233, 1234, 1235, 1236, 1238, 1239, 1240, 1242, 1244, 1245, 1246, 1248, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1260, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1272, 1274, 1275, 1276, 1278, 1280, 1281, 1282, 1284, 1285, 1286, 1287, 1288, 1290, 1292, 1293, 1294, 1295, 1296, 1298, 1299, 1300, 1302, 1304, 1305, 1306, 1308, 1309, 1310, 1311, 1312, 1314, 1315, 1316, 1317, 1318, 1320, 1322, 1323, 1324, 1325, 1326, 1328, 1329, 1330, 1332, 1334, 1335, 1336, 1337, 1338, 1340, 1341, 1342, 1344, 1345, 1346, 1347, 1348, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1358, 1359, 1360, 1362, 1364, 1365, 1366, 1368, 1370, 1371, 1372, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1382, 1383, 1384, 1385, 1386, 1388, 1389, 1390, 1392, 1393, 1394, 1395, 1396, 1398, 1400, 1401, 1402, 1404, 1405, 1406, 1407, 1408, 1410, 1412, 1413, 1414, 1415, 1416, 1418, 1419, 1420, 1421, 1422, 1424, 1425, 1426, 1428, 1430, 1431, 1432, 1434, 1435, 1436, 1437, 1438, 1440, 1442, 1443, 1444, 1445, 1446, 1448, 1449, 1450, 1452, 1454, 1455, 1456, 1458, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1470, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1482, 1484, 1485, 1486, 1488, 1490, 1491, 1492, 1494, 1495, 1496, 1497, 1498, 1500, 1502, 1503, 1504, 1505, 1506, 1508, 1509, 1510, 1512, 1514, 1515, 1516, 1518, 1519, 1520, 1521, 1522, 1524, 1525, 1526, 1527, 1528, 1530, 1532, 1533, 1534, 1535, 1536, 1538, 1539, 1540, 1542, 1544, 1545, 1546, 1547, 1548, 1550, 1551, 1552, 1554, 1555, 1556, 1557, 1558, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1568, 1569, 1570, 1572, 1574, 1575, 1576, 1578, 1580, 1581, 1582, 1584, 1585, 1586, 1587, 1588, 1589, 1590, 1592, 1593, 1594, 1595, 1596, 1598, 1599, 1600, 1602, 1603, 1604, 1605, 1606, 1608, 1610, 1611, 1612, 1614, 1615, 1616, 1617, 1618, 1620, 1622, 1623, 1624, 1625, 1626, 1628, 1629, 1630, 1631, 1632, 1634, 1635, 1636, 1638, 1640, 1641, 1642, 1644, 1645, 1646, 1647, 1648, 1650, 1652, 1653, 1654, 1655, 1656, 1658, 1659, 1660, 1662, 1664, 1665, 1666, 1668, 1670, 1671, 1672, 1673, 1674, 1675, 1676, 1677, 1678, 1680, 1682, 1683, 1684, 1685, 1686, 1687, 1688, 1689, 1690, 1692, 1694, 1695, 1696, 1698, 1700, 1701, 1702, 1704, 1705, 1706, 1707, 1708, 1710, 1712, 1713, 1714, 1715, 1716, 1718, 1719, 1720, 1722, 1724, 1725, 1726, 1728, 1729, 1730, 1731, 1732, 1734, 1735, 1736, 1737, 1738, 1740, 1742, 1743, 1744, 1745, 1746, 1748, 1749, 1750, 1752, 1754, 1755, 1756, 1757, 1758, 1760, 1761, 1762, 1764, 1765, 1766, 1767, 1768, 1770, 1771, 1772, 1773, 1774, 1775, 1776, 1778, 1779, 1780, 1782, 1784, 1785, 1786, 1788, 1790, 1791, 1792, 1794, 1795, 1796, 1797, 1798, 1799, 1800, 1802, 1803, 1804, 1805, 1806, 1808, 1809, 1810, 1812, 1813, 1814, 1815, 1816, 1818, 1820, 1821, 1822, 1824, 1825, 1826, 1827, 1828, 1830, 1832, 1833, 1834, 1835, 1836, 1838, 1839, 1840, 1841, 1842, 1844, 1845, 1846, 1848, 1850, 1851, 1852, 1854, 1855, 1856, 1857, 1858, 1860, 1862, 1863, 1864, 1865, 1866, 1868, 1869, 1870, 1872, 1874, 1875, 1876, 1878, 1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1890, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899, 1900, 1902, 1904, 1905, 1906, 1908, 1910, 1911, 1912, 1914, 1915, 1916, 1917, 1918, 1920, 1922, 1923, 1924, 1925, 1926, 1928, 1929, 1930, 1932, 1934, 1935, 1936, 1938, 1939, 1940, 1941, 1942, 1944, 1945, 1946, 1947, 1948, 1950, 1952, 1953, 1954, 1955, 1956, 1958, 1959, 1960, 1962, 1964, 1965, 1966, 1967, 1968, 1970, 1971, 1972, 1974, 1975, 1976, 1977, 1978, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1988, 1989, 1990, 1992, 1994, 1995, 1996, 1998, 2000, 2001, 2002, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2012, 2013, 2014, 2015, 2016, 2018, 2019, 2020, 2022, 2023, 2024, 2025, 2026, 2028, 2030, 2031, 2032, 2034, 2035, 2036, 2037, 2038, 2040, 2042, 2043, 2044, 2045, 2046, 2048, 2049, 2050, 2051, 2052, 2054, 2055, 2056, 2058, 2060, 2061, 2062, 2064, 2065, 2066, 2067, 2068, 2070, 2072, 2073, 2074, 2075, 2076, 2078, 2079, 2080, 2082, 2084, 2085, 2086, 2088, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2100, 2102, 2103, 2104, 2105, 2106, 2107, 2108, 2109, 2110, 2112, 2114, 2115, 2116, 2118, 2120, 2121, 2122, 2124, 2125, 2126, 2127, 2128, 2130, 2132, 2133, 2134, 2135, 2136, 2138, 2139, 2140, 2142, 2144, 2145, 2146, 2148, 2149, 2150, 2151, 2152, 2154, 2155, 2156, 2157, 2158, 2160, 2162, 2163, 2164, 2165, 2166, 2168, 2169, 2170, 2172, 2174, 2175, 2176, 2177, 2178, 2180, 2181, 2182, 2184, 2185, 2186, 2187, 2188, 2190, 2191, 2192, 2193, 2194, 2195, 2196, 2198, 2199, 2200, 2202, 2204, 2205, 2206, 2208, 2210, 2211, 2212, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2222, 2223, 2224, 2225, 2226, 2228, 2229, 2230, 2232, 2233, 2234, 2235, 2236, 2238, 2240, 2241, 2242, 2244, 2245, 2246, 2247, 2248, 2250, 2252, 2253, 2254, 2255, 2256, 2258, 2259, 2260, 2261, 2262, 2264, 2265, 2266, 2268, 2270, 2271, 2272, 2274, 2275, 2276, 2277, 2278, 2280, 2282, 2283, 2284, 2285, 2286, 2288, 2289, 2290, 2292, 2294, 2295, 2296, 2298, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2310, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2322, 2324, 2325, 2326, 2328, 2330, 2331, 2332, 2334, 2335, 2336, 2337, 2338, 2340, 2342, 2343, 2344, 2345, 2346, 2348, 2349, 2350, 2352, 2354, 2355, 2356, 2358, 2359, 2360, 2361, 2362, 2364, 2365, 2366, 2367, 2368, 2370, 2372, 2373, 2374, 2375, 2376, 2378, 2379, 2380, 2382, 2384, 2385, 2386, 2387, 2388, 2390, 2391, 2392, 2394, 2395, 2396, 2397, 2398, 2400, 2401, 2402, 2403, 2404, 2405, 2406, 2408, 2409, 2410, 2412, 2414, 2415, 2416, 2418, 2420, 2421, 2422, 2424, 2425, 2426, 2427, 2428, 2429, 2430, 2432, 2433, 2434, 2435, 2436, 2438, 2439, 2440, 2442, 2443, 2444, 2445, 2446, 2448, 2450, 2451, 2452, 2454, 2455, 2456, 2457, 2458, 2460, 2462, 2463, 2464, 2465, 2466, 2468, 2469, 2470, 2471, 2472, 2474, 2475, 2476, 2478, 2480, 2481, 2482, 2484, 2485, 2486, 2487, 2488, 2490, 2492, 2493, 2494, 2495, 2496, 2498, 2499, 2500, 2502, 2504, 2505, 2506, 2508, 2510, 2511, 2512, 2513, 2514, 2515, 2516, 2517, 2518, 2520, 2522, 2523, 2524, 2525, 2526, 2527, 2528, 2529, 2530, 2532, 2534, 2535, 2536, 2538, 2540, 2541, 2542, 2544, 2545, 2546, 2547, 2548, 2550, 2552, 2553, 2554, 2555, 2556, 2558, 2559, 2560, 2562, 2564, 2565, 2566, 2568, 2569, 2570, 2571, 2572, 2574, 2575, 2576, 2577, 2578, 2580, 2582, 2583, 2584, 2585, 2586, 2588, 2589, 2590, 2592, 2594, 2595, 2596, 2597, 2598, 2600, 2601, 2602, 2604, 2605, 2606, 2607, 2608, 2610, 2611, 2612, 2613, 2614, 2615, 2616, 2618, 2619, 2620, 2622, 2624, 2625, 2626, 2628, 2630, 2631, 2632, 2634, 2635, 2636, 2637, 2638, 2639, 2640, 2642, 2643, 2644, 2645, 2646, 2648, 2649, 2650, 2652, 2653, 2654, 2655, 2656, 2658, 2660, 2661, 2662, 2664, 2665, 2666, 2667, 2668, 2670, 2672, 2673, 2674, 2675, 2676, 2678, 2679, 2680, 2681, 2682, 2684, 2685, 2686, 2688, 2690, 2691, 2692, 2694, 2695, 2696, 2697, 2698, 2700, 2702, 2703, 2704, 2705, 2706, 2708, 2709, 2710, 2712, 2714, 2715, 2716, 2718, 2720, 2721, 2722, 2723, 2724, 2725, 2726, 2727, 2728, 2730, 2732, 2733, 2734, 2735, 2736, 2737, 2738, 2739, 2740, 2742, 2744, 2745, 2746, 2748, 2750, 2751, 2752, 2754, 2755, 2756, 2757, 2758, 2760, 2762, 2763, 2764, 2765, 2766, 2768, 2769, 2770, 2772, 2774, 2775, 2776, 2778, 2779, 2780, 2781, 2782, 2784, 2785, 2786, 2787, 2788, 2790, 2792, 2793, 2794, 2795, 2796, 2798, 2799, 2800, 2802, 2804, 2805, 2806, 2807, 2808, 2810, 2811, 2812, 2814, 2815, 2816, 2817, 2818, 2820, 2821, 2822, 2823, 2824, 2825, 2826, 2828, 2829, 2830, 2832, 2834, 2835, 2836, 2838, 2840, 2841, 2842, 2844, 2845, 2846, 2847, 2848, 2849, 2850, 2852, 2853, 2854, 2855, 2856, 2858, 2859, 2860, 2862, 2863, 2864, 2865, 2866, 2868, 2870, 2871, 2872, 2874, 2875, 2876, 2877, 2878, 2880, 2882, 2883, 2884, 2885, 2886, 2888, 2889, 2890, 2891, 2892, 2894, 2895, 2896, 2898, 2900, 2901, 2902, 2904, 2905, 2906, 2907, 2908, 2910, 2912, 2913, 2914, 2915, 2916, 2918, 2919, 2920, 2922, 2924, 2925, 2926, 2928, 2930, 2931, 2932, 2933, 2934, 2935, 2936, 2937, 2938, 2940, 2942, 2943, 2944, 2945, 2946, 2947, 2948, 2949, 2950, 2952, 2954, 2955, 2956, 2958, 2960, 2961, 2962, 2964, 2965, 2966, 2967, 2968, 2970, 2972, 2973, 2974, 2975, 2976, 2978, 2979, 2980, 2982, 2984, 2985, 2986, 2988, 2989, 2990, 2991, 2992, 2994, 2995, 2996, 2997, 2998, 3000, 3002, 3003, 3004, 3005, 3006, 3008, 3009, 3010, 3012, 3014, 3015, 3016, 3017, 3018, 3020, 3021, 3022, 3024, 3025, 3026, 3027, 3028, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3038, 3039, 3040, 3042, 3044, 3045, 3046, 3048, 3050, 3051, 3052, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3062, 3063, 3064, 3065, 3066, 3068, 3069, 3070, 3072, 3073, 3074, 3075, 3076, 3078, 3080, 3081, 3082, 3084, 3085, 3086, 3087, 3088, 3090, 3092, 3093, 3094, 3095, 3096, 3098, 3099, 3100, 3101, 3102, 3104, 3105, 3106, 3108, 3110, 3111, 3112, 3114, 3115, 3116, 3117, 3118, 3120, 3122, 3123, 3124, 3125, 3126, 3128, 3129, 3130, 3132, 3134, 3135, 3136, 3138, 3140, 3141, 3142, 3143, 3144, 3145, 3146, 3147, 3148, 3150, 3152, 3153, 3154, 3155, 3156, 3157, 3158, 3159, 3160, 3162, 3164, 3165, 3166, 3168, 3170, 3171, 3172, 3174, 3175, 3176, 3177, 3178, 3180, 3182, 3183, 3184, 3185, 3186, 3188, 3189, 3190, 3192, 3194, 3195, 3196, 3198, 3199, 3200, 3201, 3202, 3204, 3205, 3206, 3207, 3208, 3210, 3212, 3213, 3214, 3215, 3216, 3218, 3219, 3220, 3222, 3224, 3225, 3226, 3227, 3228, 3230, 3231, 3232, 3234, 3235, 3236, 3237, 3238, 3240, 3241, 3242, 3243, 3244, 3245, 3246, 3248, 3249, 3250, 3252, 3254, 3255, 3256, 3258, 3260, 3261, 3262, 3264, 3265, 3266, 3267, 3268, 3269, 3270, 3272, 3273, 3274, 3275, 3276, 3278, 3279, 3280, 3282, 3283, 3284, 3285, 3286, 3288, 3290, 3291, 3292, 3294, 3295, 3296, 3297, 3298, 3300, 3302, 3303, 3304, 3305, 3306, 3308, 3309, 3310, 3311, 3312, 3314, 3315, 3316, 3318, 3320, 3321, 3322, 3324, 3325, 3326, 3327, 3328, 3330, 3332, 3333, 3334, 3335, 3336, 3338, 3339, 3340, 3342, 3344, 3345, 3346, 3348, 3350, 3351, 3352, 3353, 3354, 3355, 3356, 3357, 3358, 3360, 3362, 3363, 3364, 3365, 3366, 3367, 3368, 3369, 3370, 3372, 3374, 3375, 3376, 3378, 3380, 3381, 3382, 3384, 3385, 3386, 3387, 3388, 3390, 3392, 3393, 3394, 3395, 3396, 3398, 3399, 3400, 3402, 3404, 3405, 3406, 3408, 3409, 3410, 3411, 3412, 3414, 3415, 3416, 3417, 3418, 3420, 3422, 3423, 3424, 3425, 3426, 3428, 3429, 3430, 3432, 3434, 3435, 3436, 3437, 3438, 3440, 3441, 3442, 3444, 3445, 3446, 3447, 3448, 3450, 3451, 3452, 3453, 3454, 3455, 3456, 3458, 3459, 3460, 3462, 3464, 3465, 3466, 3468, 3470, 3471, 3472, 3474, 3475, 3476, 3477, 3478, 3479, 3480, 3482, 3483, 3484, 3485, 3486, 3488, 3489, 3490, 3492, 3493, 3494, 3495, 3496, 3498, 3500, 3501, 3502, 3504, 3505, 3506, 3507, 3508, 3510, 3512, 3513, 3514, 3515, 3516, 3518, 3519, 3520, 3521, 3522, 3524, 3525, 3526, 3528, 3530, 3531, 3532, 3534, 3535, 3536, 3537, 3538, 3540, 3542, 3543, 3544, 3545, 3546, 3548, 3549, 3550, 3552, 3554, 3555, 3556, 3558, 3560, 3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3570, 3572, 3573, 3574, 3575, 3576, 3577, 3578, 3579, 3580, 3582, 3584, 3585, 3586, 3588, 3590, 3591, 3592, 3594, 3595, 3596, 3597, 3598, 3600, 3602, 3603, 3604, 3605, 3606, 3608, 3609, 3610, 3612, 3614, 3615, 3616, 3618, 3619, 3620, 3621, 3622, 3624, 3625, 3626, 3627, 3628, 3630, 3632, 3633, 3634, 3635, 3636, 3638, 3639, 3640, 3642, 3644, 3645, 3646, 3647, 3648, 3650, 3651, 3652, 3654, 3655, 3656, 3657, 3658, 3660, 3661, 3662, 3663, 3664, 3665, 3666, 3668, 3669, 3670, 3672, 3674, 3675, 3676, 3678, 3680, 3681, 3682, 3684, 3685, 3686, 3687, 3688, 3689, 3690, 3692, 3693, 3694, 3695, 3696, 3698, 3699, 3700, 3702, 3703, 3704, 3705, 3706, 3708, 3710, 3711, 3712, 3714, 3715, 3716, 3717, 3718, 3720, 3722, 3723, 3724, 3725, 3726, 3728, 3729, 3730, 3731, 3732, 3734, 3735, 3736, 3738, 3740, 3741, 3742, 3744, 3745, 3746, 3747, 3748, 3750, 3752, 3753, 3754, 3755, 3756, 3758, 3759, 3760, 3762, 3764, 3765, 3766, 3768, 3770, 3771, 3772, 3773, 3774, 3775, 3776, 3777, 3778, 3780, 3782, 3783, 3784, 3785, 3786, 3787, 3788, 3789, 3790, 3792, 3794, 3795, 3796, 3798, 3800, 3801, 3802, 3804, 3805, 3806, 3807, 3808, 3810, 3812, 3813, 3814, 3815, 3816, 3818, 3819, 3820, 3822, 3824, 3825, 3826, 3828, 3829, 3830, 3831, 3832, 3834, 3835, 3836, 3837, 3838, 3840, 3842, 3843, 3844, 3845, 3846, 3848, 3849, 3850, 3852, 3854, 3855, 3856, 3857, 3858, 3860, 3861, 3862, 3864, 3865, 3866, 3867, 3868, 3870, 3871, 3872, 3873, 3874, 3875, 3876, 3878, 3879, 3880, 3882, 3884, 3885, 3886, 3888, 3890, 3891, 3892, 3894, 3895, 3896, 3897, 3898, 3899, 3900, 3902, 3903, 3904, 3905, 3906, 3908, 3909, 3910, 3912, 3913, 3914, 3915, 3916, 3918, 3920, 3921, 3922, 3924, 3925, 3926, 3927, 3928, 3930, 3932, 3933, 3934, 3935, 3936, 3938, 3939, 3940, 3941, 3942, 3944, 3945, 3946, 3948, 3950, 3951, 3952, 3954, 3955, 3956, 3957, 3958, 3960, 3962, 3963, 3964, 3965, 3966, 3968, 3969, 3970, 3972, 3974, 3975, 3976, 3978, 3980, 3981, 3982, 3983, 3984, 3985, 3986, 3987, 3988, 3990, 3992, 3993, 3994, 3995, 3996, 3997, 3998, 3999, 4000, 4002, 4004, 4005, 4006, 4008, 4010, 4011, 4012, 4014, 4015, 4016, 4017, 4018, 4020, 4022, 4023, 4024, 4025, 4026, 4028, 4029, 4030, 4032, 4034, 4035, 4036, 4038, 4039, 4040, 4041, 4042, 4044, 4045, 4046, 4047, 4048, 4050, 4052, 4053, 4054, 4055, 4056, 4058, 4059, 4060, 4062, 4064, 4065, 4066, 4067, 4068, 4070, 4071, 4072, 4074, 4075, 4076, 4077, 4078, 4080, 4081, 4082, 4083, 4084, 4085, 4086, 4088, 4089, 4090, 4092, 4094, 4095, 4096, 4098, 4100, 4101, 4102, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4112, 4113, 4114, 4115, 4116, 4118, 4119, 4120, 4122, 4123, 4124, 4125, 4126, 4128, 4130, 4131, 4132, 4134, 4135, 4136, 4137, 4138, 4140, 4142, 4143, 4144, 4145, 4146, 4148, 4149, 4150, 4151, 4152, 4154, 4155, 4156, 4158, 4160, 4161, 4162, 4164, 4165, 4166, 4167, 4168, 4170, 4172, 4173, 4174, 4175, 4176, 4178, 4179, 4180, 4182, 4184, 4185, 4186, 4188, 4190, 4191, 4192, 4193, 4194, 4195, 4196, 4197, 4198, 4200, 4202, 4203, 4204, 4205, 4206, 4207, 4208, 4209, 4210, 4212, 4214, 4215, 4216, 4218, 4220, 4221, 4222, 4224, 4225, 4226, 4227, 4228, 4230, 4232, 4233, 4234, 4235, 4236, 4238, 4239, 4240, 4242, 4244, 4245, 4246, 4248, 4249, 4250, 4251, 4252, 4254, 4255, 4256, 4257, 4258, 4260, 4262, 4263, 4264, 4265, 4266, 4268, 4269, 4270, 4272, 4274, 4275, 4276, 4277, 4278, 4280, 4281, 4282, 4284, 4285, 4286, 4287, 4288, 4290, 4291, 4292, 4293, 4294, 4295, 4296, 4298, 4299, 4300, 4302, 4304, 4305, 4306, 4308, 4310, 4311, 4312, 4314, 4315, 4316, 4317, 4318, 4319, 4320, 4322, 4323, 4324, 4325, 4326, 4328, 4329, 4330, 4332, 4333, 4334, 4335, 4336, 4338, 4340, 4341, 4342, 4344, 4345, 4346, 4347, 4348, 4350, 4352, 4353, 4354, 4355, 4356, 4358, 4359, 4360, 4361, 4362, 4364, 4365, 4366, 4368, 4370, 4371, 4372, 4374, 4375, 4376, 4377, 4378, 4380, 4382, 4383, 4384, 4385, 4386, 4388, 4389, 4390, 4392, 4394, 4395, 4396, 4398, 4400, 4401, 4402, 4403, 4404, 4405, 4406, 4407, 4408, 4410, 4412, 4413, 4414, 4415, 4416, 4417, 4418, 4419, 4420, 4422, 4424, 4425, 4426, 4428, 4430, 4431, 4432, 4434, 4435, 4436, 4437, 4438, 4440, 4442, 4443, 4444, 4445, 4446, 4448, 4449, 4450, 4452, 4454, 4455, 4456, 4458, 4459, 4460, 4461, 4462, 4464, 4465, 4466, 4467, 4468, 4470, 4472, 4473, 4474, 4475, 4476, 4478, 4479, 4480, 4482, 4484, 4485, 4486, 4487, 4488, 4490, 4491, 4492, 4494, 4495, 4496, 4497, 4498, 4500, 4501, 4502, 4503, 4504, 4505, 4506, 4508, 4509, 4510, 4512, 4514, 4515, 4516, 4518, 4520, 4521, 4522, 4524, 4525, 4526, 4527, 4528, 4529, 4530, 4532, 4533, 4534, 4535, 4536, 4538, 4539, 4540, 4542, 4543, 4544, 4545, 4546, 4548, 4550, 4551, 4552, 4554, 4555, 4556, 4557, 4558, 4560, 4562, 4563, 4564, 4565, 4566, 4568, 4569, 4570, 4571, 4572, 4574, 4575, 4576, 4578, 4580, 4581, 4582, 4584, 4585, 4586, 4587, 4588, 4590, 4592, 4593, 4594, 4595, 4596, 4598, 4599, 4600, 4602, 4604, 4605, 4606, 4608, 4610, 4611, 4612, 4613, 4614, 4615, 4616, 4617, 4618, 4620, 4622, 4623, 4624, 4625, 4626, 4627, 4628, 4629, 4630, 4632, 4634, 4635, 4636, 4638, 4640, 4641, 4642, 4644, 4645, 4646, 4647, 4648, 4650, 4652, 4653, 4654, 4655, 4656, 4658, 4659, 4660, 4662, 4664, 4665, 4666, 4668, 4669, 4670, 4671, 4672, 4674, 4675, 4676, 4677, 4678, 4680, 4682, 4683, 4684, 4685, 4686, 4688, 4689, 4690, 4692, 4694, 4695, 4696, 4697, 4698, 4700, 4701, 4702, 4704, 4705, 4706, 4707, 4708, 4710, 4711, 4712, 4713, 4714, 4715, 4716, 4718, 4719, 4720, 4722, 4724, 4725, 4726, 4728, 4730, 4731, 4732, 4734, 4735, 4736, 4737, 4738, 4739, 4740, 4742, 4743, 4744, 4745, 4746, 4748, 4749, 4750, 4752, 4753, 4754, 4755, 4756, 4758, 4760, 4761, 4762, 4764, 4765, 4766, 4767, 4768, 4770, 4772, 4773, 4774, 4775, 4776, 4778, 4779, 4780, 4781, 4782, 4784, 4785, 4786, 4788, 4790, 4791, 4792, 4794, 4795, 4796, 4797, 4798, 4800, 4802, 4803, 4804, 4805, 4806, 4808, 4809, 4810, 4812, 4814, 4815, 4816, 4818, 4820, 4821, 4822, 4823, 4824, 4825, 4826, 4827, 4828, 4830, 4832, 4833, 4834, 4835, 4836, 4837, 4838, 4839, 4840, 4842, 4844, 4845, 4846, 4848, 4850, 4851, 4852, 4854, 4855, 4856, 4857, 4858, 4860, 4862, 4863, 4864, 4865, 4866, 4868, 4869, 4870, 4872, 4874, 4875, 4876, 4878, 4879, 4880, 4881, 4882, 4884, 4885, 4886, 4887, 4888, 4890, 4892, 4893, 4894, 4895, 4896, 4898, 4899, 4900, 4902, 4904, 4905, 4906, 4907, 4908, 4910, 4911, 4912, 4914, 4915, 4916, 4917, 4918, 4920, 4921, 4922, 4923, 4924, 4925, 4926, 4928, 4929, 4930, 4932, 4934, 4935, 4936, 4938, 4940, 4941, 4942, 4944, 4945, 4946, 4947, 4948, 4949, 4950, 4952, 4953, 4954, 4955, 4956, 4958, 4959, 4960, 4962, 4963, 4964, 4965, 4966, 4968, 4970, 4971, 4972, 4974, 4975, 4976, 4977, 4978, 4980, 4982, 4983, 4984, 4985, 4986, 4988, 4989, 4990, 4991, 4992, 4994, 4995, 4996, 4998, 5000, 5001, 5002, 5004, 5005, 5006, 5007, 5008, 5010, 5012, 5013, 5014, 5015, 5016, 5018, 5019, 5020, 5022, 5024, 5025, 5026, 5028, 5030, 5031, 5032, 5033, 5034, 5035, 5036, 5037, 5038, 5040, 5042, 5043, 5044, 5045, 5046, 5047, 5048, 5049, 5050, 5052, 5054, 5055, 5056, 5058, 5060, 5061, 5062, 5064, 5065, 5066, 5067, 5068, 5070, 5072, 5073, 5074, 5075, 5076, 5078, 5079, 5080, 5082, 5084, 5085, 5086, 5088, 5089, 5090, 5091, 5092, 5094, 5095, 5096, 5097, 5098, 5100, 5102, 5103, 5104, 5105, 5106, 5108, 5109, 5110, 5112, 5114, 5115, 5116, 5117, 5118, 5120, 5121, 5122, 5124, 5125, 5126, 5127, 5128, 5130, 5131, 5132, 5133, 5134, 5135, 5136, 5138, 5139, 5140, 5142, 5144, 5145, 5146, 5148, 5150, 5151, 5152, 5154, 5155, 5156, 5157, 5158, 5159, 5160, 5162, 5163, 5164, 5165, 5166, 5168, 5169, 5170, 5172, 5173, 5174, 5175, 5176, 5178, 5180, 5181, 5182, 5184, 5185, 5186, 5187, 5188, 5190, 5192, 5193, 5194, 5195, 5196, 5198, 5199, 5200, 5201, 5202, 5204, 5205, 5206, 5208, 5210, 5211, 5212, 5214, 5215, 5216, 5217, 5218, 5220, 5222, 5223, 5224, 5225, 5226, 5228, 5229, 5230, 5232, 5234, 5235, 5236, 5238, 5240, 5241, 5242, 5243, 5244, 5245, 5246, 5247, 5248, 5250, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5259, 5260, 5262, 5264, 5265, 5266, 5268, 5270, 5271, 5272, 5274, 5275, 5276, 5277, 5278, 5280, 5282, 5283, 5284, 5285, 5286, 5288, 5289, 5290, 5292, 5294, 5295, 5296, 5298, 5299, 5300, 5301, 5302, 5304, 5305, 5306, 5307, 5308, 5310, 5312, 5313, 5314, 5315, 5316, 5318, 5319, 5320, 5322, 5324, 5325, 5326, 5327, 5328, 5330, 5331, 5332, 5334, 5335, 5336, 5337, 5338, 5340, 5341, 5342, 5343, 5344, 5345, 5346, 5348, 5349, 5350, 5352, 5354, 5355, 5356, 5358, 5360, 5361, 5362, 5364, 5365, 5366, 5367, 5368, 5369, 5370, 5372, 5373, 5374, 5375, 5376, 5378, 5379, 5380, 5382, 5383, 5384, 5385, 5386, 5388, 5390, 5391, 5392, 5394, 5395, 5396, 5397, 5398, 5400, 5402, 5403, 5404, 5405, 5406, 5408, 5409, 5410, 5411, 5412, 5414, 5415, 5416, 5418, 5420, 5421, 5422, 5424, 5425, 5426, 5427, 5428, 5430, 5432, 5433, 5434, 5435, 5436, 5438, 5439, 5440, 5442, 5444, 5445, 5446, 5448, 5450, 5451, 5452, 5453, 5454, 5455, 5456, 5457, 5458, 5460, 5462, 5463, 5464, 5465, 5466, 5467, 5468, 5469, 5470, 5472, 5474, 5475, 5476, 5478, 5480, 5481, 5482, 5484, 5485, 5486, 5487, 5488, 5490, 5492, 5493, 5494, 5495, 5496, 5498, 5499, 5500, 5502, 5504, 5505, 5506, 5508, 5509, 5510, 5511, 5512, 5514, 5515, 5516, 5517, 5518, 5520, 5522, 5523, 5524, 5525, 5526, 5528, 5529, 5530, 5532, 5534, 5535, 5536, 5537, 5538, 5540, 5541, 5542, 5544, 5545, 5546, 5547, 5548, 5550, 5551, 5552, 5553, 5554, 5555, 5556, 5558, 5559, 5560, 5562, 5564, 5565, 5566, 5568, 5570, 5571, 5572, 5574, 5575, 5576, 5577, 5578, 5579, 5580, 5582, 5583, 5584, 5585, 5586, 5588, 5589, 5590, 5592, 5593, 5594, 5595, 5596, 5598, 5600, 5601, 5602, 5604, 5605, 5606, 5607, 5608, 5610, 5612, 5613, 5614, 5615, 5616, 5618, 5619, 5620, 5621, 5622, 5624, 5625, 5626, 5628, 5630, 5631, 5632, 5634, 5635, 5636, 5637, 5638, 5640, 5642, 5643, 5644, 5645, 5646, 5648, 5649, 5650, 5652, 5654, 5655, 5656, 5658, 5660, 5661, 5662, 5663, 5664, 5665, 5666, 5667, 5668, 5670, 5672, 5673, 5674, 5675, 5676, 5677, 5678, 5679, 5680, 5682, 5684, 5685, 5686, 5688, 5690, 5691, 5692, 5694, 5695, 5696, 5697, 5698, 5700, 5702, 5703, 5704, 5705, 5706, 5708, 5709, 5710, 5712, 5714, 5715, 5716, 5718, 5719, 5720, 5721, 5722, 5724, 5725, 5726, 5727, 5728, 5730, 5732, 5733, 5734, 5735, 5736, 5738, 5739, 5740, 5742, 5744, 5745, 5746, 5747, 5748, 5750, 5751, 5752, 5754, 5755, 5756, 5757, 5758, 5760, 5761, 5762, 5763, 5764, 5765, 5766, 5768, 5769, 5770, 5772, 5774, 5775, 5776, 5778, 5780, 5781, 5782, 5784, 5785, 5786, 5787, 5788, 5789, 5790, 5792, 5793, 5794, 5795, 5796, 5798, 5799, 5800, 5802, 5803, 5804, 5805, 5806, 5808, 5810, 5811, 5812, 5814, 5815, 5816, 5817, 5818, 5820, 5822, 5823, 5824, 5825, 5826, 5828, 5829, 5830, 5831, 5832, 5834, 5835, 5836, 5838, 5840, 5841, 5842, 5844, 5845, 5846, 5847, 5848, 5850, 5852, 5853, 5854, 5855, 5856, 5858, 5859, 5860, 5862, 5864, 5865, 5866, 5868, 5870, 5871, 5872, 5873, 5874, 5875, 5876, 5877, 5878, 5880, 5882, 5883, 5884, 5885, 5886, 5887, 5888, 5889, 5890, 5892, 5894, 5895, 5896, 5898, 5900, 5901, 5902, 5904, 5905, 5906, 5907, 5908, 5910, 5912, 5913, 5914, 5915, 5916, 5918, 5919, 5920, 5922, 5924, 5925, 5926, 5928, 5929, 5930, 5931, 5932, 5934, 5935, 5936, 5937, 5938, 5940, 5942, 5943, 5944, 5945, 5946, 5948, 5949, 5950, 5952, 5954, 5955, 5956, 5957, 5958, 5960, 5961, 5962, 5964, 5965, 5966, 5967, 5968, 5970, 5971, 5972, 5973, 5974, 5975, 5976, 5978, 5979, 5980, 5982, 5984, 5985, 5986, 5988, 5990, 5991, 5992, 5994, 5995, 5996, 5997, 5998, 5999, 6000, 6002, 6003, 6004, 6005, 6006, 6008, 6009, 6010, 6012, 6013, 6014, 6015, 6016, 6018, 6020, 6021, 6022, 6024, 6025, 6026, 6027, 6028, 6030, 6032, 6033, 6034, 6035, 6036, 6038, 6039, 6040, 6041, 6042, 6044, 6045, 6046, 6048, 6050, 6051, 6052, 6054, 6055, 6056, 6057, 6058, 6060, 6062, 6063, 6064, 6065, 6066, 6068, 6069, 6070, 6072, 6074, 6075, 6076, 6078, 6080, 6081, 6082, 6083, 6084, 6085, 6086, 6087, 6088, 6090, 6092, 6093, 6094, 6095, 6096, 6097, 6098, 6099, 6100, 6102, 6104, 6105, 6106, 6108, 6110, 6111, 6112, 6114, 6115, 6116, 6117, 6118, 6120, 6122, 6123, 6124, 6125, 6126, 6128, 6129, 6130, 6132, 6134, 6135, 6136, 6138, 6139, 6140, 6141, 6142, 6144, 6145, 6146, 6147, 6148, 6150, 6152, 6153, 6154, 6155, 6156, 6158, 6159, 6160, 6162, 6164, 6165, 6166, 6167, 6168, 6170, 6171, 6172, 6174, 6175, 6176, 6177, 6178, 6180, 6181, 6182, 6183, 6184, 6185, 6186, 6188, 6189, 6190, 6192, 6194, 6195, 6196, 6198, 6200, 6201, 6202, 6204, 6205, 6206, 6207, 6208, 6209, 6210, 6212, 6213, 6214, 6215, 6216, 6218, 6219, 6220, 6222, 6223, 6224, 6225, 6226, 6228, 6230, 6231, 6232, 6234, 6235, 6236, 6237, 6238, 6240, 6242, 6243, 6244, 6245, 6246, 6248, 6249, 6250, 6251, 6252, 6254, 6255, 6256, 6258, 6260, 6261, 6262, 6264, 6265, 6266, 6267, 6268, 6270, 6272, 6273, 6274, 6275, 6276, 6278, 6279, 6280, 6282, 6284, 6285, 6286, 6288, 6290, 6291, 6292, 6293, 6294, 6295, 6296, 6297, 6298, 6300, 6302, 6303, 6304, 6305, 6306, 6307, 6308, 6309, 6310, 6312, 6314, 6315, 6316, 6318, 6320, 6321, 6322, 6324, 6325, 6326, 6327, 6328, 6330, 6332, 6333, 6334, 6335, 6336, 6338, 6339, 6340, 6342, 6344, 6345, 6346, 6348, 6349, 6350, 6351, 6352, 6354, 6355, 6356, 6357, 6358, 6360, 6362, 6363, 6364, 6365, 6366, 6368, 6369, 6370, 6372, 6374, 6375, 6376, 6377, 6378, 6380, 6381, 6382, 6384, 6385, 6386, 6387, 6388, 6390, 6391, 6392, 6393, 6394, 6395, 6396, 6398, 6399, 6400, 6402, 6404, 6405, 6406, 6408, 6410, 6411, 6412, 6414, 6415, 6416, 6417, 6418, 6419, 6420, 6422, 6423, 6424, 6425, 6426, 6428, 6429, 6430, 6432, 6433, 6434, 6435, 6436, 6438, 6440, 6441, 6442, 6444, 6445, 6446, 6447, 6448, 6450, 6452, 6453, 6454, 6455, 6456, 6458, 6459, 6460, 6461, 6462, 6464, 6465, 6466, 6468, 6470, 6471, 6472, 6474, 6475, 6476, 6477, 6478, 6480, 6482, 6483, 6484, 6485, 6486, 6488, 6489, 6490, 6492, 6494, 6495, 6496, 6498, 6500, 6501, 6502, 6503, 6504, 6505, 6506, 6507, 6508, 6510, 6512, 6513, 6514, 6515, 6516, 6517, 6518, 6519, 6520, 6522, 6524, 6525, 6526, 6528, 6530, 6531, 6532, 6534, 6535, 6536, 6537, 6538, 6540, 6542, 6543, 6544, 6545, 6546, 6548, 6549, 6550, 6552, 6554, 6555, 6556, 6558, 6559, 6560, 6561, 6562, 6564, 6565, 6566, 6567, 6568, 6570, 6572, 6573, 6574, 6575, 6576, 6578, 6579, 6580, 6582, 6584, 6585, 6586, 6587, 6588, 6590, 6591, 6592, 6594, 6595, 6596, 6597, 6598, 6600, 6601, 6602, 6603, 6604, 6605, 6606, 6608, 6609, 6610, 6612, 6614, 6615, 6616, 6618, 6620, 6621, 6622, 6624, 6625, 6626, 6627, 6628, 6629, 6630, 6632, 6633, 6634, 6635, 6636, 6638, 6639, 6640, 6642, 6643, 6644, 6645, 6646, 6648, 6650, 6651, 6652, 6654, 6655, 6656, 6657, 6658, 6660, 6662, 6663, 6664, 6665, 6666, 6668, 6669, 6670, 6671, 6672, 6674, 6675, 6676, 6678, 6680, 6681, 6682, 6684, 6685, 6686, 6687, 6688, 6690, 6692, 6693, 6694, 6695, 6696, 6698, 6699, 6700, 6702, 6704, 6705, 6706, 6708, 6710, 6711, 6712, 6713, 6714, 6715, 6716, 6717, 6718, 6720, 6722, 6723, 6724, 6725, 6726, 6727, 6728, 6729, 6730, 6732, 6734, 6735, 6736, 6738, 6740, 6741, 6742, 6744, 6745, 6746, 6747, 6748, 6750, 6752, 6753, 6754, 6755, 6756, 6758, 6759, 6760, 6762, 6764, 6765, 6766, 6768, 6769, 6770, 6771, 6772, 6774, 6775, 6776, 6777, 6778, 6780, 6782, 6783, 6784, 6785, 6786, 6788, 6789, 6790, 6792, 6794, 6795, 6796, 6797, 6798, 6800, 6801, 6802, 6804, 6805, 6806, 6807, 6808, 6810, 6811, 6812, 6813, 6814, 6815, 6816, 6818, 6819, 6820, 6822, 6824, 6825, 6826, 6828, 6830, 6831, 6832, 6834, 6835, 6836, 6837, 6838, 6839, 6840, 6842, 6843, 6844, 6845, 6846, 6848, 6849, 6850, 6852, 6853, 6854, 6855, 6856, 6858, 6860, 6861, 6862, 6864, 6865, 6866, 6867, 6868, 6870, 6872, 6873, 6874, 6875, 6876, 6878, 6879, 6880, 6881, 6882, 6884, 6885, 6886, 6888, 6890, 6891, 6892, 6894, 6895, 6896, 6897, 6898, 6900, 6902, 6903, 6904, 6905, 6906, 6908, 6909, 6910, 6912, 6914, 6915, 6916, 6918, 6920, 6921, 6922, 6923, 6924, 6925, 6926, 6927, 6928, 6930, 6932, 6933, 6934, 6935, 6936, 6937, 6938, 6939, 6940, 6942, 6944, 6945, 6946, 6948, 6950, 6951, 6952, 6954, 6955, 6956, 6957, 6958, 6960, 6962, 6963, 6964, 6965, 6966, 6968, 6969, 6970, 6972, 6974, 6975, 6976, 6978, 6979, 6980, 6981, 6982, 6984, 6985, 6986, 6987, 6988, 6990, 6992, 6993, 6994, 6995, 6996, 6998, 6999, 7000, 7002, 7004, 7005, 7006, 7007, 7008, 7010, 7011, 7012, 7014, 7015, 7016, 7017, 7018, 7020, 7021, 7022, 7023, 7024, 7025, 7026, 7028, 7029, 7030, 7032, 7034, 7035, 7036, 7038, 7040, 7041, 7042, 7044, 7045, 7046, 7047, 7048, 7049, 7050, 7052, 7053, 7054, 7055, 7056, 7058, 7059, 7060, 7062, 7063, 7064, 7065, 7066, 7068, 7070, 7071, 7072, 7074, 7075, 7076, 7077, 7078, 7080, 7082, 7083, 7084, 7085, 7086, 7088, 7089, 7090, 7091, 7092, 7094, 7095, 7096, 7098, 7100, 7101, 7102, 7104, 7105, 7106, 7107, 7108, 7110, 7112, 7113, 7114, 7115, 7116, 7118, 7119, 7120, 7122, 7124, 7125, 7126, 7128, 7130, 7131, 7132, 7133, 7134, 7135, 7136, 7137, 7138, 7140, 7142, 7143, 7144, 7145, 7146, 7147, 7148, 7149, 7150, 7152, 7154, 7155, 7156, 7158, 7160, 7161, 7162, 7164, 7165, 7166, 7167, 7168, 7170, 7172, 7173, 7174, 7175, 7176, 7178, 7179, 7180, 7182, 7184, 7185, 7186, 7188, 7189, 7190, 7191, 7192, 7194, 7195, 7196, 7197, 7198, 7200, 7202, 7203, 7204, 7205, 7206, 7208, 7209, 7210, 7212, 7214, 7215, 7216, 7217, 7218, 7220, 7221, 7222, 7224, 7225, 7226, 7227, 7228, 7230, 7231, 7232, 7233, 7234, 7235, 7236, 7238, 7239, 7240, 7242, 7244, 7245, 7246, 7248, 7250, 7251, 7252, 7254, 7255, 7256, 7257, 7258, 7259, 7260, 7262, 7263, 7264, 7265, 7266, 7268, 7269, 7270, 7272, 7273, 7274, 7275, 7276, 7278, 7280, 7281, 7282, 7284, 7285, 7286, 7287, 7288, 7290, 7292, 7293, 7294, 7295, 7296, 7298, 7299, 7300, 7301, 7302, 7304, 7305, 7306, 7308, 7310, 7311, 7312, 7314, 7315, 7316, 7317, 7318, 7320, 7322, 7323, 7324, 7325, 7326, 7328, 7329, 7330, 7332, 7334, 7335, 7336, 7338, 7340, 7341, 7342, 7343, 7344, 7345, 7346, 7347, 7348, 7350, 7352, 7353, 7354, 7355, 7356, 7357, 7358, 7359, 7360, 7362, 7364, 7365, 7366, 7368, 7370, 7371, 7372, 7374, 7375, 7376, 7377, 7378, 7380, 7382, 7383, 7384, 7385, 7386, 7388, 7389, 7390, 7392, 7394, 7395, 7396, 7398, 7399, 7400, 7401, 7402, 7404, 7405, 7406, 7407, 7408, 7410, 7412, 7413, 7414, 7415, 7416, 7418, 7419, 7420, 7422, 7424, 7425, 7426, 7427, 7428, 7430, 7431, 7432, 7434, 7435, 7436, 7437, 7438, 7440, 7441, 7442, 7443, 7444, 7445, 7446, 7448, 7449, 7450, 7452, 7454, 7455, 7456, 7458, 7460, 7461, 7462, 7464, 7465, 7466, 7467, 7468, 7469, 7470, 7472, 7473, 7474, 7475, 7476, 7478, 7479, 7480, 7482, 7483, 7484, 7485, 7486, 7488, 7490, 7491, 7492, 7494, 7495, 7496, 7497, 7498, 7500, 7502, 7503, 7504, 7505, 7506, 7508, 7509, 7510, 7511, 7512, 7514, 7515, 7516, 7518, 7520, 7521, 7522, 7524, 7525, 7526, 7527, 7528, 7530, 7532, 7533, 7534, 7535, 7536, 7538, 7539, 7540, 7542, 7544, 7545, 7546, 7548, 7550, 7551, 7552, 7553, 7554, 7555, 7556, 7557, 7558, 7560, 7562, 7563, 7564, 7565, 7566, 7567, 7568, 7569, 7570, 7572, 7574, 7575, 7576, 7578, 7580, 7581, 7582, 7584, 7585, 7586, 7587, 7588, 7590, 7592, 7593, 7594, 7595, 7596, 7598, 7599, 7600, 7602, 7604, 7605, 7606, 7608, 7609, 7610, 7611, 7612, 7614, 7615, 7616, 7617, 7618, 7620, 7622, 7623, 7624, 7625, 7626, 7628, 7629, 7630, 7632, 7634, 7635, 7636, 7637, 7638, 7640, 7641, 7642, 7644, 7645, 7646, 7647, 7648, 7650, 7651, 7652, 7653, 7654, 7655, 7656, 7658, 7659, 7660, 7662, 7664, 7665, 7666, 7668, 7670, 7671, 7672, 7674, 7675, 7676, 7677, 7678, 7679, 7680, 7682, 7683, 7684, 7685, 7686, 7688, 7689, 7690, 7692, 7693, 7694, 7695, 7696, 7698, 7700, 7701, 7702, 7704, 7705, 7706, 7707, 7708, 7710, 7712, 7713, 7714, 7715, 7716, 7718, 7719, 7720, 7721, 7722, 7724, 7725, 7726, 7728, 7730, 7731, 7732, 7734, 7735, 7736, 7737, 7738, 7740, 7742, 7743, 7744, 7745, 7746, 7748, 7749, 7750, 7752, 7754, 7755, 7756, 7758, 7760, 7761, 7762, 7763, 7764, 7765, 7766, 7767, 7768, 7770, 7772, 7773, 7774, 7775, 7776, 7777, 7778, 7779, 7780, 7782, 7784, 7785, 7786, 7788, 7790, 7791, 7792, 7794, 7795, 7796, 7797, 7798, 7800, 7802, 7803, 7804, 7805, 7806, 7808, 7809, 7810, 7812, 7814, 7815, 7816, 7818, 7819, 7820, 7821, 7822, 7824, 7825, 7826, 7827, 7828, 7830, 7832, 7833, 7834, 7835, 7836, 7838, 7839, 7840, 7842, 7844, 7845, 7846, 7847, 7848, 7850, 7851, 7852, 7854, 7855, 7856, 7857, 7858, 7860, 7861, 7862, 7863, 7864, 7865, 7866, 7868, 7869, 7870, 7872, 7874, 7875, 7876, 7878, 7880, 7881, 7882, 7884, 7885, 7886, 7887, 7888, 7889, 7890, 7892, 7893, 7894, 7895, 7896, 7898, 7899, 7900, 7902, 7903, 7904, 7905, 7906, 7908, 7910, 7911, 7912, 7914, 7915, 7916, 7917, 7918, 7920, 7922, 7923, 7924, 7925, 7926, 7928, 7929, 7930, 7931, 7932, 7934, 7935, 7936, 7938, 7940, 7941, 7942, 7944, 7945, 7946, 7947, 7948, 7950, 7952, 7953, 7954, 7955, 7956, 7958, 7959, 7960, 7962, 7964, 7965, 7966, 7968, 7970, 7971, 7972, 7973, 7974, 7975, 7976, 7977, 7978, 7980, 7982, 7983, 7984, 7985, 7986, 7987, 7988, 7989, 7990, 7992, 7994, 7995, 7996, 7998, 8000, 8001, 8002, 8004, 8005, 8006, 8007, 8008, 8010, 8012, 8013, 8014, 8015, 8016, 8018, 8019, 8020, 8022, 8024, 8025, 8026, 8028, 8029, 8030, 8031, 8032, 8034, 8035, 8036, 8037, 8038, 8040, 8042, 8043, 8044, 8045, 8046, 8048, 8049, 8050, 8052, 8054, 8055, 8056, 8057, 8058, 8060, 8061, 8062, 8064, 8065, 8066, 8067, 8068, 8070, 8071, 8072, 8073, 8074, 8075, 8076, 8078, 8079, 8080, 8082, 8084, 8085, 8086, 8088, 8090, 8091, 8092, 8094, 8095, 8096, 8097, 8098, 8099, 8100, 8102, 8103, 8104, 8105, 8106, 8108, 8109, 8110, 8112, 8113, 8114, 8115, 8116, 8118, 8120, 8121, 8122, 8124, 8125, 8126, 8127, 8128, 8130, 8132, 8133, 8134, 8135, 8136, 8138, 8139, 8140, 8141, 8142, 8144, 8145, 8146, 8148, 8150, 8151, 8152, 8154, 8155, 8156, 8157, 8158, 8160, 8162, 8163, 8164, 8165, 8166, 8168, 8169, 8170, 8172, 8174, 8175, 8176, 8178, 8180, 8181, 8182, 8183, 8184, 8185, 8186, 8187, 8188, 8190, 8192, 8193, 8194, 8195, 8196, 8197, 8198, 8199, 8200, 8202, 8204, 8205, 8206, 8208, 8210, 8211, 8212, 8214, 8215, 8216, 8217, 8218, 8220, 8222, 8223, 8224, 8225, 8226, 8228, 8229, 8230, 8232, 8234, 8235, 8236, 8238, 8239, 8240, 8241, 8242, 8244, 8245, 8246, 8247, 8248, 8250, 8252, 8253, 8254, 8255, 8256, 8258, 8259, 8260, 8262, 8264, 8265, 8266, 8267, 8268, 8270, 8271, 8272, 8274, 8275, 8276, 8277, 8278, 8280, 8281, 8282, 8283, 8284, 8285, 8286, 8288, 8289, 8290, 8292, 8294, 8295, 8296, 8298, 8300, 8301, 8302, 8304, 8305, 8306, 8307, 8308, 8309, 8310, 8312, 8313, 8314, 8315, 8316, 8318, 8319, 8320, 8322, 8323, 8324, 8325, 8326, 8328, 8330, 8331, 8332, 8334, 8335, 8336, 8337, 8338, 8340, 8342, 8343, 8344, 8345, 8346, 8348, 8349, 8350, 8351, 8352, 8354, 8355, 8356, 8358, 8360, 8361, 8362, 8364, 8365, 8366, 8367, 8368, 8370, 8372, 8373, 8374, 8375, 8376, 8378, 8379, 8380, 8382, 8384, 8385, 8386, 8388, 8390, 8391, 8392, 8393, 8394, 8395, 8396, 8397, 8398, 8400, 8402, 8403, 8404, 8405, 8406, 8407, 8408, 8409, 8410, 8412, 8414, 8415, 8416, 8418, 8420, 8421, 8422, 8424, 8425, 8426, 8427, 8428, 8430, 8432, 8433, 8434, 8435, 8436, 8438, 8439, 8440, 8442, 8444, 8445, 8446, 8448, 8449, 8450, 8451, 8452, 8454, 8455, 8456, 8457, 8458, 8460, 8462, 8463, 8464, 8465, 8466, 8468, 8469, 8470, 8472, 8474, 8475, 8476, 8477, 8478, 8480, 8481, 8482, 8484, 8485, 8486, 8487, 8488, 8490, 8491, 8492, 8493, 8494, 8495, 8496, 8498, 8499, 8500, 8502, 8504, 8505, 8506, 8508, 8510, 8511, 8512, 8514, 8515, 8516, 8517, 8518, 8519, 8520, 8522, 8523, 8524, 8525, 8526, 8528, 8529, 8530, 8532, 8533, 8534, 8535, 8536, 8538, 8540, 8541, 8542, 8544, 8545, 8546, 8547, 8548, 8550, 8552, 8553, 8554, 8555, 8556, 8558, 8559, 8560, 8561, 8562, 8564, 8565, 8566, 8568, 8570, 8571, 8572, 8574, 8575, 8576, 8577, 8578, 8580, 8582, 8583, 8584, 8585, 8586, 8588, 8589, 8590, 8592, 8594, 8595, 8596, 8598, 8600, 8601, 8602, 8603, 8604, 8605, 8606, 8607, 8608, 8610, 8612, 8613, 8614, 8615, 8616, 8617, 8618, 8619, 8620, 8622, 8624, 8625, 8626, 8628, 8630, 8631, 8632, 8634, 8635, 8636, 8637, 8638, 8640, 8642, 8643, 8644, 8645, 8646, 8648, 8649, 8650, 8652, 8654, 8655, 8656, 8658, 8659, 8660, 8661, 8662, 8664, 8665, 8666, 8667, 8668, 8670, 8672, 8673, 8674, 8675, 8676, 8678, 8679, 8680, 8682, 8684, 8685, 8686, 8687, 8688, 8690, 8691, 8692, 8694, 8695, 8696, 8697, 8698, 8700, 8701, 8702, 8703, 8704, 8705, 8706, 8708, 8709, 8710, 8712, 8714, 8715, 8716, 8718, 8720, 8721, 8722, 8724, 8725, 8726, 8727, 8728, 8729, 8730, 8732, 8733, 8734, 8735, 8736, 8738, 8739, 8740, 8742, 8743, 8744, 8745, 8746, 8748, 8750, 8751, 8752, 8754, 8755, 8756, 8757, 8758, 8760, 8762, 8763, 8764, 8765, 8766, 8768, 8769, 8770, 8771, 8772, 8774, 8775, 8776, 8778, 8780, 8781, 8782, 8784, 8785, 8786, 8787, 8788, 8790, 8792, 8793, 8794, 8795, 8796, 8798, 8799, 8800, 8802, 8804, 8805, 8806, 8808, 8810, 8811, 8812, 8813, 8814, 8815, 8816, 8817, 8818, 8820, 8822, 8823, 8824, 8825, 8826, 8827, 8828, 8829, 8830, 8832, 8834, 8835, 8836, 8838, 8840, 8841, 8842, 8844, 8845, 8846, 8847, 8848, 8850, 8852, 8853, 8854, 8855, 8856, 8858, 8859, 8860, 8862, 8864, 8865, 8866, 8868, 8869, 8870, 8871, 8872, 8874, 8875, 8876, 8877, 8878, 8880, 8882, 8883, 8884, 8885, 8886, 8888, 8889, 8890, 8892, 8894, 8895, 8896, 8897, 8898, 8900, 8901, 8902, 8904, 8905, 8906, 8907, 8908, 8910, 8911, 8912, 8913, 8914, 8915, 8916, 8918, 8919, 8920, 8922, 8924, 8925, 8926, 8928, 8930, 8931, 8932, 8934, 8935, 8936, 8937, 8938, 8939, 8940, 8942, 8943, 8944, 8945, 8946, 8948, 8949, 8950, 8952, 8953, 8954, 8955, 8956, 8958, 8960, 8961, 8962, 8964, 8965, 8966, 8967, 8968, 8970, 8972, 8973, 8974, 8975, 8976, 8978, 8979, 8980, 8981, 8982, 8984, 8985, 8986, 8988, 8990, 8991, 8992, 8994, 8995, 8996, 8997, 8998, 9000, 9002, 9003, 9004, 9005, 9006, 9008, 9009, 9010, 9012, 9014, 9015, 9016, 9018, 9020, 9021, 9022, 9023, 9024, 9025, 9026, 9027, 9028, 9030, 9032, 9033, 9034, 9035, 9036, 9037, 9038, 9039, 9040, 9042, 9044, 9045, 9046, 9048, 9050, 9051, 9052, 9054, 9055, 9056, 9057, 9058, 9060, 9062, 9063, 9064, 9065, 9066, 9068, 9069, 9070, 9072, 9074, 9075, 9076, 9078, 9079, 9080, 9081, 9082, 9084, 9085, 9086, 9087, 9088, 9090, 9092, 9093, 9094, 9095, 9096, 9098, 9099, 9100, 9102, 9104, 9105, 9106, 9107, 9108, 9110, 9111, 9112, 9114, 9115, 9116, 9117, 9118, 9120, 9121, 9122, 9123, 9124, 9125, 9126, 9128, 9129, 9130, 9132, 9134, 9135, 9136, 9138, 9140, 9141, 9142, 9144, 9145, 9146, 9147, 9148, 9149, 9150, 9152, 9153, 9154, 9155, 9156, 9158, 9159, 9160, 9162, 9163, 9164, 9165, 9166, 9168, 9170, 9171, 9172, 9174, 9175, 9176, 9177, 9178, 9180, 9182, 9183, 9184, 9185, 9186, 9188, 9189, 9190, 9191, 9192, 9194, 9195, 9196, 9198, 9200, 9201, 9202, 9204, 9205, 9206, 9207, 9208, 9210, 9212, 9213, 9214, 9215, 9216, 9218, 9219, 9220, 9222, 9224, 9225, 9226, 9228, 9230, 9231, 9232, 9233, 9234, 9235, 9236, 9237, 9238, 9240, 9242, 9243, 9244, 9245, 9246, 9247, 9248, 9249, 9250, 9252, 9254, 9255, 9256, 9258, 9260, 9261, 9262, 9264, 9265, 9266, 9267, 9268, 9270, 9272, 9273, 9274, 9275, 9276, 9278, 9279, 9280, 9282, 9284, 9285, 9286, 9288, 9289, 9290, 9291, 9292, 9294, 9295, 9296, 9297, 9298, 9300, 9302, 9303, 9304, 9305, 9306, 9308, 9309, 9310, 9312, 9314, 9315, 9316, 9317, 9318, 9320, 9321, 9322, 9324, 9325, 9326, 9327, 9328, 9330, 9331, 9332, 9333, 9334, 9335, 9336, 9338, 9339, 9340, 9342, 9344, 9345, 9346, 9348, 9350, 9351, 9352, 9354, 9355, 9356, 9357, 9358, 9359, 9360, 9362, 9363, 9364, 9365, 9366, 9368, 9369, 9370, 9372, 9373, 9374, 9375, 9376, 9378, 9380, 9381, 9382, 9384, 9385, 9386, 9387, 9388, 9390, 9392, 9393, 9394, 9395, 9396, 9398, 9399, 9400, 9401, 9402, 9404, 9405, 9406, 9408, 9410, 9411, 9412, 9414, 9415, 9416, 9417, 9418, 9420, 9422, 9423, 9424, 9425, 9426, 9428, 9429, 9430, 9432, 9434, 9435, 9436, 9438, 9440, 9441, 9442, 9443, 9444, 9445, 9446, 9447, 9448, 9450, 9452, 9453, 9454, 9455, 9456, 9457, 9458, 9459, 9460, 9462, 9464, 9465, 9466, 9468, 9470, 9471, 9472, 9474, 9475, 9476, 9477, 9478, 9480, 9482, 9483, 9484, 9485, 9486, 9488, 9489, 9490, 9492, 9494, 9495, 9496, 9498, 9499, 9500, 9501, 9502, 9504, 9505, 9506, 9507, 9508, 9510, 9512, 9513, 9514, 9515, 9516, 9518, 9519, 9520, 9522, 9524, 9525, 9526, 9527, 9528, 9530, 9531, 9532, 9534, 9535, 9536, 9537, 9538, 9540, 9541, 9542, 9543, 9544, 9545, 9546, 9548, 9549, 9550, 9552, 9554, 9555, 9556, 9558, 9560, 9561, 9562, 9564, 9565, 9566, 9567, 9568, 9569, 9570, 9572, 9573, 9574, 9575, 9576, 9578, 9579, 9580, 9582, 9583, 9584, 9585, 9586, 9588, 9590, 9591, 9592, 9594, 9595, 9596, 9597, 9598, 9600, 9602, 9603, 9604, 9605, 9606, 9608, 9609, 9610, 9611, 9612, 9614, 9615, 9616, 9618, 9620, 9621, 9622, 9624, 9625, 9626, 9627, 9628, 9630, 9632, 9633, 9634, 9635, 9636, 9638, 9639, 9640, 9642, 9644, 9645, 9646, 9648, 9650, 9651, 9652, 9653, 9654, 9655, 9656, 9657, 9658, 9660, 9662, 9663, 9664, 9665, 9666, 9667, 9668, 9669, 9670, 9672, 9674, 9675, 9676, 9678, 9680, 9681, 9682, 9684, 9685, 9686, 9687, 9688, 9690, 9692, 9693, 9694, 9695, 9696, 9698, 9699, 9700, 9702, 9704, 9705, 9706, 9708, 9709, 9710, 9711, 9712, 9714, 9715, 9716, 9717, 9718, 9720, 9722, 9723, 9724, 9725, 9726, 9728, 9729, 9730, 9732, 9734, 9735, 9736, 9737, 9738, 9740, 9741, 9742, 9744, 9745, 9746, 9747, 9748, 9750, 9751, 9752, 9753, 9754, 9755, 9756, 9758, 9759, 9760, 9762, 9764, 9765, 9766, 9768, 9770, 9771, 9772, 9774, 9775, 9776, 9777, 9778, 9779, 9780, 9782, 9783, 9784, 9785, 9786, 9788, 9789, 9790, 9792, 9793, 9794, 9795, 9796, 9798, 9800, 9801, 9802, 9804, 9805, 9806, 9807, 9808, 9810, 9812, 9813, 9814, 9815, 9816, 9818, 9819, 9820, 9821, 9822, 9824, 9825, 9826, 9828, 9830, 9831, 9832, 9834, 9835, 9836, 9837, 9838, 9840, 9842, 9843, 9844, 9845, 9846, 9848, 9849, 9850, 9852, 9854, 9855, 9856, 9858, 9860, 9861, 9862, 9863, 9864, 9865, 9866, 9867, 9868, 9870, 9872, 9873, 9874, 9875, 9876, 9877, 9878, 9879, 9880, 9882, 9884, 9885, 9886, 9888, 9890, 9891, 9892, 9894, 9895, 9896, 9897, 9898, 9900, 9902, 9903, 9904, 9905, 9906, 9908, 9909, 9910, 9912, 9914, 9915, 9916, 9918, 9919, 9920, 9921, 9922, 9924, 9925, 9926, 9927, 9928, 9930, 9932, 9933, 9934, 9935, 9936, 9938, 9939, 9940, 9942, 9944, 9945, 9946, 9947, 9948, 9950, 9951, 9952, 9954, 9955, 9956, 9957, 9958, 9960, 9961, 9962, 9963, 9964, 9965, 9966, 9968, 9969, 9970, 9972, 9974, 9975, 9976, 9978, 9980, 9981, 9982, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9992, 9993, 9994, 9995, 9996, 9998, 9999, 10000}
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 173, 179, 181, 187, 191, 193, 197, 199, 209, 211, 221, 223, 227, 229, 233, 239, 241, 247, 251, 253, 257, 263, 269, 271, 277, 281, 283, 289, 293, 299, 307, 311, 313, 317, 319, 323, 331, 337, 341, 347, 349, 353, 359, 361, 367, 373, 377, 379, 383, 389, 391, 397, 401, 403, 407, 409, 419, 421, 431, 433, 437, 439, 443, 449, 451, 457, 461, 463, 467, 473, 479, 481, 487, 491, 493, 499, 503, 509, 517, 521, 523, 527, 529, 533, 541, 547, 551, 557, 559, 563, 569, 571, 577, 583, 587, 589, 593, 599, 601, 607, 611, 613, 617, 619, 629, 631, 641, 643, 647, 649, 653, 659, 661, 667, 671, 673, 677, 683, 689, 691, 697, 701, 703, 709, 713, 719, 727, 731, 733, 737, 739, 743, 751, 757, 761, 767, 769, 773, 779, 781, 787, 793, 797, 799, 803, 809, 811, 817, 821, 823, 827, 829, 839, 841, 851, 853, 857, 859, 863, 869, 871, 877, 881, 883, 887, 893, 899, 901, 907, 911, 913, 919, 923, 929, 937, 941, 943, 947, 949, 953, 961, 967, 971, 977, 979, 983, 989, 991, 997, 1003, 1007, 1009, 1013, 1019, 1021, 1027, 1031, 1033, 1037, 1039, 1049, 1051, 1061, 1063, 1067, 1069, 1073, 1079, 1081, 1087, 1091, 1093, 1097, 1103, 1109, 1111, 1117, 1121, 1123, 1129, 1133, 1139, 1147, 1151, 1153, 1157, 1159, 1163, 1171, 1177, 1181, 1187, 1189, 1193, 1199, 1201, 1207, 1213, 1217, 1219, 1223, 1229, 1231, 1237, 1241, 1243, 1247, 1249, 1259, 1261, 1271, 1273, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1313, 1319, 1321, 1327, 1331, 1333, 1339, 1343, 1349, 1357, 1361, 1363, 1367, 1369, 1373, 1381, 1387, 1391, 1397, 1399, 1403, 1409, 1411, 1417, 1423, 1427, 1429, 1433, 1439, 1441, 1447, 1451, 1453, 1457, 1459, 1469, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1501, 1507, 1511, 1513, 1517, 1523, 1529, 1531, 1537, 1541, 1543, 1549, 1553, 1559, 1567, 1571, 1573, 1577, 1579, 1583, 1591, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1633, 1637, 1639, 1643, 1649, 1651, 1657, 1661, 1663, 1667, 1669, 1679, 1681, 1691, 1693, 1697, 1699, 1703, 1709, 1711, 1717, 1721, 1723, 1727, 1733, 1739, 1741, 1747, 1751, 1753, 1759, 1763, 1769, 1777, 1781, 1783, 1787, 1789, 1793, 1801, 1807, 1811, 1817, 1819, 1823, 1829, 1831, 1837, 1843, 1847, 1849, 1853, 1859, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1891, 1901, 1903, 1907, 1909, 1913, 1919, 1921, 1927, 1931, 1933, 1937, 1943, 1949, 1951, 1957, 1961, 1963, 1969, 1973, 1979, 1987, 1991, 1993, 1997, 1999, 2003, 2011, 2017, 2021, 2027, 2029, 2033, 2039, 2041, 2047, 2053, 2057, 2059, 2063, 2069, 2071, 2077, 2081, 2083, 2087, 2089, 2099, 2101, 2111, 2113, 2117, 2119, 2123, 2129, 2131, 2137, 2141, 2143, 2147, 2153, 2159, 2161, 2167, 2171, 2173, 2179, 2183, 2189, 2197, 2201, 2203, 2207, 2209, 2213, 2221, 2227, 2231, 2237, 2239, 2243, 2249, 2251, 2257, 2263, 2267, 2269, 2273, 2279, 2281, 2287, 2291, 2293, 2297, 2299, 2309, 2311, 2321, 2323, 2327, 2329, 2333, 2339, 2341, 2347, 2351, 2353, 2357, 2363, 2369, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2407, 2411, 2413, 2417, 2419, 2423, 2431, 2437, 2441, 2447, 2449, 2453, 2459, 2461, 2467, 2473, 2477, 2479, 2483, 2489, 2491, 2497, 2501, 2503, 2507, 2509, 2519, 2521, 2531, 2533, 2537, 2539, 2543, 2549, 2551, 2557, 2561, 2563, 2567, 2573, 2579, 2581, 2587, 2591, 2593, 2599, 2603, 2609, 2617, 2621, 2623, 2627, 2629, 2633, 2641, 2647, 2651, 2657, 2659, 2663, 2669, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2701, 2707, 2711, 2713, 2717, 2719, 2729, 2731, 2741, 2743, 2747, 2749, 2753, 2759, 2761, 2767, 2771, 2773, 2777, 2783, 2789, 2791, 2797, 2801, 2803, 2809, 2813, 2819, 2827, 2831, 2833, 2837, 2839, 2843, 2851, 2857, 2861, 2867, 2869, 2873, 2879, 2881, 2887, 2893, 2897, 2899, 2903, 2909, 2911, 2917, 2921, 2923, 2927, 2929, 2939, 2941, 2951, 2953, 2957, 2959, 2963, 2969, 2971, 2977, 2981, 2983, 2987, 2993, 2999, 3001, 3007, 3011, 3013, 3019, 3023, 3029, 3037, 3041, 3043, 3047, 3049, 3053, 3061, 3067, 3071, 3077, 3079, 3083, 3089, 3091, 3097, 3103, 3107, 3109, 3113, 3119, 3121, 3127, 3131, 3133, 3137, 3139, 3149, 3151, 3161, 3163, 3167, 3169, 3173, 3179, 3181, 3187, 3191, 3193, 3197, 3203, 3209, 3211, 3217, 3221, 3223, 3229, 3233, 3239, 3247, 3251, 3253, 3257, 3259, 3263, 3271, 3277, 3281, 3287, 3289, 3293, 3299, 3301, 3307, 3313, 3317, 3319, 3323, 3329, 3331, 3337, 3341, 3343, 3347, 3349, 3359, 3361, 3371, 3373, 3377, 3379, 3383, 3389, 3391, 3397, 3401, 3403, 3407, 3413, 3419, 3421, 3427, 3431, 3433, 3439, 3443, 3449, 3457, 3461, 3463, 3467, 3469, 3473, 3481, 3487, 3491, 3497, 3499, 3503, 3509, 3511, 3517, 3523, 3527, 3529, 3533, 3539, 3541, 3547, 3551, 3553, 3557, 3559, 3569, 3571, 3581, 3583, 3587, 3589, 3593, 3599, 3601, 3607, 3611, 3613, 3617, 3623, 3629, 3631, 3637, 3641, 3643, 3649, 3653, 3659, 3667, 3671, 3673, 3677, 3679, 3683, 3691, 3697, 3701, 3707, 3709, 3713, 3719, 3721, 3727, 3733, 3737, 3739, 3743, 3749, 3751, 3757, 3761, 3763, 3767, 3769, 3779, 3781, 3791, 3793, 3797, 3799, 3803, 3809, 3811, 3817, 3821, 3823, 3827, 3833, 3839, 3841, 3847, 3851, 3853, 3859, 3863, 3869, 3877, 3881, 3883, 3887, 3889, 3893, 3901, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3937, 3943, 3947, 3949, 3953, 3959, 3961, 3967, 3971, 3973, 3977, 3979, 3989, 3991, 4001, 4003, 4007, 4009, 4013, 4019, 4021, 4027, 4031, 4033, 4037, 4043, 4049, 4051, 4057, 4061, 4063, 4069, 4073, 4079, 4087, 4091, 4093, 4097, 4099, 4103, 4111, 4117, 4121, 4127, 4129, 4133, 4139, 4141, 4147, 4153, 4157, 4159, 4163, 4169, 4171, 4177, 4181, 4183, 4187, 4189, 4199, 4201, 4211, 4213, 4217, 4219, 4223, 4229, 4231, 4237, 4241, 4243, 4247, 4253, 4259, 4261, 4267, 4271, 4273, 4279, 4283, 4289, 4297, 4301, 4303, 4307, 4309, 4313, 4321, 4327, 4331, 4337, 4339, 4343, 4349, 4351, 4357, 4363, 4367, 4369, 4373, 4379, 4381, 4387, 4391, 4393, 4397, 4399, 4409, 4411, 4421, 4423, 4427, 4429, 4433, 4439, 4441, 4447, 4451, 4453, 4457, 4463, 4469, 4471, 4477, 4481, 4483, 4489, 4493, 4499, 4507, 4511, 4513, 4517, 4519, 4523, 4531, 4537, 4541, 4547, 4549, 4553, 4559, 4561, 4567, 4573, 4577, 4579, 4583, 4589, 4591, 4597, 4601, 4603, 4607, 4609, 4619, 4621, 4631, 4633, 4637, 4639, 4643, 4649, 4651, 4657, 4661, 4663, 4667, 4673, 4679, 4681, 4687, 4691, 4693, 4699, 4703, 4709, 4717, 4721, 4723, 4727, 4729, 4733, 4741, 4747, 4751, 4757, 4759, 4763, 4769, 4771, 4777, 4783, 4787, 4789, 4793, 4799, 4801, 4807, 4811, 4813, 4817, 4819, 4829, 4831, 4841, 4843, 4847, 4849, 4853, 4859, 4861, 4867, 4871, 4873, 4877, 4883, 4889, 4891, 4897, 4901, 4903, 4909, 4913, 4919, 4927, 4931, 4933, 4937, 4939, 4943, 4951, 4957, 4961, 4967, 4969, 4973, 4979, 4981, 4987, 4993, 4997, 4999, 5003, 5009, 5011, 5017, 5021, 5023, 5027, 5029, 5039, 5041, 5051, 5053, 5057, 5059, 5063, 5069, 5071, 5077, 5081, 5083, 5087, 5093, 5099, 5101, 5107, 5111, 5113, 5119, 5123, 5129, 5137, 5141, 5143, 5147, 5149, 5153, 5161, 5167, 5171, 5177, 5179, 5183, 5189, 5191, 5197, 5203, 5207, 5209, 5213, 5219, 5221, 5227, 5231, 5233, 5237, 5239, 5249, 5251, 5261, 5263, 5267, 5269, 5273, 5279, 5281, 5287, 5291, 5293, 5297, 5303, 5309, 5311, 5317, 5321, 5323, 5329, 5333, 5339, 5347, 5351, 5353, 5357, 5359, 5363, 5371, 5377, 5381, 5387, 5389, 5393, 5399, 5401, 5407, 5413, 5417, 5419, 5423, 5429, 5431, 5437, 5441, 5443, 5447, 5449, 5459, 5461, 5471, 5473, 5477, 5479, 5483, 5489, 5491, 5497, 5501, 5503, 5507, 5513, 5519, 5521, 5527, 5531, 5533, 5539, 5543, 5549, 5557, 5561, 5563, 5567, 5569, 5573, 5581, 5587, 5591, 5597, 5599, 5603, 5609, 5611, 5617, 5623, 5627, 5629, 5633, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669, 5671, 5681, 5683, 5687, 5689, 5693, 5699, 5701, 5707, 5711, 5713, 5717, 5723, 5729, 5731, 5737, 5741, 5743, 5749, 5753, 5759, 5767, 5771, 5773, 5777, 5779, 5783, 5791, 5797, 5801, 5807, 5809, 5813, 5819, 5821, 5827, 5833, 5837, 5839, 5843, 5849, 5851, 5857, 5861, 5863, 5867, 5869, 5879, 5881, 5891, 5893, 5897, 5899, 5903, 5909, 5911, 5917, 5921, 5923, 5927, 5933, 5939, 5941, 5947, 5951, 5953, 5959, 5963, 5969, 5977, 5981, 5983, 5987, 5989, 5993, 6001, 6007, 6011, 6017, 6019, 6023, 6029, 6031, 6037, 6043, 6047, 6049, 6053, 6059, 6061, 6067, 6071, 6073, 6077, 6079, 6089, 6091, 6101, 6103, 6107, 6109, 6113, 6119, 6121, 6127, 6131, 6133, 6137, 6143, 6149, 6151, 6157, 6161, 6163, 6169, 6173, 6179, 6187, 6191, 6193, 6197, 6199, 6203, 6211, 6217, 6221, 6227, 6229, 6233, 6239, 6241, 6247, 6253, 6257, 6259, 6263, 6269, 6271, 6277, 6281, 6283, 6287, 6289, 6299, 6301, 6311, 6313, 6317, 6319, 6323, 6329, 6331, 6337, 6341, 6343, 6347, 6353, 6359, 6361, 6367, 6371, 6373, 6379, 6383, 6389, 6397, 6401, 6403, 6407, 6409, 6413, 6421, 6427, 6431, 6437, 6439, 6443, 6449, 6451, 6457, 6463, 6467, 6469, 6473, 6479, 6481, 6487, 6491, 6493, 6497, 6499, 6509, 6511, 6521, 6523, 6527, 6529, 6533, 6539, 6541, 6547, 6551, 6553, 6557, 6563, 6569, 6571, 6577, 6581, 6583, 6589, 6593, 6599, 6607, 6611, 6613, 6617, 6619, 6623, 6631, 6637, 6641, 6647, 6649, 6653, 6659, 6661, 6667, 6673, 6677, 6679, 6683, 6689, 6691, 6697, 6701, 6703, 6707, 6709, 6719, 6721, 6731, 6733, 6737, 6739, 6743, 6749, 6751, 6757, 6761, 6763, 6767, 6773, 6779, 6781, 6787, 6791, 6793, 6799, 6803, 6809, 6817, 6821, 6823, 6827, 6829, 6833, 6841, 6847, 6851, 6857, 6859, 6863, 6869, 6871, 6877, 6883, 6887, 6889, 6893, 6899, 6901, 6907, 6911, 6913, 6917, 6919, 6929, 6931, 6941, 6943, 6947, 6949, 6953, 6959, 6961, 6967, 6971, 6973, 6977, 6983, 6989, 6991, 6997, 7001, 7003, 7009, 7013, 7019, 7027, 7031, 7033, 7037, 7039, 7043, 7051, 7057, 7061, 7067, 7069, 7073, 7079, 7081, 7087, 7093, 7097, 7099, 7103, 7109, 7111, 7117, 7121, 7123, 7127, 7129, 7139, 7141, 7151, 7153, 7157, 7159, 7163, 7169, 7171, 7177, 7181, 7183, 7187, 7193, 7199, 7201, 7207, 7211, 7213, 7219, 7223, 7229, 7237, 7241, 7243, 7247, 7249, 7253, 7261, 7267, 7271, 7277, 7279, 7283, 7289, 7291, 7297, 7303, 7307, 7309, 7313, 7319, 7321, 7327, 7331, 7333, 7337, 7339, 7349, 7351, 7361, 7363, 7367, 7369, 7373, 7379, 7381, 7387, 7391, 7393, 7397, 7403, 7409, 7411, 7417, 7421, 7423, 7429, 7433, 7439, 7447, 7451, 7453, 7457, 7459, 7463, 7471, 7477, 7481, 7487, 7489, 7493, 7499, 7501, 7507, 7513, 7517, 7519, 7523, 7529, 7531, 7537, 7541, 7543, 7547, 7549, 7559, 7561, 7571, 7573, 7577, 7579, 7583, 7589, 7591, 7597, 7601, 7603, 7607, 7613, 7619, 7621, 7627, 7631, 7633, 7639, 7643, 7649, 7657, 7661, 7663, 7667, 7669, 7673, 7681, 7687, 7691, 7697, 7699, 7703, 7709, 7711, 7717, 7723, 7727, 7729, 7733, 7739, 7741, 7747, 7751, 7753, 7757, 7759, 7769, 7771, 7781, 7783, 7787, 7789, 7793, 7799, 7801, 7807, 7811, 7813, 7817, 7823, 7829, 7831, 7837, 7841, 7843, 7849, 7853, 7859, 7867, 7871, 7873, 7877, 7879, 7883, 7891, 7897, 7901, 7907, 7909, 7913, 7919, 7921, 7927, 7933, 7937, 7939, 7943, 7949, 7951, 7957, 7961, 7963, 7967, 7969, 7979, 7981, 7991, 7993, 7997, 7999, 8003, 8009, 8011, 8017, 8021, 8023, 8027, 8033, 8039, 8041, 8047, 8051, 8053, 8059, 8063, 8069, 8077, 8081, 8083, 8087, 8089, 8093, 8101, 8107, 8111, 8117, 8119, 8123, 8129, 8131, 8137, 8143, 8147, 8149, 8153, 8159, 8161, 8167, 8171, 8173, 8177, 8179, 8189, 8191, 8201, 8203, 8207, 8209, 8213, 8219, 8221, 8227, 8231, 8233, 8237, 8243, 8249, 8251, 8257, 8261, 8263, 8269, 8273, 8279, 8287, 8291, 8293, 8297, 8299, 8303, 8311, 8317, 8321, 8327, 8329, 8333, 8339, 8341, 8347, 8353, 8357, 8359, 8363, 8369, 8371, 8377, 8381, 8383, 8387, 8389, 8399, 8401, 8411, 8413, 8417, 8419, 8423, 8429, 8431, 8437, 8441, 8443, 8447, 8453, 8459, 8461, 8467, 8471, 8473, 8479, 8483, 8489, 8497, 8501, 8503, 8507, 8509, 8513, 8521, 8527, 8531, 8537, 8539, 8543, 8549, 8551, 8557, 8563, 8567, 8569, 8573, 8579, 8581, 8587, 8591, 8593, 8597, 8599, 8609, 8611, 8621, 8623, 8627, 8629, 8633, 8639, 8641, 8647, 8651, 8653, 8657, 8663, 8669, 8671, 8677, 8681, 8683, 8689, 8693, 8699, 8707, 8711, 8713, 8717, 8719, 8723, 8731, 8737, 8741, 8747, 8749, 8753, 8759, 8761, 8767, 8773, 8777, 8779, 8783, 8789, 8791, 8797, 8801, 8803, 8807, 8809, 8819, 8821, 8831, 8833, 8837, 8839, 8843, 8849, 8851, 8857, 8861, 8863, 8867, 8873, 8879, 8881, 8887, 8891, 8893, 8899, 8903, 8909, 8917, 8921, 8923, 8927, 8929, 8933, 8941, 8947, 8951, 8957, 8959, 8963, 8969, 8971, 8977, 8983, 8987, 8989, 8993, 8999, 9001, 9007, 9011, 9013, 9017, 9019, 9029, 9031, 9041, 9043, 9047, 9049, 9053, 9059, 9061, 9067, 9071, 9073, 9077, 9083, 9089, 9091, 9097, 9101, 9103, 9109, 9113, 9119, 9127, 9131, 9133, 9137, 9139, 9143, 9151, 9157, 9161, 9167, 9169, 9173, 9179, 9181, 9187, 9193, 9197, 9199, 9203, 9209, 9211, 9217, 9221, 9223, 9227, 9229, 9239, 9241, 9251, 9253, 9257, 9259, 9263, 9269, 9271, 9277, 9281, 9283, 9287, 9293, 9299, 9301, 9307, 9311, 9313, 9319, 9323, 9329, 9337, 9341, 9343, 9347, 9349, 9353, 9361, 9367, 9371, 9377, 9379, 9383, 9389, 9391, 9397, 9403, 9407, 9409, 9413, 9419, 9421, 9427, 9431, 9433, 9437, 9439, 9449, 9451, 9461, 9463, 9467, 9469, 9473, 9479, 9481, 9487, 9491, 9493, 9497, 9503, 9509, 9511, 9517, 9521, 9523, 9529, 9533, 9539, 9547, 9551, 9553, 9557, 9559, 9563, 9571, 9577, 9581, 9587, 9589, 9593, 9599, 9601, 9607, 9613, 9617, 9619, 9623, 9629, 9631, 9637, 9641, 9643, 9647, 9649, 9659, 9661, 9671, 9673, 9677, 9679, 9683, 9689, 9691, 9697, 9701, 9703, 9707, 9713, 9719, 9721, 9727, 9731, 9733, 9739, 9743, 9749, 9757, 9761, 9763, 9767, 9769, 9773, 9781, 9787, 9791, 9797, 9799, 9803, 9809, 9811, 9817, 9823, 9827, 9829, 9833, 9839, 9841, 9847, 9851, 9853, 9857, 9859, 9869, 9871, 9881, 9883, 9887, 9889, 9893, 9899, 9901, 9907, 9911, 9913, 9917, 9923, 9929, 9931, 9937, 9941, 9943, 9949, 9953, 9959, 9967, 9971, 9973, 9977, 9979, 9983, 9991, 9997]
"""

import sympy

print(sympy.isprime(5))
# True
print(list(sympy.primerange(0, 100)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(sympy.randprime(0, 100))
# 83
print(sympy.randprime(0, 100))
# 41
print(sympy.prime(3))
# 5
print(sympy.prevprime(50))
# 47
print(sympy.nextprime(50))
# 53
print(list(sympy.sieve.primerange(0, 100)))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(nonprimes := [j for i in range(2, 8) for j in range(i * 2, 100, i)])
print(primeslist := [x for x in range(2, 100) if x not in nonprimes])

"""
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

from primesieve import *

# Generate a list of the primes below 40
generate_primes(40)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# Generate a list of the primes between 100 and 120
generate_primes(100, 120)
# [101, 103, 107, 109, 113]

# Generate a list of the first 10 primes
generate_n_primes(10)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Generate a list of the first 10 starting at 1000
generate_n_primes(10, 1000)
# [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061]

# Get the 10th prime
nth_prime(10)
# 29

# Count the primes below 10**9
count_primes(10**9)
# 50847534
"""

"""
https://www.cuemath.com/numbers/prime-numbers-from-1-to-1000/
https://www.geeksforgeeks.org/primepy-module-in-python/

Installing Library
This module does not come built-in with Python. You need to install it externally. To install this module type the below command in the terminal. 

 pip install primePy  
Functions of primePy
1. primes.check(n): It will return True if ‘n’ is a prime number otherwise it will return False.
"""
# Importing primes function
# From primePy Library
from primePy import primes
 
 
print(primes.check(105))
print(primes.check(71))

"""
Output: 

False
True

2. primes.factor(n): It will return the lowest prime factor of ‘n’.

Example:
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.factor(15)
print(a)
 
a = primes.factor(75689456252)
print(a)

"""
Output: 

3
2

3. primes.factors(n): It will return all the prime factors of ‘n’ with repetition of factors if exist.

Example: 
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.factors(774177)
print(a)
 
a = primes.factors(15)
print(a)

"""
Output: 

[3, 151, 1709]
[3, 5]

4. primes.first(n) : It will return first ‘n’ prime numbers.

Example: 
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.first(5)
print(a)
 
a = primes.first(10)
print(a)

"""
Output: 

[2, 3, 5, 7, 11]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
5. primes.upto(n): It will return all the prime numbers less than or equal to ‘n’.

Example: 
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.upto(17)
print(a)
 
a = primes.upto(100)
print(a)

"""
Output:

[2, 3, 5, 7, 11, 13, 17] 
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] 
 

6. primes.between(m, n): It will return all the prime numbers between m and n.

Example: 
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.between(4, 15)
print(a)
 
a = primes.between(25, 75)
print(a)

"""
Output: 

[5, 7, 11, 13]
[29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]

7. primes.phi(n): It will return the number of integers less than ‘n’ which have no common factor with n.

Example: 
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.phi(5)
print(a)
 
a = primes.phi(10)
print(a)

"""
Output: 

4
4
"""

# Importing primes function
# From primePy Library
from primePy import primes
 
 
a = primes.first(5)
print(a)
 
a = primes.first(10)
print(a)

# print(primes.first(10001))
"""
...
02499, 102503, 102523, 102533, 102539, 102547, 102551, 102559, 102563, 102587, 102593, 102607, 102611, 102643, 102647, 102653, 102667, 102673, 102677, 102679, 102701, 102761, 102763, 102769, 102793, 102797, 102811, 102829, 102841, 102859, 102871, 102877, 102881, 102911, 102913, 102929, 102931, 102953, 102967, 102983, 103001, 103007, 103043, 103049, 103067, 103069, 103079, 103087, 103091, 103093, 103099, 103123, 103141, 103171, 103177, 103183, 103217, 103231, 103237, 103289, 103291, 103307, 103319, 103333, 103349, 103357, 103387, 103391, 103393, 103399, 103409, 103421, 103423, 103451, 103457, 103471, 103483, 103511, 103529, 103549, 103553, 103561, 103567, 103573, 103577, 103583, 103591, 103613, 103619, 103643, 103651, 103657, 103669, 103681, 103687, 103699, 103703, 103723, 103769, 103787, 103801, 103811, 103813, 103837, 103841, 103843, 103867, 103889, 103903, 103913, 103919, 103951, 103963, 103967, 103969, 103979, 103981, 103991, 103993, 103997, 104003, 104009, 104021, 104033, 104047, 104053, 104059, 104087, 104089, 104107, 104113, 104119, 104123, 104147, 104149, 104161, 104173, 104179, 104183, 104207, 104231, 104233, 104239, 104243, 104281, 104287, 104297, 104309, 104311, 104323, 104327, 104347, 104369, 104381, 104383, 104393, 104399, 104417, 104459, 104471, 104473, 104479, 104491, 104513, 104527, 104537, 104543, 104549, 104551, 104561, 104579, 104593, 104597, 104623, 104639, 104651, 104659, 104677, 104681, 104683, 104693, 104701, 104707, 104711, 104717, 104723, 104729, 104743]
"""

"""
https://www.geeksforgeeks.org/gcd-in-python/

The Highest Common Factor (HCF), also called gcd, can be computed in python using a single function offered by math module and hence can make tasks easier in many situations.

Naive Methods to compute gcd

Way 1: Using Recursion
"""

# Python code to demonstrate naive
# method to compute gcd ( recursion )
 
def hcfnaive(a, b):
    if(b == 0):
        return abs(a)
    else:
        return hcfnaive(b, a % b)
 
a = 60
b = 48
 
# prints 12
print("The gcd of 60 and 48 is : ", end="")
print(hcfnaive(60, 48))

"""
Output
The gcd of 60 and 48 is : 12

Way 2: Using Loops 
"""

# Python code to demonstrate naive
# method to compute gcd ( Loops )
 
def computeGCD(x, y):
 
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
             
    return gcd
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ", end="")
print (computeGCD(60,48))

"""
Output
The gcd of 60 and 48 is : 12

Way 3: Using Euclidean Algorithm 
"""

# Python code to demonstrate naive
# method to compute gcd ( Euclidean algo )
 
 
def computeGCD(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)
 
a = 60
b = 48
 
# prints 12
print ("The gcd of 60 and 48 is : ",end="")
print (computeGCD(60, 48))

"""
Output:

The gcd of 60 and 48 is : 12

Both numbers are 0, gcd is 0
If only either number is Not a number, Type Error is raised.
"""
up_ceiling = 10001
non_primes = [j for i in range(2,8) for j in range(i*2, up_ceiling, i)]
primes = [x for x in range(2, up_ceiling) if x not in non_primes]
print(primes)
