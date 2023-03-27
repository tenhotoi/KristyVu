# https://www.geeksforgeeks.org/stack-queue-python-using-module-queue/?ref=rp

import queue
 
# ======================================= QUEUE ============================================
# From class queue, Queue is
# created as an object Now L
# is Queue of a maximum
# capacity of 20
L = queue.Queue(maxsize=20)
 
# Data is inserted into Queue
# using put() Data is inserted
# at the end
L.put(5)
L.put(9)
L.put(1)
L.put(7)
 
# get() takes data out from
# the Queue from the head
# of the Queue
print(L.get())
print(L.get())
print(L.get())
print(L.get())

L = queue.Queue(maxsize=6)
 
# qsize() give the maxsize
# of the Queue
print(L.qsize())
 
L.put(5)
L.put(9)
L.put(1)
L.put(7)
 
# Return Boolean for Full
# Queue
print("Full: ", L.full())

L.put(9)
L.put(10)
print("Full: ", L.full())
 
print(L.get())
print(L.get())
print(L.get())
 
# Return Boolean for Empty
# Queue
print("Empty: ", L.empty())
 
print(L.get())
print(L.get())
print(L.get())
 
print("Empty: ", L.empty())
print("Full: ", L.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(L.get())

import queue
 
L = queue.LifoQueue(maxsize=6)
 
# qsize() give the maxsize of
# the Queue
print(L.qsize())
 
# Data Inserted as 5->9->1->7,
# same as Queue
L.put(5)
L.put(9)
L.put(1)
L.put(7)
L.put(9)
L.put(10)
print("Full: ", L.full())
print("Size: ", L.qsize())

# Data will be accessed in the
# reverse order Reverse of that
# of Queue
print(L.get())
print(L.get())
print(L.get())
print(L.get())
print(L.get())
print("Empty: ", L.empty())

# ======================================= STACK ============================================
# Python program to
# demonstrate stack implementation
# using list
  
stack = []
  
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
  
print('Initial stack')
print(stack)
  
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
  
print('\nStack after elements are popped:')
print(stack)
  
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
"""
Output
Initial stack
['a', 'b', 'c']

Elements popped from stack:
c
b
a

Stack after elements are popped:
[]
"""

# Python program to
# demonstrate stack implementation
# using collections.deque
  
from collections import deque
  
stack = deque()
  
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
  
print('Initial stack:')
print(stack)
  
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
  
print('\nStack after elements are popped:')
print(stack)
  
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

# Python program to
# demonstrate stack implementation
# using queue module
  
from queue import LifoQueue
  
# Initializing a stack
stack = LifoQueue(maxsize=3)
  
# qsize() show the number of elements
# in the stack
print(stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
  
print("Full: ", stack.full())
print("Size: ", stack.qsize())
  
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
  
print("\nEmpty: ", stack.empty())

# Python program to demonstrate
# stack implementation using a linked list.
# node class
  
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
  
  
class Stack:
  
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
  
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
  
    # Get the current size of the stack
    def getSize(self):
        return self.size
  
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
  
    # Get the top item of the stack
    def peek(self):
  
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
  
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
  
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
  
  
# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
  
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")