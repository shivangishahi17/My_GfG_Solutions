#User function Template for python3

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def solve(self, n, k, dp):
        if n==1:
            return k
        if k==0 or k==1:
            return k
        if dp[n][k]!=-1:
            return dp[n][k]
            
        mn=9999 
        temp=0
        for K in range(1, k+1):
            temp=1+ max(self.solve(n-1, K-1, dp),self.solve(n, k-K, dp))
            mn=min(mn, temp)
        dp[n][k]=mn
        return dp[n][k]
        
    def eggDrop(self,n, k):
        # code here
        dp=[[-1 for i in range(k+1)] for j in range(n+1)]
        return self.solve(n, k, dp)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n,k = map(int,input().strip().split())
        ob=Solution()
        print(ob.eggDrop(n,k))
# } Driver Code Ends