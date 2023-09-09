#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, row, col, grid, vis, lis, row0, col0):
        vis[row][col]=1
        lis.append((row-row0, col-col0))
        delrow=[-1, 0, +1, 0]
        delcol=[0, -1, 0, +1]
        for i in range(4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and grid[nrow][ncol]==1:
                self.dfs(nrow, ncol, grid, vis, lis, row0, col0)
                
            
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n=len(grid)
        m=len(grid[0])
        
        vis=[[0 for i in range(m)]for j in range(n)]
        list=[]
        ans=set()
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col]==1:
                    lis=[]
                    self.dfs(row, col, grid, vis, lis, row, col)
                    ans.add(tuple(lis))
                    
        return len(ans)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends