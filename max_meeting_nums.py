# https://www.geeksforgeeks.org/find-maximum-meetings-in-one-room/
# Python3 program to find maximum number
# of meetings
 
# Custom class for storing starting time,
# finishing time and position of meeting.
 
 
class meeting:
 
    def __init__(self, start, end, pos):
 
        self.start = start
        self.end = end
        self.pos = pos
 
# Function for finding maximum
# meeting in one room
 
 
def maxMeeting(l, N):
 
    # Initialising an arraylist
    # for storing answer
    ans = []
 
    # Sorting of meeting according to
    # their finish time.
    l.sort(key=lambda x: x.end)
 
    # Initially select first meeting
    ans.append(l[0].pos)
 
    # time_limit to check whether new
    # meeting can be conducted or not.
    time_limit = l[0].end
 
    # Check for all meeting whether it
    # can be selected or not.
    for i in range(1, N):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end
 
    # Print final selected meetings
    for i in ans:
        print(i + 1, end=" ")
 
    print()

import bisect
def max_profit(start, end, profit):
    sorted_list = sorted(zip(start, end, profit), key=lambda v: v[1])
    pd = [[0,0]] # [end, profit]
    for s, e, p in sorted_list:
        i = bisect.bisect(pd, [s + 1]) - 1
        if pd[i][1] + p > pd[-1][1]:
            pd.append([e, pd[i][1] + p])
    return pd[-1][1]

def max_profit_with_index(start, end, profit):
    sorted_list = sorted(zip(start, end, profit, [i for i in range(len(start))]), key= lambda v: v[1])
    print(sorted_list)
    pd = [[0,0]]    
    index_list = {}
    index_list[0] = None
    for s, e, p, indexNumber in sorted_list:
        print(i := bisect.bisect(pd, [s + 1]) - 1)
        if pd[i][1] + p > pd[-1][1]:
            pd.append([e, pd[i][1] + p])
            print(pd)
            tmp = []
            if index_list[pd[i][0]] != None:
                tmp = tmp + index_list[pd[i][0]]
            tmp.append(indexNumber)
            index_list[e] = tmp
            print(index_list)
    return pd[-1][1]

# Driver's code
if __name__ == '__main__':
 
    # Starting time
    s = [1, 3, 0, 5, 8, 5]
 
    # Finish time
    f = [2, 4, 6, 7, 9, 9]
 
    # Number of meetings.
    N = len(s)
 
    l = []
 
    for i in range(N): 
        # Creating object of meeting
        # and adding in the list
        l.append(meeting(s[i], f[i], i))
 
    # Function call
    maxMeeting(l, N)
 
    # This code is contributed by MuskanKalra1

    """
    Input: 
    s[] = {1, 3, 0, 5, 8, 5}, 
    f[] = {2, 4, 6, 7, 9, 9} 
    Output: 1 2 4 5
    """
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
        # Number of meetings.
    N = len(s)
 
    l = []
 
    for i in range(N):
        # Creating object of meeting
        # and adding in the list
        l.append(meeting(s[i], f[i], i))
    # Function call
    maxMeeting(l, N)
    # Output : 6 7 1

    # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

    countNum = 1 # first meeting is always counted
    meetNum = [1]
    j = 0
    for i in range(len(s) - 1):
        if s[i + 1] > f [j]:
            meetNum.append(i + 2)
            print('s, f: ', s[i + 1], f[i+1])
            countNum +=1
            j = i + 1
    
    print("Max num of meetings is: ", countNum)
    print("Meeting numbers: ", meetNum)
    # Max num of meetings is:  1
    # Meeting numbers:  [1]

    dictionary = {}
    for i in range(len(s) - 1):
        dictionary.update({s[i]: f[i]})

    print('dictionary is: ', dictionary)

    # sort dictionary by values
    print(sortEndTime1 := {k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])})
    print(sortEndTime2 := dict(sorted(dictionary.items(), key=lambda item: item[1])))
    """
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
    Output: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
    or

    dict(sorted(x.items(), key=lambda item: item[1]))
    Output: {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
    """
    """
    dictionary is:  {75250: 112960, 50074: 114515, 43659: 81825, 8931: 93424, 11273: 54316, 27545: 35533, 50879: 73383}
    {27545: 35533, 11273: 54316, 50879: 73383, 43659: 81825, 8931: 93424, 75250: 112960, 50074: 114515}
    {27545: 35533, 11273: 54316, 50879: 73383, 43659: 81825, 8931: 93424, 75250: 112960, 50074: 114515}
    """
    # https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

    # Sort dictionary by keys:
    myKeys = list(dictionary.keys())
    myKeys.sort()
    sorted_dict = {i: dictionary[i] for i in myKeys}    
    print(sorted_dict)
    # other ways to sort by keys:
    dict1 = dict(sorted(dictionary.items()))
    print(dict1)
    print({k: v for k, v in sorted(dictionary.items(), key=lambda item: item[0])})
    print(dict(sorted(dictionary.items(), key=lambda item: item[0])))

    meetStarts = []
    meetCount = 0
    mStart = mEnd = 0
    for i, (mHead, mTail) in enumerate(sortEndTime2.items()):
        print('i is: ', i)
        print('head is: ', mHead)
        print('tail is: ', mTail)
        if mHead > mEnd:
            print('head is: ', mHead)
            print('tail is: ', mTail)
            meetStarts.append(mHead)
            meetCount += 1
            mEnd = mTail
            print('mEnd is: ', mEnd)

    meetNumbers = [i + 1 for i, (mHead, mTail) in enumerate(dictionary.items()) if mHead in meetStarts]
    print("Max num of meetings is: ", meetCount)
    print("Meeting numbers: ", meetNumbers)
    """
    Max num of meetings is:  3
    Meeting numbers:  [1, 6, 7]
    """

    # I AM THINKING OF A NEW WAY:
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 

    newDict = {}
    for i in range(len(s) - 1):
        newDict.update({i:[s[i], f[i]]})

    newDict = dict(sorted(newDict.items(), key = lambda item: item[1][1]))
    # more methods of sorting dictionary are discussed here: https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/

    tempEnd = 0
    meetCount = 0
    meetNums = []
    for each in newDict.items():
        if each[1][0] > tempEnd:  # if start of meeting 'each' is greater than temp end 
            meetCount += 1
            meetNums.append(each[0] + 1)
            tempEnd = each[1][1]

    print("Max num of meetings is: ", meetCount)
    print("Meeting numbers: ", meetNums)
    """
    Max num of meetings is:  3
    Meeting numbers:  [6, 7, 1]
    """

    """
    i is:  0
    head is:  27545
    tail is:  35533
    head is:  27545
    tail is:  35533
    mEnd is:  35533
    i is:  1
    head is:  11273
    tail is:  54316
    i is:  2
    head is:  50879
    tail is:  73383
    head is:  50879
    tail is:  73383
    mEnd is:  73383
    i is:  3
    head is:  43659
    tail is:  81825
    i is:  4
    head is:  8931
    tail is:  93424
    i is:  5
    head is:  75250
    tail is:  112960
    head is:  75250
    tail is:  112960
    mEnd is:  112960
    i is:  6
    head is:  50074
    tail is:  114515
    Max num of meetings is:  3
    Meeting numbers:  [1, 6, 7]
    Max num of meetings is:  3
    Meeting numbers:  [6, 7, 1]
    """
    # HOW ABOUT HASH TABLE?
    from hashtable_takehomesolution import HashTable

    hash_table = HashTable(50)
    for i in range(len(s) - 1):
        hash_table.set_val(i,[s[i], f[i]])

    # https://www.geeksforgeeks.org/sorting-hashmap-according-key-value-java/
    # in Java, TreeMap is used since it's sorted by key by defaults
    # but in Python we don't have this, thus can't have a sorted hashtable in Python

    """
    Google Software Engineer interview question:  1235. Maximum Profit in Job Scheduling
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
    """
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [2, 3, 7, 1, 8, 0, 4, 9]

    print('3/25/2023 max profit: ', max_profit(s, f, p))
    print('3/25/2023 max profit with index: ', max_profit_with_index(s, f, p))

    p_dict = {}

    for i in range(len(p)):
        p_dict.update({i:[s[i], f[i], p[i]]})

    print(p_dict)
    #{0: [75250, 112960, 2], 1: [50074, 114515, 3], 2: [43659, 81825, 7], 3: [8931, 93424, 1], 4: [11273, 54316, 8], 5: [27545, 35533, 0], 6: [50879, 73383, 4], 7: [77924, 160252, 9]}
    p_dict_sorted = dict(sorted(p_dict.items(), key= lambda item: item[1][2], reverse= True))
    print(p_dict_sorted)
    # {7: [77924, 160252, 9], 4: [11273, 54316, 8], 2: [43659, 81825, 7], 6: [50879, 73383, 4], 1: [50074, 114515, 3], 0: [75250, 112960, 2], 3: [8931, 93424, 1], 5: [27545, 35533, 0]}

    tempEnd = 0
    meetCount = 0
    meetNums = []
    for each in p_dict_sorted.items():
        if each[1][0] > tempEnd:  # if start of meeting 'each' is greater than temp end 
            meetCount += 1
            meetNums.append(each[0] + 1)
            tempEnd = each[1][1]

    print("Max num of meetings is: ", meetCount)
    print("Meeting numbers: ", meetNums)

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/solutions/409009/JavaC++Python-DP-Solution/
import time
import bisect
# from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        print(jobs := sorted(zip(startTime, endTime, profit), key=lambda v: v[1]))  # sorted by end time
        dp = [[0, 0]]
        for s, e, p in jobs:
            print(f's is {s}, e is {e}, p is {p}')
            print(i := bisect.bisect(dp, [s + 1]) - 1)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
                print(dp)
        return dp[-1][1]
    
    def jobScheduling_trying(self, startTime, endTime, profit):
        print(jobs := sorted(zip(startTime, endTime, profit, [i for i in range(len(startTime))]), key=lambda v: v[1]))  # sorted by end time
        dp = [[0, 0]]
        # index_dic = {}
        # index_dic[0] = None
        index_dic = {0: None}
        for s, e, p, indexNum in jobs:
            print(f's is {s}, e is {e}, p is {p}')
            print(i := bisect.bisect_right(dp, [s + 1]) - 1)
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
                print(dp)               # [[0, 0], [35533, 1], [73383, 2], [112960, 3]]
                print(end := dp[i][0])
                tmp = []
                if index_dic[end] != None:
                    tmp = tmp + index_dic[end]
                tmp.append(indexNum)
                index_dic[e] = tmp

        print('Index locations of the jobs: ', index_dic)
        # {0: None, 35533: [5], 73383: [5, 6], 112960: [5, 6, 0]}           <============ with tmp = tmp + index_dic[end]
        # {0: None, 35533: [5, 6, 0], 73383: [5, 6, 0], 112960: [5, 6, 0]}  <============ with tmp = index_dic[end]
        return dp[-1][1]

if __name__ == '__main__':
    s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    # p = [2, 13, -7, 1, 18, 11, 4, -9]
    s = [73383, 50074, 43659, 8931, 11273, 27545, 35533, 77924]
    f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252] 
    p = [1]*len(s)

    sol = Solution()
    # Execution start time
    begin = time.time()
    print('Maximum Profit in Job Scheduling: ', sol.jobScheduling(s, f, p))
    # Execution end time
    end = time.time()
    
    print("Time taken to execute the\
    function is", end-begin)

    print('Maximum Profit in Job Scheduling: ', sol.jobScheduling_trying(s, f, p))

    print(bisect.bisect([2, 2, 2], 2))
    print(bisect.bisect([[0, 0], [35533, 1]], [35533]))
    print(bisect.bisect([[2, 0], [2, 1], [2, 2]], [2]))
    print(bisect.bisect([[2, 0], [2, 1], [2, 2]], [2, -1]))
    print(bisect.bisect([[2, 0], [2, 1], [2, 2]], [2, 0]))
    print(bisect.bisect([[2, 0], [2, 1], [2, 2]], [2, 1]))

    """
    3
    1
    0
    0
    1
    2
    """
    print(bisect.bisect is bisect.bisect_right)
    print(bisect.bisect.__name__)

    """
    True
    bisect_right
    """