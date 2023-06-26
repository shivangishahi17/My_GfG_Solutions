#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here 
        mod=10**9+7
        dp=[1]*n
        for i in range(2, n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]%mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends