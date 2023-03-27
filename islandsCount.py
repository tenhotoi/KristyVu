class Solution(object):
   def numIslands(self, grid):
      if len(grid) == 0:
         return 0
      n= len(grid)
      print('Grid row number is: ', n)
      m = len(grid[0])
      print('Grid column number is: ', m)
      ans = 0
      for i in range(n):
         for j in range(m):
            if grid[i][j] == "1":
               ans+=1
            self.make_water(i,j,n,m,grid)
      return ans
      
   def make_water(self,i,j,n,m,grid):
      if i<0 or j<0 or i>=n or j>=m:
         return
      if grid[i][j] == "0":
         return
      else:
         grid[i][j] = "0"
      self.make_water(i+1,j,n,m,grid)
      self.make_water(i,j+1,n,m,grid)
      self.make_water(i-1,j,n,m,grid)
      self.make_water(i,j-1,n,m,grid)
      
ob1 = Solution()
print('Number of islands is: ', ob1.numIslands([["1","1","0","0","1"],["1","1","0","1","0"],["1","0","1","0","0"],
["1","0","0","1","1"]]))
