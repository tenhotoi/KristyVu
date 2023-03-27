"""
Google Software Engineer interview question:  1235. Maximum Profit in Job Scheduling
https://walkccc.me/LeetCode/problems/1235/
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i]. 
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that 
there are no two jobs in the subset with overlapping time range. 
If you choose a job that ends at time X you will be able to start another job that starts at time X.

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

https://walkccc.me/LeetCode/problems/1235/
Approach 1: Top-down
Time: O(nlogn)
Space: O(n)
"""
import time

import functools
import bisect

class Solution:
    def jobScheduling_original(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])

        # Will use binary search to find the first available startTime
        for i in range(len(startTime)):
            startTime[i] = jobs[i][0]

        # dp(i) := max profit to schedule jobs[i:]
        @functools.lru_cache(None)
        def dp(i: int) -> int:
            if i == len(startTime):
                return 0
            print('dp cache info is: ', dp.cache_info())
            j = bisect.bisect_left(startTime, jobs[i][1])
            return max(jobs[i][2] + dp(j), dp(i + 1))

        return dp(0)

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        print(startTime_sorted := sorted(startTime))
        # print(jobs := sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)]))
        print(jobs := sorted(zip(startTime, endTime, profit)))

        # Will use binary search to find the first available startTime, which is smallest start time, thus sort from smallest to largest
        # for i in range(len(startTime)):
            # startTime[i] = jobs[i][0]

        print(startTime_sorted)
        index_array = []
        # https://docs.python.org/3/library/functools.html
        """
        https://www.geeksforgeeks.org/python-functools-lru_cache/
        lru_cache()
        lru_cache() is one such function in functools module which helps in reducing 
        the execution time of the function by using memoization technique.
        """
        # dp(i) := max profit to schedule jobs[i:]
        # @functools.lru_cache(None)      # https://realpython.com/lru-cache-python/
        # @functools.lru_cache(maxsize=len(startTime_sorted))      # https://realpython.com/lru-cache-python/
        def dp(i: int) -> int:
            print(f'i is now {i}')
            if i == len(startTime_sorted):         # bisect_left would put very large end time at the end of the array, thus len(starttime) here
                return 0   # <======= the reason i never goes out of the range is because we return every time end value == len()
                     
            print('seems that scripts try to get where end value stands in start array: ', end := jobs[i][1])
            print(startTime_sorted)
            print(f'relatively to start times, end time of {i}, which is {end}, is at location: ', j := bisect.bisect_left(startTime_sorted, jobs[i][1]))
            print(startTime_sorted)
            print('first item in max comparation, which is current profit: ', first := jobs[i][2])
            print('second item in max comparation, which is where end stands in start array: ', second := dp(j))
            print('third item in max comparation, which is next item in start array: ', third := dp(i + 1))
            print('max is: ', max(first + second, third))
            if first + second > third:
                index_array.append(f'left side, max is with {i}')
            else:
                index_array.append(f'right side of {i} is max, max is with {i + 1}')
            print('index_array is: ', index_array)
            # print('dp cache info is: ', dp.cache_info())
            return max(first + second, third)  # comparing all posible cases, starting from 1st, then 2nd,...
        
        print('index_array is: ', index_array)         # this line never get called since scripts go through here only once
        # print('dp cache info is: ', dp.cache_info())   # this line never get called since scripts go through here only once
        return dp(0)

if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 13, -7, 1, 18, 11, 4, -9]

    sol = Solution()
    # Execution start time
    begin = time.time()
    print('Maximum Profit in Job Scheduling without cache: ', sol.jobScheduling(s, f, p))
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the \
    function without cache is", end-begin)

    begin = time.time()
    print('Maximum Profit in Job Scheduling with cache: ', sol.jobScheduling_original(s, f, p))
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the \
    function with cache is", end-begin)

"""
https://walkccc.me/LeetCode/problems/1235/
Approach 2: Bottom-up
Time: O(nlogn)
Space: O(n)
"""

import bisect

class Solution:
    def jobScheduling_original(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # dp[i] := max profit to schedule jobs[i:]
        dp = [0] * (len(startTime) + 1)
        jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])

        # Will use binary search to find the first available startTime
        for i in range(len(startTime)):
            startTime[i] = jobs[i][0]

        for i in reversed(range(len(startTime))):
            j = bisect.bisect_left(startTime, jobs[i][1])
            dp[i] = max(jobs[i][2] + dp[j], dp[i + 1])

        return dp[0]

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # dp[i] := max profit to schedule jobs[i:]
        print(dp := [0] * (len(startTime) + 1))
        # jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])
        print(jobs := sorted(zip(startTime, endTime, profit)))

        # Will use binary search to find the first available startTime
        for i in range(len(startTime)):
            startTime[i] = jobs[i][0]

        for i in reversed(range(len(startTime))):   # the reason for going backward is because endtime is alway greater than starttime, and we need some values to be added, and this can be done by going backward.
            print(f'i is now {i}')
            j = bisect.bisect_left(startTime, jobs[i][1])
            print(f'j is now {j}')
            dp[i] = max(jobs[i][2] + dp[j], dp[i + 1])
            print(dp)

        print(dp)  # max is in the first element of dp list
        return dp[0]
    
if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 13, -7, 1, 18, 11, 4, -9]

    sol = Solution()
    # Execution start time
    begin = time.time()
    print('Maximum Profit in Job Scheduling: ', sol.jobScheduling(s, f, p))
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the\
    function is", end-begin)

"""
https://walkccc.me/LeetCode/problems/1235/
Approach 3: Heap
Time: O(nlogn)
Space: O(n)
"""

import heapq

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        maxProfit = 0
        # print(jobs := sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)]))
        print(jobs := sorted(zip(startTime, endTime, profit)))
        minHeap = []  # (endTime, profit)

        # Will use binary search to find the first available startTime
        # for i in range(len(startTime)):
            # startTime[i] = jobs[i][0]

        for s, e, p in jobs:   # already sorted to have s going from lowest to highest here, meaning earliest starting time
            print(f's is {s}, e is {e}, p is {p}, and minHeap outside while loop is {minHeap}')
            while minHeap and s >= minHeap[0][0]:
                print(f'minHeap is {minHeap}')
                maxProfit = max(maxProfit, heapq.heappop(minHeap)[1])  # considering max, not sum, because these jobs are overlapping time range
                print(f'maxProfit is {maxProfit}')
            heapq.heappush(minHeap, (e, p + maxProfit))
        print(f's is {s}, e is {e}, p is {p}, and minHeap at the end of for loop is {minHeap}')

        return max(maxProfit, max(p for _, p in minHeap))

if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 13, -7, 1, 18, 11, 4, -9]

    sol = Solution()
    # Execution start time
    begin = time.time()
    print('Maximum Profit in Job Scheduling: ', sol.jobScheduling(s, f, p))
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the\
    function is", end-begin)

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/409009/JavaC++Python-DP-Solution/
class Solution:
    def jobScheduling_original(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
    
    def jobScheduling(self, startTime, endTime, profit):
        print(jobs := sorted(zip(startTime, endTime, profit, [index for index in range(len(startTime))]), key=lambda v: v[1]))  # sorted by end time
        dp = [[0, 0]]
        index_dic = {}
        index_dic[0] = None
        for s, e, p, index in jobs:
            print(f's is {s}, e is {e}, p is {p}')
            print(i := bisect.bisect(dp, [s + 1]) - 1)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
                print(dp)       # [[0, 0], [35533, 11], [54316, 18], [112960, 20], [114515, 24]]
                tmp = []
                if index_dic[dp[i][0]] != None:
                    tmp = tmp + index_dic[dp[i][0]]
                tmp.append(index)
                index_dic[e] = tmp
                print(index_dic[e])
        print(index_dic)
        # {0: None, 35533: [5], 54316: [4], 112960: [4, 0], 114515: [5, 1]}         <============ with tmp = tmp + index_dic[dp[i][0]]
        # {0: None, 35533: [5, 1], 54316: [4, 0], 112960: [4, 0], 114515: [5, 1]}   <============ with tmp = index_dic[dp[i][0]]
        return dp[-1][1]
    
if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 13, -7, 1, 18, 11, 4, -9]

    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 3, 7, 1, 8, 0, 4, 9]
    
    sol = Solution()
    # Execution start time
    begin = time.time()
    print('Maximum Profit in Job Scheduling with index: ', sol.jobScheduling(s, f, p))  # Maximum Profit in Job Scheduling:  24
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the\
    function is", end-begin)


"""
https://www.geeksforgeeks.org/weighted-job-scheduling/
Given N jobs where every job is represented by following three elements of it.

Start Time
Finish Time
Profit or Value Associated (>= 0)
Find the maximum profit subset of jobs such that no two jobs in the subset overlap. 

Example: 

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.

The above problem can be solved using the following recursive solution.  

1) First sort jobs according to finish time.
2) Now apply following recursive process. 
   // Here arr[] is array of n jobs
   findMaximumProfit(arr[], n)
   {
     a) if (n == 1) return arr[0];
     b) Return the maximum of following two profits.
         (i) Maximum profit by excluding current job, i.e., 
             findMaximumProfit(arr, n-1)
         (ii) Maximum profit by including the current job            
   }

How to find the profit including current job?
The idea is to find the latest job before the current job (in 
sorted array) that doesn't conflict with current job 'arr[n-1]'. 
Once we find such a job, we recur for all jobs till that job and
add profit of current job to result.
In the above example, "job 1" is the latest non-conflicting
for "job 4" and "job 2" is the latest non-conflicting for "job 3".
"""

# Python3 program for weighted job scheduling using
# Naive Recursive Method
 
# Importing the following module to sort array
# based on our custom comparison function
from functools import cmp_to_key
 
# A job has start time, finish time and profit
class Job:
     
    def __init__(self, start, finish, profit):
         
        self.start = start
        self.finish = finish
        self.profit = profit
 
# A utility function that is used for
# sorting events according to finish time
def jobComparator(s1, s2):
     
    return s1.finish < s2.finish
 
# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1
def latestNonConflict(arr, i):
     
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
             
    return -1
 
# A recursive function that returns the
# maximum possible profit from given
# array of jobs. The array of jobs must
# be sorted according to finish time
def findMaxProfitRec(arr, n):
     
    # Base case
    if n == 1:
        return arr[n - 1].profit
 
    # Find profit when current job is included
    inclProf = arr[n - 1].profit
    i = latestNonConflict(arr, n)
     
    if i != -1:
        inclProf += findMaxProfitRec(arr, i + 1)
 
    # Find profit when current job is excluded
    exclProf = findMaxProfitRec(arr, n - 1)
    return max(inclProf, exclProf)
 
# The main function that returns the maximum
# possible profit from given array of jobs
def findMaxProfit(arr, n):
     
    # Sort jobs according to finish time
    arr = sorted(arr, key = cmp_to_key(jobComparator))
    return findMaxProfitRec(arr, n)
 
# Driver code
values = [ (3, 10, 20), (1, 2, 50),
           (6, 19, 100), (2, 100, 200) ]
arr = []
for i in values:
    arr.append(Job(i[0], i[1], i[2]))
     
n = len(arr)
 
# Execution start time
begin = time.time()
print("The optimal profit is", findMaxProfit(arr, n))
# Execution end time
end = time.time()
  
print("Time taken to execute the\
function is", end-begin) 
# This code is code contributed by Kevin Joshi

"""
The above solution may contain many overlapping subproblems. For example, if lastNonConflicting() always returns the previous job, then findMaxProfitRec(arr, n-1) is called twice and the time complexity becomes O(n*2n). As another example when lastNonConflicting() returns previous to the previous job, there are two recursive calls, for n-2 and n-1. In this example case, recursion becomes the same as Fibonacci Numbers. 
"""
# Python3 program for weighted job scheduling
# using Dynamic Programming
 
# Importing the following module to sort array
# based on our custom comparison function
from functools import cmp_to_key
 
# A job has start time, finish time and profit
 
 
class Job:
 
    def __init__(self, start, finish, profit):
 
        self.start = start
        self.finish = finish
        self.profit = profit
 
# A utility function that is used for sorting
# events according to finish time
 
 
def jobComparator(s1, s2):
 
    return s1.finish < s2.finish
 
# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1
 
 
def latestNonConflict(arr, i):
 
    for j in range(i - 1, -1, -1):
        if arr[j].finish <= arr[i - 1].start:
            return j
 
    return -1
 
# The main function that returns the maximum possible
# profit from given array of jobs
 
 
def findMaxProfit(arr, n):
 
    # Sort jobs according to finish time
    arr = sorted(arr, key=cmp_to_key(jobComparator))
 
    # Create an array to store solutions of subproblems.
    # table[i] stores the profit for jobs till arr[i]
    # (including arr[i])
    table = [None] * n
    table[0] = arr[0].profit
 
    # Fill entries in M[] using recursive property
    for i in range(1, n):
 
        # Find profit including the current job
        inclProf = arr[i].profit
        l = latestNonConflict(arr, i)
 
        if l != -1:
            inclProf += table[l]
 
        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])
 
    # Store result and free dynamic memory
    # allocated for table[]
    result = table[n - 1]
 
    return result
 
 
# Driver code
values = [(3, 10, 20), (1, 2, 50),
          (6, 19, 100), (2, 100, 200)]
arr = []
for i in values:
    arr.append(Job(i[0], i[1], i[2]))
 
n = len(arr)
 
# Execution start time
begin = time.time()
print("The optimal profit is", findMaxProfit(arr, n))
# Execution end time
end = time.time()
  
print("Time taken to execute the\
function is", end-begin) 
# This code is contributed by Kevin Joshi

"""
Output: 

The optimal profit is 250
Time Complexity of the above Dynamic Programming Solution is O(n2). Note that the above solution can be optimized to O(nLogn) using Binary Search in latestNonConflict() instead of linear search. Thanks to Garvit for suggesting this optimization. Please refer below post for details.
"""

# Python program for weighted job scheduling using Dynamic
# Programming and Binary Search
 
# Class to represent a job
class Job:
    def __init__(self, start, finish, profit):
        self.start  = start
        self.finish = finish
        self.profit  = profit
 
 
# A Binary Search based function to find the latest job
# (before current job) that doesn't conflict with current
# job.  "index" is index of the current job.  This function
# returns -1 if all jobs before index conflict with it.
# The array jobs[] is sorted in increasing order of finish
# time.
def binarySearch(job, start_index):
 
    # Initialize 'lo' and 'hi' for Binary Search
    lo = 0
    hi = start_index - 1
 
    # Perform binary Search iteratively
    while lo <= hi:
        mid = (lo + hi) // 2
        if job[mid].finish <= job[start_index].start:
            if job[mid + 1].finish <= job[start_index].start:
                lo = mid + 1
            else:
                return mid
        else:
            hi = mid - 1
    return -1
 
# The main function that returns the maximum possible
# profit from given array of jobs
def schedule(job):
   
    # Sort jobs according to finish time
    job = sorted(job, key = lambda j: j.finish)
 
    # Create an array to store solutions of subproblems.  table[i]
    # stores the profit for jobs till arr[i] (including arr[i])
    n = len(job)
    table = [0 for _ in range(n)]
 
    table[0] = job[0].profit;
 
    # Fill entries in table[] using recursive property
    for i in range(1, n):
 
        # Find profit including the current job
        inclProf = job[i].profit
        l = binarySearch(job, i)
        if (l != -1):
            inclProf += table[l];
 
        # Store maximum of including and excluding
        table[i] = max(inclProf, table[i - 1])
 
    return table[n-1]
 
# Execution start time
begin = time.time()
# Driver code to test above function
job = [Job(1, 2, 50), Job(3, 5, 20),
      Job(6, 19, 100), Job(2, 100, 200)]
# Execution end time
end = time.time()
  
print("Time taken to execute the\
function is", end-begin)
print("Optimal profit is"),
print(schedule(job))

"""
Output:

Optimal profit is 250
Time complexity: O(n Log n)

Auxiliary Space: O(n) because using extra space for array table

"""
import urllib
import urllib.request as request
import functools

@functools.lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

@functools.lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = r'https://peps.python.org/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

print(get_pep.cache_info())
# CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)

"""
# https://www.geeksforgeeks.org/python-program-for-stock-buy-sell-to-maximize-profit/

Python Program For Stock Buy Sell To Maximize Profit

Naive approach: A simple approach is to try buying the stocks and selling them on every single day 
when profitable and keep updating the maximum profit so far.

Below is the implementation of the above approach:
"""

# Python3 implementation of the approach
 
# Function to return the maximum profit
# that can be made after buying and
# selling the given stocks
def maxProfit(price, start, end):
 
    # If the stocks can't be bought
    if (end <= start):
        return 0
 
    # Initialise the profit
    profit = 0
 
    # The day at which the stock
    # must be bought
    for i in range(start, end, 1):
 
        # The day at which the
        # stock must be sold
        for j in range(i+1, end+1):
 
            # If buying the stock at ith day and
            # selling it at jth day is profitable
            if (price[j] > price[i]):
                 
                # Update the current profit
                curr_profit = price[j] - price[i] + maxProfit(price, start, i - 1)+ maxProfit(price,  j + 1, end)
 
                # Update the maximum profit so far
                profit = max(profit, curr_profit)
 
    return profit
 
# Driver code
if __name__ == '__main__':
    price = [100, 180, 260,
             310, 40, 535, 695]
    n = len(price)
    print(maxProfit(price, 0, n - 1))
# This code is contributed by Rajput-Ji

"""
865
Time Complexity: O(N2)
Auxiliary Space: O(1)

Efficient approach: If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. 
Following is the algorithm for this problem.  

Find the local minima and store it as starting index. If not exists, return.
Find the local maxima. and store it as an ending index. If we reach the end, set the end as the ending index.
Update the solution (Increment count of buy-sell pairs)
Repeat the above steps if the end is not reached.
"""

# Python3 Program to find
# best buying and selling days
 
# This function finds the buy sell
# schedule for maximum profit
def stockBuySell(price, n):
     
    # Prices must be given for at
    # least two days
    if (n == 1):
        return
     
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
         
        # Find Local Minima
        # Note that the limit is (n-2) as
        # we are comparing present element
        # to the next element
        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1
         
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
         
        # Store the index of minima
        buy = i
        i += 1
         
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and
               (price[i] >= price[i - 1])):
            i += 1
             
        # Store the index of maxima
        sell = i - 1

        print("Buy on day: ",buy,"    ",
                "Sell on day: ",sell)
def stockBuySell_kristy(price, n):
     
    # Prices must be given for at
    # least two days
    if (n == 1):
        return
     
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):
         
        # Find Local Minima
        # Note that the limit is (n-2) as
        # we are comparing present element
        # to the next element
        while ((i < (n - 1)) and
                (price[i + 1] <= price[i])):
            i += 1
         
        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break
         
        # Store the index of minima
        buy = i
        i += 1
         
        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        """while ((i < n) and
               (price[i] >= price[i - 1])):
            i += 1
             
        # Store the index of maxima
        sell = i - 1
        """
        while ((i < n - 1) and price[i + 1] >= price[i]): 
            i += 1
        sell = i
        print("Buy on day: ",buy,"    ",
                "Sell on day: ",sell)
                
# Driver code
 
# Stock prices on consecutive days
price = [100, 180, 260,
         310, 40, 535, 695]
n = len(price)

# Function call
stockBuySell(price, n)
# This is code contributed by SHUBHAMSINGH10

"""
Buy on day:  0      Sell on day:  3
Buy on day:  4      Sell on day:  6
Time Complexity: The outer loop runs till I become n-1. The inner two loops increment value of I in every iteration. 
So overall time complexity is O(n)
Auxiliary Space : O(1) since using constant variables

Valley Peak Approach:

In this approach, we just need to find the next greater element and subtract it from the current element so that 
the difference keeps increasing until we reach a minimum. If the sequence is a decreasing sequence so the maximum profit possible is 0.


# Python3 program for the
"""
# Python3 program for the
# above approach
def max_profit(prices: list,
               days: int) -> int:
    profit = 0
 
    for i in range(1, days):
 
        # Checks if elements are adjacent
        # and in increasing order
        if prices[i] > prices[i-1]:
 
            # Difference added to 'profit'
            profit += prices[i] - prices[i-1]
 
    return profit

def max_loss(prices: list,
               days: int) -> int:
    loss = 0
 
    for i in range(1, days):
 
        # Checks if elements are adjacent
        # and in increasing order
        if prices[i] < prices[i-1]:
 
            # Difference added to 'profit'
            loss += prices[i] - prices[i-1]
 
    return loss
 
# Driver Code
if __name__ == '__main__':
 
    # Stock prices on consecutive days
    prices = [100, 180, 260,
              310, 40, 535, 695]
 
    # Function call
    profit = max_profit(prices, len(prices))
    print(profit)

    loss = max_profit(prices, len(prices))
    print(loss)

# This code is contributed by vishvofficial.

"""
Output
865
Time Complexity: O(n)
Auxiliary Space: O(1)
"""

"""
https://docs.python.org/3/library/urllib.html
urllib is a package that collects several modules for working with URLs:

urllib.request for opening and reading URLs
urllib.error containing the exceptions raised by urllib.request
urllib.parse for parsing URLs
urllib.robotparser for parsing robots.txt files

https://realpython.com/lru-cache-python/

"""

"""
import requests

cache = dict()

def get_article_from_server(url):
    print("Fetching article from server...")
    response = requests.get(url)
    return response.text

def get_article(url):
    print("Getting article...")
    if url not in cache:
        cache[url] = get_article_from_server(url)

    return cache[url]

get_article("https://realpython.com/sorting-algorithms-python/")
get_article("https://realpython.com/sorting-algorithms-python/")
"""

"""
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
[(8931, 93424, 1, 3), (11273, 54316, 8, 4), (27545, 35533, 0, 5), (43659, 81825, 7, 2), (50074, 114515, 3, 1), (50879, 73383, 4, 6), (75250, 112960, 2, 0), (77924, 160252, 9, 7)]
[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
index_array is:  []
dp cache info is:  CacheInfo(hits=0, misses=0, maxsize=8, currsize=0)
i is now 0
seems that scripts try to get where end value stands in start array:  93424
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 0 is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  1
i is now 8
second item in max comparation, which is where end stands in start array:  0
i is now 1
seems that scripts try to get where end value stands in start array:  54316
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 1 is at location:  6
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  8
i is now 6
seems that scripts try to get where end value stands in start array:  112960
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 6 is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  2
second item in max comparation, which is where end stands in start array:  0
i is now 7
seems that scripts try to get where end value stands in start array:  160252
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 7 is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  9
second item in max comparation, which is where end stands in start array:  0
third item in max comparation, which is next item in start array:  0
max is:  9
index_array is:  ['left side, max is with 7']
dp cache info is:  CacheInfo(hits=3, misses=5, maxsize=8, currsize=1)
third item in max comparation, which is next item in start array:  9
max is:  9
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7']
dp cache info is:  CacheInfo(hits=3, misses=5, maxsize=8, currsize=2)
second item in max comparation, which is where end stands in start array:  9
i is now 2
seems that scripts try to get where end value stands in start array:  35533
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 2 is at location:  3
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  0
i is now 3
seems that scripts try to get where end value stands in start array:  81825
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 3 is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  7
second item in max comparation, which is where end stands in start array:  0
i is now 4
seems that scripts try to get where end value stands in start array:  114515
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 4 is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  3
second item in max comparation, which is where end stands in start array:  0
i is now 5
seems that scripts try to get where end value stands in start array:  73383
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 5 is at location:  6
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  4
second item in max comparation, which is where end stands in start array:  9
third item in max comparation, which is next item in start array:  9
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=3)
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=4)
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=5)
second item in max comparation, which is where end stands in start array:  13
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=6)
third item in max comparation, which is next item in start array:  13
max is:  17
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=7)
third item in max comparation, which is next item in start array:  17
max is:  17
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1', 'right side of 0 is max, max is with 1']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=8)
Maximum Profit in Job Scheduling:  (17, ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1', 'right side of 0 is max, max is with 1'])
Time taken to execute the     function is 0.007997989654541016
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
The optimal profit is 250
Time taken to execute thefunction is 0.0
The optimal profit is 250
Time taken to execute thefunction is 0.0
Time taken to execute thefunction is 0.0
Optimal profit is
250
8 118571
290 53187
308 41428
320 21688
8 118571
218 20740
320 21688
279 20205
289 30487
320 21688
9991 9
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
865
Buy on day:  0      Sell on day:  3
Buy on day:  4      Sell on day:  6
865


[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
[(8931, 93424, 1, 3), (11273, 54316, 8, 4), (27545, 35533, 0, 5), (43659, 81825, 7, 2), (50074, 114515, 3, 1), (50879, 73383, 4, 6), (75250, 112960, 2, 0), (77924, 160252, 9, 7)]
[75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
index_array is:  []
dp cache info is:  CacheInfo(hits=0, misses=0, maxsize=8, currsize=0)
i is now 0
seems that scripts try to get where end value stands in start array:  93424
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 0, which is 93424, is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  1
i is now 8
second item in max comparation, which is where end stands in start array:  0
i is now 1
seems that scripts try to get where end value stands in start array:  54316
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 1, which is 54316, is at location:  6
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  8
i is now 6
seems that scripts try to get where end value stands in start array:  112960
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 6, which is 112960, is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  2
second item in max comparation, which is where end stands in start array:  0
i is now 7
seems that scripts try to get where end value stands in start array:  160252
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 7, which is 160252, is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  9
second item in max comparation, which is where end stands in start array:  0
third item in max comparation, which is next item in start array:  0
max is:  9
index_array is:  ['left side, max is with 7']
dp cache info is:  CacheInfo(hits=3, misses=5, maxsize=8, currsize=1)
third item in max comparation, which is next item in start array:  9
max is:  9
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7']
dp cache info is:  CacheInfo(hits=3, misses=5, maxsize=8, currsize=2)
second item in max comparation, which is where end stands in start array:  9
i is now 2
seems that scripts try to get where end value stands in start array:  35533
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 2, which is 35533, is at location:  3
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  0
i is now 3
seems that scripts try to get where end value stands in start array:  81825
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 3, which is 81825, is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  7
second item in max comparation, which is where end stands in start array:  0
i is now 4
seems that scripts try to get where end value stands in start array:  114515
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 4, which is 114515, is at location:  8
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  3
second item in max comparation, which is where end stands in start array:  0
i is now 5
seems that scripts try to get where end value stands in start array:  73383
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
relatively to start times, end time of 5, which is 73383, is at location:  6
[8931, 11273, 27545, 43659, 50074, 50879, 75250, 77924]
first item in max comparation, which is current profit:  4
second item in max comparation, which is where end stands in start array:  9
third item in max comparation, which is next item in start array:  9
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=3)
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=4)
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4']
dp cache info is:  CacheInfo(hits=7, misses=9, maxsize=8, currsize=5)
second item in max comparation, which is where end stands in start array:  13
third item in max comparation, which is next item in start array:  13
max is:  13
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=6)
third item in max comparation, which is next item in start array:  13
max is:  17
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=7)
third item in max comparation, which is next item in start array:  17
max is:  17
index_array is:  ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1', 'right side of 0 is max, max is with 1']
dp cache info is:  CacheInfo(hits=8, misses=9, maxsize=8, currsize=8)
Maximum Profit in Job Scheduling:  (17, ['left side, max is with 7', 'right side of 6 is max, max is with 7', 'left side, max is with 5', 'right side of 4 is max, max is with 5', 'right side of 3 is max, max is with 4', 'right side of 2 is max, max is with 3', 'left side, max is with 1', 'right side of 0 is max, max is with 1'])
Time taken to execute the     function is 0.008012533187866211
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
Maximum Profit in Job Scheduling:  17
Time taken to execute the    function is 0.0
The optimal profit is 250
Time taken to execute thefunction is 0.0
The optimal profit is 250
Time taken to execute thefunction is 0.0009984970092773438
Time taken to execute thefunction is 0.0
Optimal profit is
250
8 118571
290 53187
308 41428
320 21688
8 118571
218 20740
320 21688
279 20205
289 30487
320 21688
9991 9
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
865
Buy on day:  0      Sell on day:  3
Buy on day:  4      Sell on day:  6
865
"""
values = [ (3, 10, 20), (1, 2, 50),
           (6, 19, 100), (2, 100, 200) ]

v_sorted = sorted(values, key=lambda v: v[1])
pd = [[0,0]]  # [end, profit]
for s, e, p in values:
    i = bisect.bisect(pd, [s + 1]) - 1
    if pd[i][1] + p > pd[-1][1]:
        pd.append([e, pd[i][1] + p])

print('Max profit: ', pd[-1][1])
# Max profit:  250

def max_profit_with_index(start, end, profit):
    sorted_list = sorted(zip(start, end, profit, [i for i in range(len(start))]), key= lambda v: v[1])
    pd = [[0,0]]    
    index_list = {0: None}
    for s, e, p, indexNumber in sorted_list:
        j = bisect.bisect(pd, [s + 1]) - 1
        if pd[j][1] + p > pd[-1][1]:
            pd.append([e, pd[j][1] + p])
            print(pd)
            tmp = []
            if index_list[pd[j][0]] != None:
                tmp = tmp + index_list[pd[j][0]]
            tmp.append(indexNumber)
            index_list[e] = tmp
            print(index_list)
    return pd[-1][1]

if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 3, 7, 1, 8, 0, 4, 9]

    print('3/25/2023 max profit with index: ', max_profit_with_index(s, f, p))

    price = [100, 180, 260,
            310, 310, 40, 40, 535, 695]
    stockBuySell(price, len(price))
    stockBuySell_kristy(price, len(price))

"""
[[0, 0], [54316, 8]]
{0: None, 54316: [4]}
[[0, 0], [54316, 8], [112960, 10]]
{0: None, 54316: [4], 112960: [4, 0]}
[[0, 0], [54316, 8], [112960, 10], [160252, 17]]
{0: None, 54316: [4], 112960: [4, 0], 160252: [4, 7]}
3/25/2023 max profit with index:  17
Buy on day:  0      Sell on day:  4
Buy on day:  6      Sell on day:  8
Buy on day:  0      Sell on day:  4
Buy on day:  6      Sell on day:  8
"""