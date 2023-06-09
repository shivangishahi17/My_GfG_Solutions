# User function Template for Python3

class Solution:
    def subsetSum(self, arr, n, sum):
        dp=[[False for _ in range(sum+1)] for x in range(n+1)]
        
        for i in range(n+1):
            dp[i][0]=True
        
        for j in range(sum+1):
            dp[0][i]=False
            
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if arr[i-1]<=j:
                    dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
                elif arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
        return dp[n][sum]
    def equalPartition(self, N, arr):
        # code here
        if sum(arr)%2 != 0:
            return False
        elif sum(arr)%2 == 0:
            return self.subsetSum(arr, N, sum(arr)//2)
        

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends