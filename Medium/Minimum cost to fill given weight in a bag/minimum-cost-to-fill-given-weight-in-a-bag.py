#User function Template for python3
import sys
class Solution:
    def minimumCost(self, cost, n, W):
        # code here
        dp=[[0 for i in range(W+1)] for j in range(n+1)]
	
	    for i in range(n+1):
	        dp[i][0]=0
	    for i in range(W+1):
	        dp[0][i]=sys.maxsize
	        
	    for i in range(1,n+1):
	        for j in range(1,W+1):
	            if(cost[i-1] != -1 and j>=i):
	                dp[i][j]=min(dp[i-1][j],dp[i][j-i]+cost[i-1])
	            else:
	                dp[i][j]=dp[i-1][j]
	    if(dp[n][W]==sys.maxsize):
	        return -1
	    return dp[n][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,w = input().split()
		n,w = int(n),int(w)
		a = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minimumCost(a,n,w)
		print(ans)

# } Driver Code Ends