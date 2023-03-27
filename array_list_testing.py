# Time complexity : O(N) 
# Auxiliary Space : O(1)

"""
Several methods are:

1. Using another temporary array.
2. Rotating one by one.
3. Using a juggling algorithm.
"""

def rotate1(L, d, n):
    # k = L.index(d)
    # new_lis = []
    # new_lis = L[k+1:]+L[0:k+1]
    new_lis = L[d:]+L[0:d]
    return new_lis
 
 
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    N = len(arr)

    print("\n arr before rotating: ", arr, "\n")
    # Function call
    arr = rotate1(arr, d, N)
    for i in arr:
        print(i, end=" ")
    print("\n")

# Python program to rotate an array by d elements
 
# Function to left rotate arr[] of size n by d
def Rotate(arr, d, n):
  p = 1
  while(p <= d):
    last = arr[0]
    for i in range (n - 1):
      arr[i] = arr[i + 1]
    arr[n - 1] = last
    p = p + 1
     
# Function to print an array
def printArray(arr, size):
  for i in range (size):
    print(arr[i] ,end = " ")
  print("\n")
     
# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
N = len(arr)
d = 2
 
# Function calling
Rotate(arr, d, N)
printArray(arr, N)
 
# This code is contributed by Atul_kumar_Shrivastava

# Python3 program to rotate an array by
# d elements
# Function to left rotate arr[] of size n by d
 
 
def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
 
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while 1:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp
 
# UTILITY FUNCTIONS
# function to print an array
 
 
def printArray(arr, size):
    for i in range(size):
        print("% d" % arr[i], end=" ")
    print("\n")
 
# Function to get gcd of a and b
 
 
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
 
 
# Driver program to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
printArray(arr, n)
 
# This code is contributed by Shreyanshi Arun
# https://www.geeksforgeeks.org/array-rotation/

from collections import deque
 
#Taking input -- elements
inp=[1,2,3,4,5,6,7]
#input -- Number of rotations
d=2
 
#Changing from list to deque structure
deq = deque(inp)
 
#To know the type of data structure
U = type(deq)                         #If we print-- Output: <class 'collections.deque'>
 
 
#Rotating left using rotate function
#To rotate left use (-), Ex: rotate(-3)
#To rotate right by 3 elements Ex: rotate(3)
 
deq.rotate(-d)
print(deq)


# Python3 code for above implementation
 
# Wrapper over the recursive function leftRotateRec()
# It left rotates arr by d.
 
 
''' UTILITY FUNCTIONS '''
''' function to print an array '''
 
 
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()
 
 
'''
 * This function swaps d elements starting at
 * index fi with d elements starting at index si
 '''
 
 
def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp
 
 
def leftRotate(arr, d, n):
    if(d == 0 or d == n):
        return
    i = d
    j = n - d
    while (i != j):
 
        if(i < j):  # A is shorter
            swap(arr, d - i, d + j - i, i)
            j -= i
 
        else:  # B is shorter
            swap(arr, d - i, d, j)
            i -= j
 
    swap(arr, d - i, d, i)
 
 
    # Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    leftRotate(arr, 2, 7)
    printArray(arr, 7)

# https://www.geeksforgeeks.org/block-swap-algorithm-for-array-rotation/

# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

# Python program for reversal algorithm of array rotation
 
# Function to reverse arr[] from index start to end
 
 
def reverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end-1
 
# Function to left rotate arr[] of size n by d
 
 
def leftRotate(arr, d):
 
    if d == 0:
        return
    n = len(arr)
    # in case the rotating factor is
    # greater than array length
    d = d % n
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
 
# Function to print an array
 
 
def printArray2(arr):
    for i in range(0, len(arr)):
        print (arr[i],end=' ')
    print('\n')
 
 
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
d = 2
 
leftRotate(arr, d)  # Rotate array by 2
printArray2(arr)
 
# This code is contributed by Devesh Agrawal

# Function to rotate an array by k elements to the right
def rotateArray(arr, k):
    # Find the size of the array
    n = len(arr);
 
    # Mod k with the size of the array
    # To handle the case where k is greater than the size of the array
    k %= n;
 
    # Reverse the entire array
    arr[0:n] = arr[0:n][::-1]
 
    # Reverse the first k elements
    arr[0:k] = arr[0:k][::-1]
 
    # Reverse the remaining n-k elements
    arr[k:n] = arr[k:n][::-1]
 
# Initialize the array
arr = [ 1, 2, 3, 4, 5 ];
 
# Number of elements to rotate to the right
k = 2;
 
# Call the rotateArray function to rotate the array
rotateArray(arr, k);
 
# Print the rotated array
for i in range(0,len(arr)):
    print(arr[i], end= " ");

# >>>>>>>>>>>>>>>>>>>>>>> Python 3 code to demonstrate <<<<<<<<<<<<<<<<<<<<<<<<<
# removing duplicated from list
# using set()
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
 
# using set()
# to remove duplicated
# from list
test_list = list(set(test_list))
 
# printing list after removal
# distorted ordering
print ("The list after removing duplicates : "
        + str(test_list))

# >>>>>>>>>>>>>>>>>>>>>>>   Python 3 code to demonstrate  <<<<<<<<<<<<<<<<<<<<<<<<<
# removing duplicated from list
# using list comprehension + enumerate()
 
# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : "
        + str(test_list))
 
# using list comprehension + enumerate()
# to remove duplicated
# from list
# solution would be O(n^2). This is just unacceptable for such a trivial problem
# To take the first appearance use:
res = [i for n, i in enumerate(test_list) if i not in test_list[:n]]
 
# printing list after removal
print ("The list after removing duplicates with the first appearance use: "
        + str(res))

# To take the last appearance use:
res = [i for n, i in enumerate(test_list) if i not in test_list[n + 1:]]
 
# printing list after removal
print ("The list after removing duplicates with the last appearance use: "
        + str(res))

# https://stackoverflow.com/questions/480214/how-do-i-remove-duplicates-from-a-list-while-preserving-order
items = [1, 2, 0, 1, 3, 2]
a = list(dict.fromkeys(items))  # Or [*dict.fromkeys(items)] if you prefer
print('result of list of dictionary is: ', a)

# http://www.peterbe.com/plog/uniqifiers-benchmark

def f1(seq):
   # not order preserving
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

def f2(seq): 
   # order preserving
   checked = []
   for e in seq:
       if e not in checked:
           checked.append(e)
   return checked

def f3(seq):
   # Not order preserving
   keys = {}
   for e in seq:
       keys[e] = 1
   return keys.keys()

def f4(seq): 
   # order preserving
   noDupes = []
   [noDupes.append(i) for i in seq if not noDupes.count(i)]
   return noDupes

def f5(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

def f6(seq):
   # Not order preserving    
   setarr = set(seq)
   return list(setarr)

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

test_list = [1, 5, 3, 6, 3, 5, 6, 1]
a = f1(test_list)
print('result of f1 is: ', a)

a = f2(test_list)
print('result of f2 is: ', a)

a = f3(test_list)
print('result of f3 is: ', a)

a = f4(test_list)
print('result of f4 is: ', a)

a = f5(test_list)
print('result of f5 is: ', a)

a = f6(test_list)
print('result of f6 is: ', a)

a = f7(test_list)
print('result of f7 is: ', a)

# https://stackoverflow.com/questions/1549509/remove-duplicates-in-a-list-while-keeping-its-order-python
# The downside is that it causes an extra sort, thus an unneeded O(n * log(n)) (where otherwise O(n) would be sufficient).
mylist = ['c','a','a','b','a','b','c']
print(a := sorted(set(mylist), key=lambda x: mylist.index(x)))
print('result of sorted index is: ', a)

# try dict to reserse the order:
# mylist = [2, 5, 9, 0, 1]
print(a := list(dict.fromkeys(mylist)))

"""
Output:
['c', 'a', 'b']
result of sorted index is:  ['c', 'a', 'b']
['c', 'a', 'b']
"""

# https://leetcode.com/discuss/interview-question/217646/cisco-meraki-phone-merge-intervals
"""
Merge Intervals (LeetCode #56)

Given a list of intervals, combine all intervals that overlap and return a list of the reduced intervals.

Input: [[1,10],[2,5],[3,11],[14,20]]
Output: [[1,11],[14,20]]

Input: [[1,4], [2, 8], [9, 12], [14, 15]]
Output: [[1,8], [9, 12], [14,15]]

Greedy N*log(N):
vector answer;
sort(intervals.begin(),intervals.end()); // sort by starting time
for(int i=0;i<intervals.size();i++) {
    interval next = intervals[i];
    while(i<intervals.size() && next.end > intervals[i+1].start) {
        next.end=max(next.end,intervals[i+1].end); // get the max end time of all overlapping
        i++:
    }
    answer.push(next);
}
return answer;
"""
# https://www.interviewbit.com/blog/merge-intervals/
# >>>>>>>>>>>>>>>>> Approach 1: Brute Force <<<<<<<<<<<<<<<<<
def isOverlap(minS, maxE, interval):
 
    if minS > interval[1] or maxE < interval[0]:
        return False
 
    return True
 
 
def mergeIntervalsSol1(intervals):
    n = len(intervals)
 
    res = []
 
    vis = [False for i in range(n)]
 
    for i in range(n):
        if vis[i] is True:
            continue
 
        vis[i] = True
        minS = intervals[i][0]
        maxE = intervals[i][1]
 
        while 1:
            cnt = 0
 
            for j in range(n):
 
                if vis[j] is False and isOverlap(minS, maxE, intervals[j]):
 
                    vis[j] = True
                    minS = min(minS, intervals[j][0])
                    maxE = max(maxE, intervals[j][1])
                    cnt += 1
            if cnt == 0:
                break

        res.append([minS, maxE])
 
    return res

# Time Complexity: O(N^2), where N is total size of the interval array
# Space Complexity: O(N), as visiting array is used.

# >>>>>>>>>>>>>>>> Approach 2: Sorting <<<<<<<<<<<<<<<<
def mergeIntervalsSol2(intervals: list[list[int]]) -> list[list[int]]:
 
    intervals.sort(key=lambda x: x[0])
 
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
            print(merged)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
 
    return merged

# Time Complexity: O(NlogN), where N is total size of the array
# Space Complexity: O(N), where N is total size of the merged array


intervals = [[1, 3],[2, 6],[8, 10],[15, 18]]
a = mergeIntervalsSol1(intervals)
print('mergeInterval output: ', a)

intervals = [[1, 3],[2, 6],[8, 10],[15, 18]]
a = mergeIntervalsSol2(intervals)
print('merge output: ', a)


# https://www.tutorialspoint.com/merge-intervals-in-python
class Solution(object):
   def merge(self, intervals):
      """
      :type intervals: List[Interval]
      :rtype: List[Interval]
      """
      if len(intervals) == 0:
         return []
      self.quicksort(intervals,0,len(intervals)-1)
      #for i in intervals:
         #print(i.start, i.end)
      stack = []
      stack.append(intervals[0])
      for i in range(1,len(intervals)):
         last_element= stack[len(stack)-1]
         if last_element[1] >= intervals[i][0]:
            last_element[1] = max(intervals[i][1],last_element[1])
            stack.pop(len(stack)-1)
            stack.append(last_element)
         else:
            stack.append(intervals[i])
      return stack
   def partition(self,array,start,end):
      pivot_index = start
      for i in range(start,end):
         if array[i][0]<=array[end][0]:
            array[i],array[pivot_index] =array[pivot_index],array[i]
            pivot_index+=1
      array[end],array[pivot_index] =array[pivot_index],array[end]
      return pivot_index
   def quicksort(self,array,start,end):
      if start<end:
         partition_index = self.partition(array,start,end)
         self.quicksort(array,start,partition_index-1)
         self.quicksort(array, partition_index + 1, end)

ob1 = Solution()
print(ob1.merge([[1,3],[2,6],[8,10],[15,18]]))
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1, 6], [8, 10], [15, 18]]

# https://www.geeksforgeeks.org/sum-consecutive-elements-array/
arr = [4, 10, 15, 5, 6]

for i in range(len(arr) - 1): 
    print(i)
    arr[i] = arr[i] + arr[i + 1]

arr.pop(-1)
print(arr)
# Output: 14  25  20  11 

# https://www.geeksforgeeks.org/replace-array-elements-by-sum-of-next-two-consecutive-elements/?ref=rp
arr =[3, 4, 2, 1, 6]
first, second = arr[0], arr[1]
for i in range(len(arr) - 2):
    arr[i] = arr[i + 1] + arr[i + 2]

arr[-2] = arr[-1] + first
arr[-1] = first + second
print(arr)
# Output: 6 3 7 9 7

print(['>'] * 10)
# Output: ['>', '>', '>', '>', '>', '>', '>', '>', '>', '>']

# https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/
# initializing list
test_list = [ '4', '6', '7', '2', '1']
from itertools import combinations
print(list(combinations([int(x) for x in test_list], 3)))
# [(4, 6, 7), (4, 6, 2), (4, 6, 1), (4, 7, 2), (4, 7, 1), (4, 2, 1), (6, 7, 2), (6, 7, 1), (6, 2, 1), (7, 2, 1)]
val = 12
print([sol for sol in list(combinations([int(x) for x in test_list], 3)) if sum(sol) == val])
# [(4, 6, 2), (4, 7, 1)]
print(list(filter(lambda x: sum(x)==val, list(combinations([int(x) for x in test_list], 3)))))
# [(4, 6, 2), (4, 7, 1)]