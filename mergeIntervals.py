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

# https://www.tutorialspoint.com/program-to-count-number-of-intervals-that-is-totally-contained-inside-other-intervals-in-python
# count number of intervals that is totally contained inside other intervals
def solve(intervals):
   if not intervals:
      return 0

   intervals.sort(key=lambda x: (x[0], -x[1]))

   end_mx = float("-inf")
   ans = 0

   for start, end in intervals:
      if end <= end_mx:
         ans += 1

      end_mx = max(end_mx, end)

   return ans

intervals = [[2, 6],[3, 4],[4, 7],[5, 5]]
print(solve(intervals))

# https://www.tutorialspoint.com/program-to-count-number-of-intervals-which-are-intersecting-at-given-point-in-python
# count number of intervals which are intersecting at given point
def solve(intervals, point):
   count = 0
   for i, j in intervals:
      if point >= i and point <= j:
         count += 1
   return count

intervals = [[2, 6],[4, 10],[5, 9],[11, 14]]
point = 5
print(solve(intervals, point))

# Input: [[2, 6],[4, 10],[5, 9],[11, 14]], 5
# Output: 3

# https://www.tutorialspoint.com/find-intersecting-intervals-in-python
# Find Intersecting Intervals
class Solution:
   def solve(self, intervals):
      start, end = intervals.pop()
      while intervals:
         start_temp, end_temp = intervals.pop()
         start = max(start, start_temp)
         end = min(end, end_temp)
      return [start, end]
ob = Solution()
intervals = [[10, 110],[20, 60],[25, 75]]
print(ob.solve(intervals))

# Input: [[10, 110],[20, 60],[25, 75]]
# Output: [25, 60]

# https://www.tutorialspoint.com/program-to-find-smallest-intersecting-element-of-each-row-in-a-matrix-in-python
# find the smallest number that exists in every row
class Solution:
   def solve(self, matrix):
      if not matrix:
         return -1
      first = set(matrix[0])
      for row in matrix:
         first &= set(row)
         if not first:
            return -1
      return min(first)
ob1 = Solution()
matrix = [
   [2, 3, 5],
   [5, 10, 10],
   [1, 3, 5]
]
print(ob1.solve(matrix))

# Output: 5

port_mappings = [
"__10.1.1.1|10.2.2.2__",
"portA:member1_port3",
"portB:member2_port27",
"portC:member1_port14",
"__10.3.3.3__",
"portA:port4",
"portB:port15"
"__10.3.3.4__",
"portA:port4",
"portB:port15"
]
print(ob1.solve(port_mappings))


