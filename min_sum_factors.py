# https://www.geeksforgeeks.org/python-program-for-find-minimum-sum-of-factors-of-number/?ref=rp

"""
Given a number, find minimum sum of its factors.
Examples: 
 

Input : 12
Output : 7
Explanation: 
Following are different ways to factorize 12 and
sum of factors in different ways.
12 = 12 * 1 = 12 + 1 = 13
12 = 2 * 6 = 2 + 6 = 8
12 = 3 * 4 = 3 + 4 = 7
12 = 2 * 2 * 3 = 2 + 2 + 3 = 7
Therefore minimum sum is 7

Input : 105
Output : 15
""" 


# Python program to find minimum
# sum of product of number
  
# To find minimum sum of
# product of number
def findMinSum(num):
    sum = 0
     
    # Find factors of number
    # and add to the sum
    i = 2       # 2 is smallest factor, thus would give min sum along the way
    while(i * i <=num):
        while(num % i == 0):
            sum += i
            num //= i
            print('i, num, sum are: {} {} {}'.format(i, num, sum))
        i += 1
    sum += num   # since num i snow < i * i and s the last factor of the original number, so need to include (add) it to the sum
     
    # Return sum of numbers
    # having minimum product
    return sum
 
# Driver Code 
num = 12
print (findMinSum(num))

num = 105
print (findMinSum(num))
 
# This code is contributed by Sachin Bisht

"""
Output: 
7
15

Time Complexity: O(n1/2 * log n)
"""