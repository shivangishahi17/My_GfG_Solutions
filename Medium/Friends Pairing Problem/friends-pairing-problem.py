#User function Template for python3

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        dp=[0 for i in range(n+1)] 
        
        dp[0]=1
        dp[1]=1
        
        for i in range(2, n+1):
            dp[i]=(dp[i-1]+(i-1)*dp[i-2])%(10**9+7)
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.countFriendsPairings(n))
# } Driver Code Ends