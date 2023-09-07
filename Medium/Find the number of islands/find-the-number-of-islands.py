#User function Template for python3

import sys
from collections import deque
sys.setrecursionlimit(10**8)
class Solution:
    def bfs(self, row, col, vis, grid):
        n=len(grid)
        m=len(grid[0])
        vis[row][col]=1
        queue=deque()
        queue.append((row, col))
        
        while queue:
            row, col=queue.popleft()
            
            for delrow in range(-1,2):
                for delcol in range(-1, 2):
                    nrow=row+delrow
                    ncol=col+delcol
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==1 and not vis[nrow][ncol]:
                        vis[nrow][ncol]=1
                        queue.append([nrow, ncol])
                    
            
        
    def numIslands(self,grid):
        #code here
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)]for j in range(n)]
        count=0
        for row in range(n):
            for col in range(m):
                if not vis[row][col] and grid[row][col]==1:                    
                    count+=1
                    self.bfs(row, col, vis, grid)
        return count


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
        print(obj.numIslands(grid))
# } Driver Code Ends