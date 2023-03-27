"""
https://iq.opengenus.org/max-points-on-a-line/

COMPLEXITY	        NAIVE APPROACH	MAPPING SLOPES APPROACH
Time-Complexity	        n^3	            n^2 * log n
Space Complexity	    1	            n
"""

# >>>>>>>>>>>>>>>>>>>>>>>> NAIVE APPROACH <<<<<<<<<<<<<<<<<<<<<<<

"""
Time-Complexity

Since there are 3 nested loops which run from almost 1 to n, the time complexity is n^3

Worst case time complexity: Θ(n^3)
Average case time complexity: Θ(n^3)
Best case time complexity: Θ(n^3)
Space-Complexity

We do not use any extra space and hence the Space complexity is: Θ(1)

Pseudo Code:

int same_line(int a[],int b[],int c[]){ 
    if (a[0]-c[0])*(b[1]-c[1]) == (a[1]-c[1])*(b[0]-c[0])
        return 1
    else
        return 0
}
int maxPoints(int[][] points) {
    int n = points.size()
    int counter = 0
    for(int i = 0 to i < n){
        for(int j = i+1 to j < n){
            if(points[i][0]==points[j][0] && points[i][1]==points[j][1]) 
                continue
            int sum = 0
            for(int k = 0 to k < n) 
                sum += same_line(points[i],points[j],points[k])
            counter = max(max_pts,sum)
        }
    }
    if(counter==0)
        return n
    else
        return max_pts
}
"""

def same_line(a, b, c):
    print((a[0]-c[0])*(b[1]-c[1]) == (a[1]-c[1])*(b[0]-c[0]))
    print((a[0]-c[0])*(b[1]-c[1]))
    print((a[1]-c[1])*(b[0]-c[0]))
    if ((a[0]-c[0])*(b[1]-c[1]) == (a[1]-c[1])*(b[0]-c[0])):
        return 1
    else:
        return 0

def maxPoints(points):
    n = len(points)
    max_pts = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if(points[i][0]==points[j][0] and points[i][1]==points[j][1]):
                continue
            sum = 0
            for k in range(0, n):
                sum += same_line(points[i],points[j],points[k])
            max_pts = max(max_pts,sum)
    if(max_pts==0):
        return n
    else:
        return max_pts

print(maxPoints([
    [-1, 1],
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 3],
    [3, 4],
]))

# >>>>>>>>>>>>>>>>>>>>>>>> MAPPING SLOPES APPROACH <<<<<<<<<<<<<<<<<<<<<<<
class Point:
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    def maxPoints(self, points):
        n = len(points)
        if (n <= 2):
            return n
        max_points = 0 
        for i in range(0, n):
            pointi = Point(points[i])
            l = {}
            dup = 1 
            for j in range(0, n):
                pointj = Point(points[j])
                if (pointi.x == pointj.x and pointi.y == pointj.y and i!=j): 
                    dup+=1
                elif i!=j :
                    if (pointi.x==pointj.x):
                        l['v'] = l.get('v',0) + 1
                    elif (pointi.y==pointj.y):
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(pointi.y-pointj.y)/(pointi.x-pointj.x)
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                max_points = max(max_points,max(l.values())+dup)
            else: 
                max_points = max(max_points,dup)
        return max_points

"""
Time-Complexity

Since we have 2 nested loops running from 1 to n (number of points) the time-complexity is n^2. In the inner loop we have a gcd function which is executed in logn time.

Therefore, the overall time complexity of this algorithm is:

Worst case time complexity: Θ(n^2 * log n)
Average case time complexity: Θ(n^2 * log n)
Best case time complexity: Θ(n^2 * log n)
Space-Complexity

We use extra 'n' space in the mapping algorithm to store and compare the slopes of n points and hence the overall space complexity is: Θ(n)
"""

points = {3,0}, {4,2}, {2,-2}, {5,5}
sol = Solution()
print(sol.maxPoints(points))

# https://www.geeksforgeeks.org/count-maximum-points-on-same-line/
# python3 program to find maximum number of 2D points that lie on the same line.
 
from collections import defaultdict
from math import gcd
from typing import DefaultDict, List, Tuple
 
IntPair = Tuple[int, int]
 
 
def normalized_slope(a: IntPair, b: IntPair) -> IntPair:
    """
    Returns normalized (rise, run) tuple. We won't return the actual rise/run
    result in order to avoid floating point math, which leads to faulty
    comparisons.
 
    See
    https://en.wikipedia.org/wiki/Floating-point_arithmetic#Accuracy_problems
    """
    run = b[0] - a[0]
 
    # normalize undefined slopes to (1, 0)
    if run == 0:
        return (1, 0)
 
    # normalize to left-to-right
    if run < 0:
        a, b = b, a
        run = b[0] - a[0]
 
    rise = b[1] - a[1]
    # Normalize by greatest common divisor.
    # math.gcd only works on positive numbers.
    gcd_ = gcd(abs(rise), run)
    return (
        rise // gcd_,
        run // gcd_,
    )
 
 
def maximum_points_on_same_line(points: List[List[int]]) -> int:
    # You need at least 3 points to potentially have non-collinear points.
    # For [0, 2] points, all points are on the same line.
    if len(points) < 3:
        return len(points)
 
    # Note that every line we find will have at least 2 points.
    # There will be at least one line because len(points) >= 3.
    # Therefore, it's safe to initialize to 0.
    max_val = 0
 
    for a_index in range(0, len(points) - 1):
        # All lines in this iteration go through point a.
        # Note that lines a-b and a-c cannot be parallel.
        # Therefore, if lines a-b and a-c have the same slope, they're the same
        # line.
        a = tuple(points[a_index])
        # Fresh lines already have a, so default=1
        slope_counts: DefaultDict[IntPair, int] = defaultdict(lambda: 1)
 
        for b_index in range(a_index + 1, len(points)):
            b = tuple(points[b_index])
            slope_counts[normalized_slope(a, b)] += 1
 
        max_val = max(
            max_val,
            max(slope_counts.values()),
        )
 
    return max_val

"""
Time Complexity: O(n2logn), where n denoting length of string.
Auxiliary Space: O(n).
"""

# https://iq.opengenus.org/max-points-on-a-line/
# slope = (y2-y1)/(x2-x1) , where x2 is not equal to x1.
def maxPointsOnLine(arr):   
    max_points= 0    
    for i in range(len(arr)):
        tmpDict = {}
        dupPts = 1   # 1 because need to count the current point itself here
        for j in range(len(arr)):
            if (i != j):
                if (arr[i][0] == arr[j][0]) and (arr[i][1] == arr[j][1]):
                    dupPts += 1
                elif (arr[i][0] == arr[j][0]):
                    tmpDict['h'] = tmpDict.get('h',0) + 1  # https://www.geeksforgeeks.org/python-increment-value-in-dictionary/
                elif (arr[i][1] == arr[j][1]): 
                    tmpDict['v'] = tmpDict.get('v',0) + 1                  
                elif (arr[i][0] != arr[j][0]) and (arr[i][1] != arr[j][1]):      
                    """
                    print('i is: ', i)
                    print('arr[i] is: ', arr[i])
                    print('arr[j] is: ', arr[j])
                    print('first: ', arr[i][1])
                    print('second: ', arr[j][1])
                    print('third: ', arr[i][0])
                    print('forth: ', arr[j][0])
                    """                   
                    tmpDict[(arr[i][1] - arr[j][1])/(arr[i][0] - arr[j][0])] = tmpDict.get((arr[i][1] - arr[j][1])/(arr[i][0] - arr[j][0]), 0) +  1

        print({k:v for k,v in tmpDict.items()})
        if len(tmpDict) > 0:
            max_points = max(max_points, max(tmpDict.values()) + dupPts)
        else:
            max_points = max(max_points, dupPts)
        print('max_points is now: ', max_points)
    return max_points

print(maxPointsOnLine([
    [-1, 1],
    [0, 0],
    [1, 1],
    [38,9],
    [0, 6],
    [2, 2],
    [22, 19],
    [3, 3],
    [3, 4],
    [9, 1],
    [0, 10]
]))

# Try this to enter points on the graph:  https://www.desmos.com/calculator/mhq4hsncnh

"""
# https://www.geeksforgeeks.org/python-increment-value-in-dictionary/
# Python3 code to demonstrate working of
# Increment value in dictionary
# Using get()
 
# Initialize dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'for' : 4, 'CS' : 5}
 
# printing original dictionary
print("The original dictionary : " + str(test_dict))
 
# Using get()
# Increment value in dictionary
test_dict['best'] = test_dict.get('best', 0) + 3
     
# printing result
print("Dictionary after the increment of key : " + str(test_dict))

# Python3 code to demonstrate working of
# Increment value in dictionary
# Using defaultdict()
from collections import defaultdict
 
# Initialize dictionary
test_dict = defaultdict(int)
 
# printing original dictionary
print("The original dictionary : " + str(dict(test_dict)))
 
# Using defaultdict()
# Increment value in dictionary
test_dict['best'] += 3
     
# printing result
print("Dictionary after the increment of key : " + str(dict(test_dict)))
"""