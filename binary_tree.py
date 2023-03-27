
def binary_tree_paths(root):
    if not root:
        return []
    paths = []
    dfs(root, "", paths)
    return paths

def dfs(node, path, paths):
    if not node.left and not node.right:
        paths.append(path + str(node.val))
    if node.left:
        dfs(node.left, path + str(node.val) + "->", paths)
    if node.right:
        dfs(node.right, path + str(node.val) + "->", paths)

# https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/?ref=rp
"""
Example 1
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7


Example 2
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30
Solution:

Following is a 3 step solution for converting Binary tree to Binary Search Tree.

Create a temp array arr[] that stores inorder traversal of the tree. This step takes O(n) time.
Sort the temp array arr[]. Time complexity of this step depends upon the sorting algorithm. In the following implementation, Quick Sort is used which takes (n^2) time. This can be done in O(nLogn) time using Heap Sort or Merge Sort.
Again do inorder traversal of tree and copy array elements to tree nodes one by one. This step takes O(n) time.
Following is the implementation of the above approach. The main function to convert is highlighted in the following code.

Implementation:
"""
# Program to convert binary tree to BST
 
# A binary tree node
class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# Helper function to store the inorder traversal of a tree
def storeInorder(root, inorder):
     
    # Base Case
    if root is None:
        return
     
    # First store the left subtree
    storeInorder(root.left, inorder)
     
    # Copy the root's data
    inorder.append(root.data)
 
    # Finally store the right subtree
    storeInorder(root.right, inorder)
 
# A helper function to count nodes in a binary tree
def countNodes(root):
    if root is None:
        return 0
 
    return countNodes(root.left) + countNodes(root.right) + 1
 
# Helper function that copies contents of sorted array
# to Binary tree
def arrayToBST(arr, root):
 
    # Base Case
    if root is None:
        return
     
    # First update the left subtree
    arrayToBST(arr, root.left)
 
    # now update root's data delete the value from array
    root.data = arr[0]
    arr.pop(0)
 
    # Finally update the right subtree
    arrayToBST(arr, root.right)
 
# This function converts a given binary tree to BST
def binaryTreeToBST(root):
     
    # Base Case: Tree is empty
    if root is None:
        return
     
    # Count the number of nodes in Binary Tree so that
    # we know the size of temporary array to be created
    n = countNodes(root)
 
    # Create the temp array and store the inorder traversal
    # of tree
    arr = []
    storeInorder(root, arr)
     
    # Sort the array
    arr.sort()
 
    # copy array elements back to binary tree
    arrayToBST(arr, root)
 
# Print the inorder traversal of the tree
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print (root.data,end=" ")
    printInorder(root.right)

if __name__ == '__main__':
    # Driver program to test above function
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)
    """
          10
         /  \
        30   15
       /      \
      20       5
    """    
    # Convert binary tree to BST
    binaryTreeToBST(root)   
    print ("Following is the inorder traversal of the converted BST")
    printInorder(root)
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

"""
Output
Following is the inorder traversal of the converted BST
5 10 15 20 30
Complexity Analysis:

Time Complexity: O(nlogn). This is the complexity of the sorting algorithm which we are using after first in-order traversal, rest of the operations take place in linear time.
Auxiliary Space: O(n). Use of data structure ‘array’ to store in-order traversal.
We will be covering another method for this problem which converts the tree using O(height of the tree) extra space.
"""

# https://www.geeksforgeeks.org/binary-tree-binary-search-tree-conversion-using-stl-set/?ref=rp
# Python3 program to convert a Binary tree
# to BST using sets as containers.
 
# Binary Tree Node
""" A utility function to create a
new BST node """
class newNode:
 
    # Construct to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# function to store the nodes in set
# while doing inorder traversal.
def storeinorderInSet(root, s):
 
    if (not root) :
        return
 
    # visit the left subtree first
    storeinorderInSet(root.left, s)
 
    # insertion takes order of O(logn)
    # for sets
    s.add(root.data)
 
    # visit the right subtree
    storeinorderInSet(root.right, s)

    """ 
    Constructing tree given in the above figure
        5
        / \
       7   9
      /\  / \
     1 6 10 11 
    """
     
# Time complexity = O(nlogn)
 
# function to copy items of set one by one
# to the tree while doing inorder traversal
def setToBST(s, root) :
    print(f's is {s}')
    # base condition
    if (not root):
        return
 
    # first move to the left subtree and
    # update items
    setToBST(s, root.left)
 
    # iterator initially pointing to
    # the beginning of set
    it = next(iter(s))
    print(f'it is {it}')
    
    # copying the item at beginning of
    # set(sorted) to the tree.
    root.data = it
 
    # now erasing the beginning item from set.
    s.remove(it)
    print(f's after removing it: {s}')
    # now move to right subtree
    # and update items
    setToBST(s, root.right)

    """ 
    Constructing tree given in the above figure
        5
        / \
       7   9
      /\  / \
     1 6 10 11 
    """
"""
s is {1, 5, 6, 7, 9, 10, 11}
s is {1, 5, 6, 7, 9, 10, 11}
s is {1, 5, 6, 7, 9, 10, 11}
s is {1, 5, 6, 7, 9, 10, 11}
it is 1
s after removing it: {5, 6, 7, 9, 10, 11}
s is {5, 6, 7, 9, 10, 11}
it is 5
s after removing it: {6, 7, 9, 10, 11}
s is {6, 7, 9, 10, 11}
s is {6, 7, 9, 10, 11}
it is 6
s after removing it: {7, 9, 10, 11}
s is {7, 9, 10, 11}
it is 7
s after removing it: {9, 10, 11}
s is {9, 10, 11}
s is {9, 10, 11}
s is {9, 10, 11}
it is 9
s after removing it: {10, 11}
s is {10, 11}
it is 10
s after removing it: {11}
s is {11}
s is {11}
it is 11
s after removing it: set()
s is set()
""" 

# T(n) = O(nlogn) time
# Converts Binary tree to BST.
def binaryTreeToBST(root):
 
    s = set()
 
    # populating the set with the tree's
    # inorder traversal data
    storeinorderInSet(root, s)
 
    # now sets are by default sorted as
    # they are implemented using self-
    # balancing BST
 
    # copying items from set to the tree
    # while inorder traversal which makes a BST
    setToBST(s, root)
 
# Time complexity = O(nlogn),
# Auxiliary Space = O(n) for set.
 
# function to do inorder traversal
def inorder(root) :
 
    if (not root) :
        return
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)
 
# Driver Code
if __name__ == '__main__':
 
    root = newNode(5)
    root.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(10)
    root.left.left = newNode(1)
    root.left.right = newNode(6)
    root.right.right = newNode(11)
 
    """ 
    Constructing tree given in the above figure
        5
        / \
       7   9
      /\  / \
     1 6 10 11 
    """
 
    # converting the above Binary tree to BST
    binaryTreeToBST(root)
    print("\nInorder traversal of BST is: ")
    inorder(root)
    # Inorder traversal of BST is:
    # 1 5 6 7 9 10 11
 
# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)

"""
Output
Inorder traversal of BST is: 
1 5 6 7 9 10 11 
"""

# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/?ref=rp

# A utility function to search a given key in BST
def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        print(f'\n{key} is found in root.val')
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
"""

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
        print(root.val, end=' ')
        inorder(root.right)
 
 
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
    print()
    # Print inoder traversal of the BST
    inorder(r)      # 20 30 40 50 60 70 80 

    inorder(search(r, 70))
    # 70 is found in root.val
    # 60 70 80

"""
Output
20 30 40 50 60 70 80

Time Complexity: The worst-case time complexity of search and insert operations is O(h) where h is the height of the Binary Search Tree. 
In the worst case, we may have to travel from the root to the deepest leaf node. 
The height of a skewed tree may become n and the time complexity of the search and insert operation may become O(n). 
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
        print()
        tree.inorder()  # 10 15 20 30 40 50 60
"""
    Constructing tree given in the above figure
        30
        / \
       15   50
      /\  / \
    10 20 40 60 
    
<in the left: 30 was appended to stack> <in the left: 15 was appended to stack> <in the left: 10 was appended to stack> 10 15 
<in the left: 20 was appended to stack> 20 30 
<in the left: 50 was appended to stack> <in the left: 40 was appended to stack> 40 50 
<in the left: 60 was appended to stack> 60   
""" 
 
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
                print (f'<in the left: {temp.val} was appended to stack>', end=' ')
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.val), end=" ")
                temp = temp.right
 
"""
    Constructing tree given in the above figure
        30
        / \
       15   50
      /\  / \
    10 20 40 60 
    
<in the left: 30 was appended to stack> <in the left: 15 was appended to stack> <in the left: 10 was appended to stack> 10 15 
<in the left: 20 was appended to stack> 20 30 
<in the left: 50 was appended to stack> <in the left: 40 was appended to stack> 40 50 
<in the left: 60 was appended to stack> 60   
""" 

if __name__ == "__main__":
    GFG.main([])
 
    # This code is contributed by rastogik346.

"""
Output
10 15 20 30 40 50 60 
Time Complexity: O(N)
Auxiliary Space: O(N)
"""


 