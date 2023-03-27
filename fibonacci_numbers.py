# Challenge: A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers. 
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.
# Print every number in the Fibonacci Sequence without going over 200.

def fibonacci_upto(limit):
    a = [0]
    previous, current = 0, 1
 
    while current < limit:
        a.append(current)  
        next = current + previous
        previous = current
        current = next
        
    return a   

s= fibonacci_upto(200)
print(s)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

s= [fibonacci_of(n) for n in range(20)]
print(s)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# https://www.geeksforgeeks.org/python-functools-lru_cache/
from functools import lru_cache
import time
  
# Function that computes Fibonacci 
# numbers without lru_cache
def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)
      
# Execution start time
begin = time.time()
print(fib_without_cache(30))
# s = [fibonacci_of(n) for n in range(30)]
# print(s)  
# Execution end time
end = time.time()
  
print("Time taken to execute the\
function without lru_cache is", end-begin)
  
# Function that computes Fibonacci
# numbers with lru_cache
@lru_cache(maxsize = 128)
def fib_with_cache(n):
    if n < 2:
        return n
    print(fib_with_cache.cache_info())
    return fib_with_cache(n-1) + fib_with_cache(n-2)
      
begin = time.time()
print(fib_with_cache(30))
# s = [fibonacci_of(n) for n in range(30)]
# print(s)
end = time.time()
  
print("Time taken to execute the \
function with lru_cache is", end-begin)

"""
Output:

Time taken to execute the function without lru_cache is 0.4448213577270508
Time taken to execute the function with lru_cache is 2.8371810913085938e-05

Example 2:
"""

from functools import lru_cache
  
@lru_cache(maxsize = 100)
def count_vowels(sentence):
    print(sentence)
    print(sentence := sentence.casefold())    # https://www.geeksforgeeks.org/python-string-casefold-method/
    print(sentence)
    return sum(sentence.count(vowel) for vowel in 'aeiou')
      
print(count_vowels("Welcome to Geeksforgeeks"))

"""
Output:

9
"""

# Function that computes Fibonacci
# nu3mbers with lru_cache
@lru_cache(maxsize = 128)
def fib_with_cache(n):
    fibonacci_array = [0]
    pre, current = 0, 1
    while len(fibonacci_array) < n:
        fibonacci_array.append(current)
        next = pre + current
        pre = current
        current = next
    print(fib_with_cache.cache_info())
    return fibonacci_array

begin = time.time()
print(fib_with_cache(30))
end = time.time()
  
print("Time taken to execute the \
function with lru_cache is", end-begin)

"""
CacheInfo(hits=0, misses=1, maxsize=128, currsize=0)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229]
Time taken to execute the function with lru_cache is 0.0
"""