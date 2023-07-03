#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        if K == 0 or N == 0:
            return 0
        
        dp = [[[0 for i in range(2)] for i in range(K+1)] for i in range(N)]
        
        for i in range(N):
            dp[i][0][0] = 0
        
        for j in range(K+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -A[0]
        
        for i in range(1, N):
            for j in range(1, K+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + A[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - A[i])
        return dp[N-1][K][0]
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends