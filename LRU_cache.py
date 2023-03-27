# https://www.geeksforgeeks.org/python-lru-cache/

"""
LRU Cache is the least recently used cache which is basically used for Memory Organization. 
In this, the elements come as First in First Out format. 
The LRU caching scheme is to remove the least recently used frame when the cache is full and a new page is referenced which is not there in the cache. There are generally two terms use with LRU Cache, let’s see them –

Page hit: If the required page is found in the main memory then it is a page hit.
Page Fault: If the required page is not found in the main memory then page fault occurs.
When a page is referenced, the required page may be in the memory. If it is in the memory, we need to detach the node of the list and bring it to the front of the queue.
If the required page is not in memory, we bring that in memory. In simple words, we add a new node to the front of the queue and update the corresponding node address in the hash. If the queue is full, i.e. all the frames are full, we remove a node from the rear of the queue, and add the new node to the front of the queue.

Example – Consider the following reference string :

1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Find the number of page faults using least recently used (LRU) page replacement algorithm with 3 page frames.
Explanation –

LRU Cache Using Python
You can implement this with the help of the queue. In this, we have used Queue using the linked list. Run the given code in Pycharm IDE.
"""

import time
   
      
class Node:
      
    # Nodes are represented in n
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
   
   
class LRUCache:
    cache_limit = None
      
    # if the DEBUG is TRUE then it
    # will execute
    DEBUG = False
   
    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
   
    def __call__(self, *args, **kwargs):
          
        # The cache presents with the help
        # of Linked List
        if args in self.cache:
            self.llist(args)
              
            if self.DEBUG == True:
                return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
            return self.cache[args]
   
        # The given cache keeps on moving.
        if self.cache_limit is not None:
              
            if len(self.cache) > self.cache_limit:
                n = self.head.next
                self._remove(n)
                del self.cache[n.key]
   
        # Compute and cache and node to see whether 
        # the following element is present or not 
        # based on the given input.
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
          
        if self.DEBUG == True:
            return f'{result}\nCache: {self.cache}'
        return result
   
    # Remove from double linked-list - Node.
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
   
    # Add to double linked-list - Node.
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
   
    # Over here the result task is being done 
    def llist(self, args):
        current = self.head
          
        while True:
              
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                  
                if self.DEBUG == True:
                    del self.cache[node.key]  
                    self.cache[node.key] = node.val 
                break
              
            else:
                current = current.next
   
   
# Default Debugging is FALSE. For 
# execution of DEBUG is set to TRUE
LRUCache.DEBUG = True
   
# The DEFAULT test limit is NONE.
LRUCache.cache_limit = 3
   
  
@LRUCache
def ex_func_01(n):
    print(f'Computing...{n}')
    time.sleep(1)
    return n
   
"""   
print(f'\nFunction: ex_func_01')
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(5))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(5))


Output:

Function: ex_func_01
Computing...1
1
Cache: {(1,): 1}
Computing...2
2
Cache: {(1,): 1, (2,): 2}
Computing...3
3
Cache: {(1,): 1, (2,): 2, (3,): 3}
Computing...4
4
Cache: {(1,): 1, (2,): 2, (3,): 3, (4,): 4}
Cached...(1,)
1
Cache: {(2,): 2, (3,): 3, (4,): 4, (1,): 1}
Cached...(2,)
2
Cache: {(3,): 3, (4,): 4, (1,): 1, (2,): 2}
Computing...5
5
Cache: {(4,): 4, (1,): 1, (2,): 2, (5,): 5}
Cached...(1,)
1
Cache: {(4,): 4, (2,): 2, (5,): 5, (1,): 1}
Cached...(2,)
2
Cache: {(4,): 4, (5,): 5, (1,): 1, (2,): 2}
Computing...3
3
Cache: {(5,): 5, (1,): 1, (2,): 2, (3,): 3}
Computing...4
4
Cache: {(1,): 1, (2,): 2, (3,): 3, (4,): 4}
Computing...5
5
Cache: {(2,): 2, (3,): 3, (4,): 4, (5,): 5}
"""

# built-in cache:
import functools

@functools.lru_cache()
def sum(n):
    if n == 0:
        return
    n -= 1
    sum(n) 
    print(sum.cache_info)   # <built-in method cache_info of functools._lru_cache_wrapper object at 0x0000025BC4058EB0>
    print(sum.cache_info()) # CacheInfo(hits=0, misses=1, maxsize=128, currsize=0)

# sum(5)
# sum(9)

# LRU Cache in Python using OrderedDict
"""
LRU (Least Recently Used) Cache discards the least recently used items first. This algorithm requires keeping track of what was used when, which is expensive if one wants to make sure the algorithm always discards the least recently used item. General implementations of this technique require keeping “age bits” for cache-lines and track the “Least Recently Used” cache-line based on age-bits.
Our problem statement is to design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.
* get(key) – Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1. 
* put(key, value) – Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is always initialized with positive capacity.

Examples: 

Input/Output : 
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);                                    
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4



Our solution is to use the power of OrderedDict from collections module which keep order of insertion of keys and we can change that order if required. The best part is all operations have O(1) time complexity.
We maintain our OrderedDict in such a way that the order shows how recently they were used. In the beginning, we will have least recently used and in the end, most recently used. 
If any update OR query is made to a key it moves to the end (most recently used). If anything is added, it is added at the end (most recently used/added)
For get(key): we return the value of the key that is queried in O(1) and return -1 if we don’t find the key in out dict/cache. And also move the key to the end to show that it was recently used.
For put(key, value): first, we add/ update the key by conventional methods. And also move the key to the end to show that it was recently used. But here we will also check whether the length of our ordered dictionary has exceeded our capacity, If so we remove the first key (least recently used)
""" 

from collections import OrderedDict
 
class LRUCache:
 
    # initialising capacity
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    # we return the value of the key
    # that is queried in O(1) and return -1 if we
    # don't find the key in out dict / cache.
    # And also move the key to the end
    # to show that it was recently used.
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    # first, we add / update the key by conventional methods.
    # And also move the key to the end to show that it was recently used.
    # But here we will also check whether the length of our
    # ordered dictionary has exceeded our capacity,
    # If so we remove the first key (least recently used)
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
 
# RUNNER
# initializing our cache with the capacity of 2
cache = LRUCache(2)
 
cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)
 
#This code was contributed by Sachin Negi
"""
Output: 
OrderedDict([(1, 1)])
OrderedDict([(1, 1), (2, 2)])
OrderedDict([(2, 2), (1, 1)])
OrderedDict([(1, 1), (3, 3)])
OrderedDict([(1, 1), (3, 3)])
OrderedDict([(3, 3), (4, 4)])
OrderedDict([(3, 3), (4, 4)])
OrderedDict([(4, 4), (3, 3)])
OrderedDict([(3, 3), (4, 4)])

Time Complexity :O(1)
"""

# LRU Cache implementation using Double Linked Lists
"""
Given a pre define size of a list N and an array Arr. The task is to implement Least Recently Used(LRU) algorithm using Double Linked Lists. 
The program takes two sets of inputs. First, The size of the linked list. Second, The element to search in the linked list.
Examples:

Input: N = 3, Arr = { 1, 2, 3 } 
Output: 
[0]->[0]->[0]->NULL 
[1]->[0]->[0]->NULL 
[2]->[1]->[0]->NULL 
[3]->[2]->[1]->NULL 

Input: N = 5, Arr = { 1, 2, 3, 4, 3, 8 } 
Output: 
[0]->[0]->[0]->[0]->[0]->NULL 
[1]->[0]->[0]->[0]->[0]->NULL 
[2]->[1]->[0]->[0]->[0]->NULL 
[3]->[2]->[1]->[0]->[0]->NULL 
[4]->[3]->[2]->[1]->[0]->NULL 
[2]->[4]->[3]->[1]->[0]->NULL 
[8]->[2]->[4]->[3]->[1]->NULL 
"""

class doublelinkedlist:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
 
head = None
tail = None
temp = None
 
status = None
 
def AddNode(value):
    global head, tail, temp
    if head is None:
        head = doublelinkedlist(value)
        tail = head
        head.prev = None
    else:
        temp = tail
        tail.next = doublelinkedlist(value)
        tail = tail.next
        tail.prev = temp
    tail.next = None
    return 0
 
def Display():
    global head, temp
    if head is None:
        print("Add a node first")
        return -2
    else:
        temp = head
        while temp is not None:
            print(f"[{temp.val}]->", end="")
            temp = temp.next
        print("NULL")
    return 0
 
def SearchCache(value):
    global head, temp
    if head is None:
        print("Add a node first")
        return -1
    temp = head
    while temp is not None:
        if temp.val == value:
            while temp != head:
                temp.val = temp.prev.val
                temp = temp.prev
            head.val = value
            return 0
        temp = temp.next
    temp = tail.prev
    while temp is not None:
        temp.next.val = temp.val
        temp = temp.prev
    head.val = value
    return 0
 
def NumberOfNodes(number):
    global status
    for i in range(number):
        status = AddNode(0)
        if status < 0:
            print("Could not assign node")
            return status
    return 0
 
def FreeCache(number):
    global head, tail, temp
    temp = head
    while temp is not None:
        head = head.next
        del temp
        temp = head
    tail = None
    return 0
def LRUOp(arr, n):
    global status
    for i in range(n):
        status = SearchCache(arr[i])
        if status < 0:
            exit(1)
        status = Display()
 
if __name__ == '__main__':
    MEMSIZE = 5
    status = NumberOfNodes(MEMSIZE)
    n = 10
    arr = [1, 2, 3, 4, 5, 2, 10, 7, 11, 1]
    LRUOp(arr, n)
    FreeCache(MEMSIZE)

"""
Output: 
[1]->[0]->[0]->[0]->[0]->NULL
[2]->[1]->[0]->[0]->[0]->NULL
[3]->[2]->[1]->[0]->[0]->NULL
[4]->[3]->[2]->[1]->[0]->NULL
[5]->[4]->[3]->[2]->[1]->NULL
[2]->[5]->[4]->[3]->[1]->NULL
[10]->[2]->[5]->[4]->[3]->NULL
[7]->[10]->[2]->[5]->[4]->NULL
[11]->[7]->[10]->[2]->[5]->NULL
[1]->[11]->[7]->[10]->[2]->NULL
"""

# Implementing LRU Cache Decorator in Python
"""
LRU cache consists of Queue and Dictionary data structures. 
Queue: to store the most recently used to least recently used files 
Hash table: to store the file and its position in the cache 
What is decorator?
A decorator is a function that takes a function as its only parameter and returns a function. 
This is helpful to “wrap” functionality with the same code over and over again. 
Note: For more information, refer to Decorators in Python.
Now, after getting the basic idea about the LRU and Decorators in Python, 
let’s have a look at the implementation of the LRU cache Decorator in Python.
""" 

from collections import deque
 
 
# LRU cache implementation
class LRUCache:
     
    def __init__(self, size=5):
        self.size = size
        self.container = deque()
        self.map = dict()
      
      
    def reallocate(self):
        # to reallocate the hashmap for
        # every access of file access file
        # will reallocate the data in hashmap
        # according to the numbers position
        # in the container for every access,
        # hit and miss(evict)
        if len(self.container) > 1:
             
            for key, val in enumerate(self.container):
                self.map[val] = key
      
      
    def access(self, val):
         
        # print("access "+str(val))
        self.container.remove(val)
        self.container.appendleft(val)
        self.reallocate()
      
    def evict(self, val):
         
        # print("cache miss "+str(val))
        if val in self.map:
            #del self.map[val]
            self.container.remove(val)
         
        else:
            x = self.container.pop()
            del self.map[x]
         
        self.normal_insert(val)
          
    def normal_insert(self, val):
        self.container.appendleft(val)
        self.reallocate()
          
    def insert(self, val):
         
        if val in self.map.keys():
             
            # if value in present in
            # the hashmap then it is a hit.
            # access function will access the
            # number already present and replace
            # it to leftmost position
            self.access(val)
             
        else:
            # if value is not present in
            # the hashtable
            if (len(self.map.keys()) == self.size):
                # if the size of the queue
                # is equal to capacity and
                # we try to insert the number,
                # then it is a miss then,
                # evict function will delete the
                # right most elements and insert
                # the latest element in the
                # leftmost position
                self.evict(val)
                 
            else:
                # normal_insert function will normally
                # insert the data into the cache..
                self.normal_insert(val)
      
    def print(self):
        lru_elements = [x for x in self.container]
        print(lru_elements)
  
  
 
# definition of lru decorator
def LRUDecorator(size):
     
    lru = LRUCache(size)
     
    def decorator(function):
         
        def functionality(num):
            lru.insert(num)
            lru.print()
             
            # to check the num pageframe(position)
            # uncomment the below statement
            # print(lur.map)
            print(num, function(num))
        return functionality
     
    return decorator
  
     
# Using LRU Decorator
@LRUDecorator(size=4)
def ex_func_01(n):
    print(f'Computing...{n}')
    time.sleep(1)
    return n
          
print(f'\nFunction: ex_func_01')
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(5))
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(5))

"""
Output:
 
Function: ex_func_01
[1]
Computing...1
1 1
None
[2, 1]
Computing...2
2 2
None
[3, 2, 1]
Computing...3
3 3
None
[4, 3, 2, 1]
Computing...4
4 4
None
[1, 4, 3, 2]
Computing...1
1 1
None
[2, 1, 4, 3]
Computing...2
2 2
None
[5, 2, 1, 4]
Computing...5
5 5
None
[1, 5, 2, 4]
Computing...1
1 1
None
[2, 1, 5, 4]
Computing...2
2 2
None
[3, 2, 1, 5]
Computing...3
3 3
None
[4, 3, 2, 1]
Computing...4
4 4
None
[5, 4, 3, 2]
Computing...5
5 5
None
"""