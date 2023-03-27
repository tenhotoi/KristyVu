"""
[Day 35 of 100 Days]As a software engineer, it's important to have a solid understanding of data structures and algorithms. In this post, we'll explore a common data structure - linked lists - and demonstrate how to solve a specific problem involving linked lists.
The problem is as follows: given the head of a linked list and an integer value val, remove all the nodes in the linked list that have value val, and return the new head of the linked list.
Let's break down the problem and solution. A linked list is a data structure that consists of a sequence of nodes, where each node contains some data and a pointer to the next node in the sequence. The head of the linked list is the first node in the sequence.
To solve the problem, we need to iterate through the linked list and remove any nodes that have value val. We can do this by keeping track of the previous node while iterating, so that we can update the next pointer of the previous node to skip over any nodes with value val.
The removeElements function takes in the head of the linked list and an integer value val to remove. First, we skip any leading nodes with value val, since they should be removed. Then, we iterate through the remaining nodes and remove any nodes with value val. We keep track of the previous node using the prev variable. If the current node has value val, we remove it by updating the next pointer of the previous node to skip over the current node. If the current node does not have value val, we update prev and move on to the next node. Finally, we return the head of the updated linked list.
In summary, solving problems involving linked lists requires a solid understanding of the data structure, as well as algorithms for traversing and manipulating the list. By following a systematic approach, as demonstrated in the solution above, we can effectively solve these types of problems.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    # Skip any leading nodes with value val
    while head and head.val == val:
        head = head.next

    # Remove any remaining nodes with value val
    curr = head
    prev = None
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next

    return head

    