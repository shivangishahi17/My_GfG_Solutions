#User function Template for python3

class Solution:
    def solve(self, i, j, n, mat, dp):
        if i>=n:
            return 0
        if j>=n or j<0:
            return 0
        
        if dp[i][j]!=-1:
            return dp[i][j]
            
        down=mat[i][j]+self.solve(i+1, j, n, mat, dp)
        ldown=mat[i][j]+self.solve(i+1, j-1, n, mat, dp)
        rdown=mat[i][j]+self.solve(i+1, j+1, n, mat, dp)
        
        dp[i][j]=max(down, max(ldown, rdown))
        return dp[i][j]
        
    def maximumPath(self, N, Matrix):
        # code here
        dp=[[-1 for i in range(N+1)] for j in range(N+1)]
        i=0
        j=0
        ma=0
        
        for k in range(N):
            ans=self.solve(i, k, N, Matrix, dp)
            ma=max(ma, ans)
        return ma
            

        
     

 

        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        Matrix = [[0]*N for i in range(N)]
        for itr in range(N*N):
            Matrix[(itr//N)][itr%N] = int(arr[itr])
        
        ob = Solution()
        print(ob.maximumPath(N, Matrix))

# } Driver Code Ends