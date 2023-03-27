# https://www.geeksforgeeks.org/python-find-all-triplets-in-a-list-with-given-sum/

"""
Given a list of integers, write a Python program to find all triplets that sum up to given integer ‘k’. 
Examples:

Input : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 10
Output : [(1, 5, 4), (1, 6, 3), (1, 7, 2), (2, 5, 3)]

Input : [12, 3, 6, 1, 6, 9], k = 24
Output : [(12, 6, 6), (12, 9, 3)]
Approach #1 : Naive (Using set) In this approach, we use two for loops. The first loop sets first element, another to check whether other two elements including first sums up to k or not. This approach takes O(n2) time complexity. 
"""

# Python3 program to Find total number
# of triplets in a temp_list with given k
 
def findTriplets(lst, k):
    triplet_count = 0
    final_temp_list =[]
     
    for i in range(0, len(lst)-1):
         
        s = set()
        temp_list = []
 
        # Adding first element
        temp_list.append(lst[i])
 
        curr_k = k - lst[i]
         
        for j in range(i + 1, len(lst)):
             
            if (curr_k - lst[j]) in s:
                triplet_count += 1
                 
                # Adding second element
                temp_list.append(lst[j])
 
                # Adding third element
                temp_list.append(curr_k - lst[j])
                 
                # Appending tuple to the final list
                final_temp_list.append(tuple(temp_list))
                temp_list.pop(2)
                temp_list.pop(1)
            s.add(lst[j])
             
    return final_temp_list
     
# Driver Code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 10
print(findTriplets(lst, k))

"""
Output:
[(1, 5, 4), (1, 6, 3), (1, 7, 2), (2, 5, 3)]
  Approach #2 : Using itertools Python itertools module provide combination(iterable, r) function. This tool returns the r length subsequences of elements from the input iterable. Every time we make a combination of 3 elements and check if they sums up to k or not. 
"""

# Python3 program to Find total number
# of  triplets in a list with given sum
from itertools import combinations
 
def findTriplets(lst, key):
     
    def valid(val):
        return sum(val) == key
         
    return list(filter(valid, list(combinations(lst, 3))))
 
# Driver Code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findTriplets(lst, 10))

"""
Output:
[(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
Approach#3: using while loop
This approach implements the classic algorithm for finding all triplets in an input list that sum up to a given value k. It first sorts the input list in ascending order, and then iterates through all possible triplets using three nested loops. For each triplet, it checks if the sum equals k and if so, appends the triplet to a results list. Finally, it returns the results list.

Algorithm
1. Sort the input list in non-decreasing order.
2. Initialize an empty result list.
3. Iterate through the input list from the first element to the second-to-last element.
4. For each element, initialize two pointers left and right, one pointing to the element next to it and the other pointing to the last element of the list.
5. While left is less than right:
a. If the sum of the current element, the element at index left, and the element at index right is equal to k, append a tuple of these three elements to the result list.
b. If the sum is less than k, increment left.
c. If the sum is greater than k, decrement right.
6. Return the result list.
""" 


def find_triplets(input_list, k):
    input_list.sort()
    result = []
    for i in range(len(input_list) - 2):
        left = i + 1
        right = len(input_list) - 1
        while left < right:
            if input_list[i] + input_list[left] + input_list[right] == k:
                result.append((input_list[i], input_list[left], input_list[right]))
                left += 1
                right -= 1
            elif input_list[i] + input_list[left] + input_list[right] < k:
                left += 1
            else:
                right -= 1
    return result
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 10
print(find_triplets(input_list, k))


"""
Output
[(1, 2, 7), (1, 3, 6), (1, 4, 5), (2, 3, 5)]
Time complexity: O(n^2), where n is the length of the input list. This is because the outer loop iterates through all possible triplets, and the inner loop performs a constant amount of work for each iteration of the outer loop.

Auxiliary Space: O(1), because the code only uses a constant amount of additional memory to store the left and right indices and the results list.
"""


# https://www.tutorialspoint.com/find-all-triplets-in-a-list-with-given-sum-in-python
def SumTriplets(listA, sum):
   trpltcnt = 0
   res = []

   for i in range(0, len(listA) - 1):

      s = set()
      tmp = []

      # Adding first element
      tmp.append(listA[i])

      current_sum = sum - listA[i]

      for j in range(i + 1, len(listA)):

         if (current_sum - listA[j]) in s:
            trpltcnt += 1

            # Adding second element
            tmp.append(listA[j])

            # Adding third element
            tmp.append(current_sum - listA[j])

            # Appending tuple to the final list
            res.append(tuple(tmp))
            tmp.pop(2)
            tmp.pop(1)
         s.add(listA[j])

   return res


listA = [11,12,13,14,15,16,17,18,19,20]
print("Required triplets:\n",SumTriplets(listA, 40))

"""
Output
Running the above code gives us the following result −

Required triplets:
[(11, 15, 14), (11, 16, 13), (11, 17, 12), (12, 15, 13)]
Example
 Live Demo
"""

from itertools import combinations

listA = [11,12,13,14,15,16,17,18,19,20]

def fsum(val):
      return sum(val) == 40

res = list(filter(fsum,list(combinations(listA, 3))))
print("Required triplets:\n",res)

"""
Output
Running the above code gives us the following result −

Required triplets:
[(11, 12, 17), (11, 13, 16), (11, 14, 15), (12, 13, 15)]
"""

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


# https://github.com/geekcomputers/Python/blob/master/Triplets%20with%20zero%20sum/find_Triplets_with_zero_sum.py
def triplet_sum(test_list, val):
    print(test_list)
    print(l_sorted := [int(x) for x in sorted(test_list)])
    sol = []
    for i in range(len(l_sorted) - 2):
        left = i + 1
        right = len(l_sorted) - 1
        while left < right:
            print(f'left, right at beginning of while loop is {left}, {right}')
            sum = l_sorted[i] + l_sorted[left] + l_sorted[right]
            if sum == val:
                sol.append((l_sorted[i], l_sorted[left], l_sorted[right]))
                left += 1
                right -= 1
            elif sum < val:
                left += 1
            else:
                right -= 1
            print(f'left, right at the end of while loop is {left}, {right}')

    return sol

input = [ '4', '6', '7', '2', '1']
value = 12
print(triplet_sum(input,value))


"""
right is 4
right is 4
right is 4
right is 3
right is 4
[(1, 4, 7), (2, 4, 6)]
"""
listA = [11,12,13,14,15,16,17,18,19,20]
print(triplet_sum(listA, 40))