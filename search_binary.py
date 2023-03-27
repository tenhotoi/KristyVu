# looking for an item in a sorted list
def binarySearch(val, arr, low, high):
    if low >= (high - 1):
        return
    if len(arr) == 0:
        return 'WARNING: Empty array.'

    if low < 0 or high > (len(arr) - 1):
        return 'Please have valid low and high index values.'
    
    mid = (low + high) // 2
    print('low, high, mid is: ', low, high, mid)
    if arr[mid] == val:
        return mid
    elif arr[low] == val:
        return low
    elif arr[high] == val:
        return high
    elif arr[mid] < val:
        return binarySearch(val, arr, mid, high)
    else:
        return binarySearch(val, arr, low, mid)

def biSearch(val, arr):
    if len(arr) <= 1:
        return 'WARNING: No need to search since array size is either empty or only 1 element.'

    low = 0
    high = len(arr) - 1
    while low < (high - 1):
        mid = (high + low) // 2
        print('low, high, mid are: ', low, high, mid)
        midval = arr[mid]
        print('midval is: ', midval)
        if arr[mid] == val:
            return mid
        elif arr[low] == val:
            return low
        elif arr[high] == val:
            return high
        elif arr[mid] < val:
            low = mid
        else:
            high = mid
        
    

array = [2, 9, 1, 0, 3, 5, 6, 3, 3, 7]
array.sort()
searchfor = [0, 5, 4, 9]
for i in searchfor:
    print('array before biSearch is: ', array)
    index = biSearch(i, array)
    print(i, ' is found at index: ', index)
    index = binarySearch(i, array, 0, len(array) - 1)
    print(i, ' is found at index: ', index)

"""
array before biSearch is:  [0, 1, 2, 3, 3, 3, 5, 6, 7, 9]
low, high, mid are:  0 9 4
midval is:  3
0  is found at index:  0
low, high, mid is:  0 9 4
0  is found at index:  0
array before biSearch is:  [0, 1, 2, 3, 3, 3, 5, 6, 7, 9]
low, high, mid are:  0 9 4
midval is:  3
low, high, mid are:  4 9 6
midval is:  5
5  is found at index:  6
low, high, mid is:  0 9 4
low, high, mid is:  4 9 6
5  is found at index:  6
array before biSearch is:  [0, 1, 2, 3, 3, 3, 5, 6, 7, 9]
low, high, mid are:  0 9 4
midval is:  3
low, high, mid are:  4 9 6
midval is:  5
low, high, mid are:  4 6 5
midval is:  3
4  is found at index:  None
low, high, mid is:  0 9 4
low, high, mid is:  4 9 6
low, high, mid is:  4 6 5
4  is found at index:  None
array before biSearch is:  [0, 1, 2, 3, 3, 3, 5, 6, 7, 9]
low, high, mid are:  0 9 4
midval is:  3
9  is found at index:  9
low, high, mid is:  0 9 4
9  is found at index:  9
"""

# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/?ref=rp
# Python program to demonstrate
# insert operation in binary search tree
 
# A utility class that represents
# an individual node in a BST
 
 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert
# a new node with the given key
 

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
 
# This code is contributed by Bhavya Jain

"""
Time complexity: O(h), where h is the height of the BST.
Space complexity: O(h), where h is the height of the BST. This is because the maximum amount of space needed to store the recursion stack would be h.

Illustration to search 6 in below tree: 

Start from the root. 
Compare the searching element with root, if less than root, then recursively call left subtree, else recursively call right subtree. 
If the element to search is found anywhere, return true, else return false. 

For searching a value, if we had a sorted array we could have performed a binary search. Let’s say we want to search a number in the array, 
in binary search, we first define the complete list as our search space, the number can exist only within the search space. 
"""
 
# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80

if __name__ == '__main__':
    r = Node(50)
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)
    print('r is: ', r)
    
    # Print inoder traversal of the BST
    inorder(r)
    print('r after inorder is: ', r)

"""
Output
20
30
40
50
60
70
80

Time Complexity: The worst-case time complexity of search and insert operations is O(h) where h is the height of the Binary Search Tree. In the worst case, we may have to travel from the root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of the search and insert operation may become O(n). 
Auxiliary Space: O(1)

Implementation: Insertion using the loop.
"""

class GFG:
    @staticmethod
    def main(args):
        tree = BST()
        tree.insert(30)
        tree.insert(50)
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.inorder()
 
 
class Node:
    left = None
    val = 0
    right = None
 
    def __init__(self, val):
        self.val = val
 
 
class BST:
    root = None
 
    def insert(self, key):
        node = Node(key)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
        while (temp != None):
            if (temp.val > key):
                prev = temp
                temp = temp.left
            elif(temp.val < key):
                prev = temp
                temp = temp.right
        if (prev.val > key):
            prev.left = node
        else:
            prev.right = node
 
    def inorder(self):
        temp = self.root
        stack = []
        while (temp != None or not (len(stack) == 0)):
            if (temp != None):
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.val) + " ", end="")
                temp = temp.right
 
 
if __name__ == "__main__":
    GFG.main([])
 
    # This code is contributed by rastogik346.

"""
Output
10 15 20 30 40 50 60 
Time Complexity: O(N)
Auxiliary Space: O(N)
"""


 
