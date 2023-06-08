#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, mat, i, j, vis):
        if i>=n or j>=m or i<0 or j<0:
            return 
        
        if mat[i][j]==0:
            return 
        
        if vis[i][j]==0:
            vis[i][j]=1
            self.dfs(mat, i+1, j, vis)
            self.dfs(mat, i-1, j, vis)
            self.dfs(mat, i, j+1, vis)
            self.dfs(mat, i, j-1, vis)
            self.dfs(mat, i+1, j+1, vis)
            self.dfs(mat, i+1, j-1, vis)
            self.dfs(mat, i-1, j+1, vis)
            self.dfs(mat, i-1, j-1, vis)
        
    def numIslands(self,grid):
        #code here
        n= len(grid)
        m = len(grid[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and visited[i][j]==0:
                    self.dfs(grid, i, j, visited)
                    count += 1
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