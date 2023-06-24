# User function Template for Python3

class Solution:
    def solve(self, i, j, n, m, mat, dp):
        if i<0 or i==n:
            return 0
        if j==m:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        else:
            right=mat[i][j]+self.solve(i, j+1, n, m, mat, dp)
            rightUp=mat[i][j]+self.solve(i-1, j+1, n, m, mat, dp)
            rightDown=mat[i][j]+self.solve(i+1, j+1, n, m, mat, dp)
            dp[i][j]=max(right, max(rightUp, rightDown))
            return dp[i][j]
            
    def maxGold(self, n, m, M):
        # code here
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        j=0
        ma=0
        for i in range(n):
            ans=self.solve(i, j, n, m, M, dp)
            ma=max(ma, ans)
        return ma

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends