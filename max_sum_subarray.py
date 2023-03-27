# https://www.geeksforgeeks.org/maximum-subarray-sum-using-divide-and-conquer-algorithm/#discuss

"""
You are given a one dimensional array that may contain both positive and negative integers, find the sum of contiguous subarray of numbers which has the largest sum.

For example, if the given array is {-2, -5, 6, -2, -3, 1, 5, -6}, then the maximum subarray sum is 7 (see highlighted elements).

The naive method is to run two loops. The outer loop picks the beginning element, the inner loop finds the maximum possible sum with first element picked by outer loop and compares this maximum with the overall maximum. Finally, return the overall maximum. The time complexity of the Naive method is O(n^2).

Using Divide and Conquer approach, we can find the maximum subarray sum in O(nLogn) time. Following is the Divide and Conquer algorithm. 
Divide the given array in two halves
Return the maximum of following three
Maximum subarray sum in left half (Make a recursive call)
Maximum subarray sum in right half (Make a recursive call)
Maximum subarray sum such that the subarray crosses the midpoint
The lines 2.a and 2.b are simple recursive calls. How to find maximum subarray sum such that the subarray crosses the midpoint? We can easily find the crossing sum in linear time. The idea is simple, find the maximum sum starting from mid point and ending at some point on left of mid, then find the maximum sum starting from mid + 1 and ending with some point on right of mid + 1. Finally, combine the two and return the maximum among left, right and combination of both.

Below is the implementation of the above approach: 
"""

# A Divide and Conquer based program
# for maximum subarray sum problem
  
# Find the maximum possible sum in
# arr[] auch that arr[m] is part of it
  
  
def maxCrossingSum_original(arr, l, m, h):
    print(f'  low, mid, high are: {l}, {m}, {h}  '.center(60,'+'))
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000
  
    for i in range(m, l-1, -1):
        print(f' i value in left of mid is {i}  '.center(60, '='))
        sm = sm + arr[i]
  
        if (sm > left_sum):
            left_sum = sm
    print(f'  left sum AFTER FOR LOOP is now: {left_sum} '.center(60, '-'))
  
    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m, h + 1):
        sm = sm + arr[i]
  
        if (sm > right_sum):
            right_sum = sm
    print(f'  right sum AFTER FOR LOOP is now: {right_sum} '.center(60, '-'))
    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum - arr[m], left_sum, right_sum)
  
def maxCrossingSum(arr, l, m, h):
    print(f'  low, mid, high are: {l}, {m}, {h}  '.center(60,'+'))
    # Include elements on left of mid.
    sm = 0
    left_sum = -10000
  
    for i in range(m, l-1, -1):
        print(f' i value in left of mid is {i}  '.center(60, '='))
        sm = sm + arr[i]
  
        if (sm > left_sum):
            left_sum = sm
        else:
            break

    print(f'  left sum AFTER FOR LOOP is now: {left_sum} '.center(60, '-'))
  
    # Include elements on right of mid
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]
  
        if (sm > right_sum):
            right_sum = sm
        else:
            break

    print(f'  right sum AFTER FOR LOOP is now: {right_sum} '.center(60, '-'))
    # Return sum of elements on left and right of mid
    # returning only left_sum + right_sum will fail for [-2, 1]
    return max(left_sum + right_sum, left_sum, right_sum)
  
# Returns sum of maximum sum subarray in aa[l..h]
def maxSubArraySum(arr, l, h):
    #Invalid Range: low is greater than high
    if (l > h):
        return -10000
    # Base Case: Only one element
    if (l == h):
        return arr[l]
  
    # Find middle point
    m = (l + h) // 2
  
    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    #     subarray crosses the midpoint
    return max(maxSubArraySum(arr, l, m-1),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))
  
  
# Driver Code
arr = [2, 3, 4, 5, 7]
n = len(arr)
  
max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
  
# This code is contributed by Nikita Tiwari.
arr = [-2, 1]
n = len(arr)
  
max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)

"""
For example, if the given array is {-2, -5, 6, -2, -3, 1, 5, -6}, then the maximum subarray sum is 7 (see highlighted elements).
"""
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr)
  
max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)
# Maximum contiguous sum is  7

"""
You are given a one dimensional array that may contain both positive and negative integers, 
find the sum of contiguous subarray of numbers which has the largest sum.

The code failed for below case: Maximum contiguous sum is  102
"""
arr = [100, -5, 6, -2, -3, 1, 5, -6]
n = len(arr)
  
max_sum = maxSubArraySum(arr, 0, n-1)
print("Maximum contiguous sum is ", max_sum)

"""
Output
Maximum contiguous sum is 21n
Time Complexity: maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation. 
T(n) = 2T(n/2) + Θ(n) 

Time Complexity : O(nlogn)

Auxiliary Space: O(1).
The above recurrence is similar to Merge Sort and can be solved either using Recurrence Tree method or Master method. 
It falls in case II of Master Method and solution of the recurrence is Θ(nLogn). 

The Kadane’s Algorithm for this problem takes O(n) time. 
Therefore the Kadane’s algorithm is better than the Divide and Conquer approach, 
but this problem can be considered as a good example to show power of Divide and Conquer. 
The above simple approach where we divide the array in two halves, reduces the time complexity from O(n^2) to O(nLogn).
"""

# https://www.geeksforgeeks.org/maximum-sum-subarray-using-divide-and-conquer-set-2/?ref=rp

# Python3 implementation of the approach
 
class Node:
     
    def __init__(self, x):
         
        # To store the maximum sum for a sub-array
        self._max = x
         
        # To store the maximum prefix sum for a sub-array
        self._pre = x
         
        # To store the maximum suffix sum for a sub-array
        self._suf = x
         
        # To store the total sum for a sub-array
        self._sum = x
         
# Function to merge the 2 nodes left and right
def merg(l, r):
     
    # Creating node ans
    ans = Node(0)
 
    # The max prefix sum of ans Node is maximum of
    # a) max prefix sum of left Node
    # b) sum of left Node + max prefix sum of right Node
    # c) sum of left Node + sum of right Node
    ans._pre = max(l._pre, l._sum + r._pre, l._sum + r._sum)
 
    # The max suffix sum of ans Node is maximum of
    # a) max suffix sum of right Node
    # b) sum of right Node + max suffix sum of left Node
    # c) sum of left Node + sum of right Node
    ans._suf = max(r._suf, r._sum+l._suf, l._sum + r._sum)
     
    # Total sum of ans Node = total sum of
    # left Node + total sum of right Node
    ans._sum = l._sum + r._sum
     
    # The max sum of ans Node stores the answer
    # which is the maximum value among:
    # prefix sum of ans Node
    # suffix sum of ans Node
    # maximum value of left Node
    # maximum value of right Node
    # prefix value of left Node + suffix value of right Node
    ans._max = max(ans._pre, ans._suf, ans._sum,
                    l._max, r._max, l._suf + r._pre)
 
    # Return the ans Node
    return ans
 
# Function for calculating the
# max_sum_subArray using divide and conquer
def getMaxSumSubArray(l, r, ar):
 
    if l == r: return Node(ar[l])
 
    mid = (l + r) // 2
     
    # Call method to return left Node:
    left = getMaxSumSubArray(l, mid, ar)
     
    # Call method to return right Node:
    right = getMaxSumSubArray(mid+1, r, ar)
     
    # Return the merged Node:
    return merg(left, right)
 
# Driver code
if __name__ == "__main__":
 
    ar = [-2, -5, 6, -2, -3, 1, 5, -6]
    n = len(ar)
    ans = getMaxSumSubArray(0, n-1, ar)
    print("Answer is", ans._max)
 
# This code is contributed by Rituraj Jain

"""
Output: 

Answer is 7
Time Complexity: The getMaxSumSubArray() recursive function generates the following recurrence relation. 
T(n) = 2 * T(n / 2) + O(1) note that conquer part takes only O(1) time. 
So on solving this recurrence using Master’s Theorem we get the time complexity of O(n).
"""
l = 4
m = 10
for i in range(m, l-1, -1):
    print(i)

for i in range(m, l, -1):
    print(i)

"""
10
9
8
7
6
5
4  <======== this is (l - 1)

10
9
8
7
6
5
>>>>>>>>>>>>> it won't print anything when '-1' is not there in the 3rd location
"""
l = 0
m = 4
for i in range(m, l-1, -1):
    print(i)

for i in range(m, l, -1):
    print(i)

"""
4
3
2
1
0   <=========== same rule when reverse: never reach to upper bound (2nd location), thus need to have (l -1) since reverse counting here

4
3
2
1
"""

print(float('-inf'))

# # https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/
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