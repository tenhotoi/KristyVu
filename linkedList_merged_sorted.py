# https://www.geeksforgeeks.org/python-program-for-merging-two-sorted-linked-lists-such-that-merged-list-is-in-reverse-order/?ref=rp

"""
Given two linked lists sorted in increasing order. Merge them such a way that the result list is in decreasing order (reverse order).

Examples: 

Input:  a: 5->10->15->40
        b: 2->3->20 
Output: res: 40->20->15->10->5->3->2

Input:  a: NULL
        b: 2->3->20 
Output: res: 20->3->2
Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
A Simple Solution is to do following. 
1) Reverse first list ‘a’. 
2) Reverse second list ‘b’. 
3) Merge two reversed lists.
Another Simple Solution is first Merge both lists, then reverse the merged list.
Both of the above solutions require two traversals of linked list. 

How to solve without reverse, O(1) auxiliary space (in-place) and only one traversal of both lists? 
The idea is to follow merge style process. Initialize result list as empty. Traverse both lists from beginning to end. Compare current nodes of both lists and insert smaller of two at the beginning of the result list. 

1) Initialize result list as empty: res = NULL.
2) Let 'a' and 'b' be heads first and second lists respectively.
3) While (a != NULL and b != NULL)
    a) Find the smaller of two (Current 'a' and 'b')
    b) Insert the smaller value node at the front of the result.
    c) Move ahead in the list of the smaller nodes. 
4) If 'b' becomes NULL before 'a', insert all nodes of 'a' 
   into the result list at the beginning.
5) If 'a' becomes NULL before 'b', insert all nodes of 'a' 
   into result list at the beginning. 
Below is the implementation of above solution.
"""

# Given two sorted non-empty linked lists. 
# Merge them in such a way that the result 
# list will be in reverse order. Reversing 
# of linked list is not allowed. Also,
# extra space should be O(1) 
  
# Node of a linked list 
class Node: 
    def __init__(self, next = None, 
                 data = None): 
        self.next = next
        self.data = data 
  
# Given two non-empty linked lists 
# 'a' and 'b'
def SortedMerge(a,b):
  
    # If both lists are empty
    if (a == None and b == None):
        return None
  
    # Initialize head of the 
    # resultant list
    res = None
  
    # Traverse both lists while both 
    # of then have nodes.
    while (a != None and b != None):
      
        # If a's current value is smaller 
        # or equal to b's current value.
        if (a.key <= b.key):
          
            # Store next of current Node 
            # in first list
            temp = a.next
  
            # Add 'a' at the front of 
            # resultant list
            a.next = res
            res = a
  
            # Move ahead in first list
            a = temp
          
        # If a's value is greater. Below steps 
        # are similar to above (Only 'a' is 
        # replaced with 'b')
        else:        
            temp = b.next
            b.next = res
            res = b
            b = temp
          
    # If second list reached end, but first 
    # list has nodes. Add remaining nodes of 
    # first list at the front of result list
    while (a != None):    
        temp = a.next
        a.next = res
        res = a
        a = temp
      
    # If first list reached end, but second 
    # list has node. Add remaining nodes of 
    # first list at the front of result list
    while (b != None):
      
        temp = b.next
        b.next = res
        res = b
        b = temp
      
    return res
  
# Function to print Nodes in a given 
# linked list 
def printList(Node):
  
    while (Node != None):
      
        print( Node.key, end = " ")
        Node = Node.next
    print()
      
# Utility function to create a new 
# node with given key 
def newNode(key):
    temp = Node()
    temp.key = key
    temp.next = None
    return temp
  
# Driver code
# Start with the empty list 
res = None
  
# Let us create two sorted linked lists 
# to test the above functions. Created 
# lists shall be
#     a: 5.10.15
#     b: 2.3.20 
a = newNode(5)
a.next = newNode(10)
a.next.next = newNode(15)
  
b = newNode(2)
b.next = newNode(3)
b.next.next = newNode(20)
  
print("List A before merge: ")
printList(a)
  
print("List B before merge: ")
printList(b)
  
# Merge 2 increasing order LLs 
# in descresing order 
res = SortedMerge(a, b)
  
print("Merged Linked List is: ")
printList(res)
# This code is contributed by Arnab Kundu

"""
Output: 

List A before merge: 
5 10 15 
List B before merge: 
2 3 20 
Merged Linked List is: 
20 15 10 5 3 2 
Time Complexity: O(N)

Auxiliary Space: O(1)

This solution traverses both lists only once, doesn’t require reverse and works in-place.
This article is contributed by Mohammed Raqeeb. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above
"""