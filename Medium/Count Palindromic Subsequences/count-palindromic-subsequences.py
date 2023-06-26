class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def helper(self, str, dp, i, j):
        if i>j:
            return 0
        
        if i==j:
            return 1
            
        if dp[i][j]!=-1:
            return dp[i][j]
            
        if str[i]==str[j]:
            dp[i][j]=1+self.helper(str, dp, i+1, j)+ self.helper(str, dp, i, j-1)
           
        else:
            dp[i][j]=self.helper(str, dp, i+1, j) + self.helper(str, dp, i, j-1)-self.helper(str, dp, i+1, j-1)
        
        return dp[i][j]
        
    def countPS(self,string):
        # Code here
        n=len(string)
        MOD=10**9+7
        dp=[[-1 for i in range(1000)] for j in range(1000)]
        ans=self.helper(string, dp, 0, n-1)
        return ans%MOD
        
       
        
    



#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends