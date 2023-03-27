"""
[Day 37 of 100 Days]As a software engineer, you might come across a problem where you need to reverse a singly linked list. This problem might sound simple, but it can test your understanding of data structures and algorithms.

The problem statement is as follows: Given the head of a singly linked list, reverse the list, and return the reversed list.

A singly linked list is a data structure where each node in the list points to the next node, except for the last node, which points to None. To reverse a singly linked list, we need to update the next pointers of each node in the list so that they point to the previous node instead of the next node.

The reverseList function takes the head of the original list as an argument and returns the head of the reversed list. We initialize two pointers: prev points to the previous node (initialized to None), and curr points to the current node (initialized to the head of the original list). We then traverse the list, updating the next pointers of each node to point to the previous node instead of the next node. Once we reach the end of the list, the prev pointer points to the head of the reversed list, so we return it.

In conclusion, reversing a singly linked list might sound simple, but it can test your understanding of data structures and algorithms. I hope this post helps you to understand the problem and its solution. 
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    # Initiate pointers
    prev = None
    curr = head

    # Traverse the list, updating pointers
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Return the new head
    return prev

# Function to insert node
def insert(root, item):
    temp = ListNode(item)
      
    if (root == None):
        root = temp
    else :
        ptr = root
        while (ptr.next != None):
            ptr = ptr.next
        ptr.next = temp
      
    return root

def display(root): 
    while (root.next != None): 
        print(root.val, end="->") 
        root = root.next 
    print(root.val, '\n')
  
def revertArrayToList(arr, n): 
    root = None 
    for i in range(n - 1, -1, -1): 
        print('i is currently: ', i)
        root = insert(root, arr[i])
        # display(root)
    return root 

def revertArrayToListKristy(arr, n): 
    root = None 
    for each in arr[n-1::-1]: 
        root = insert(root, each)
        # display(root)
    return root 

def arrayToList(arr, n): 
    root = None 
    for i in range(n): 
        print('i is currently: ', i)
        root = insert(root, arr[i])
        # display(root)
    return root 

import linkedlistTesting

# Driver code 
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5]; 
    n = len(arr) - 1
    root = arrayToList(arr, n); 
    display(root) 
    root = revertArrayToList(arr, n); 
    display(root) 
    root = revertArrayToListKristy(arr, n); 
    display(root) 
    root = reverseList(root); 
    display(root) 
    root = linkedlistTesting.removeElements(root,3)
    display(root) 



