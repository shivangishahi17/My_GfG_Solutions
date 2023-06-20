#User function Template for python3

class Solution:
    def longestSubsequence(self, N, A):
        # code here
        dp=[1 for i in range(N+1)]
        for i in range(1,N):
            for j in range(i):
                if abs(A[j]-A[i])==1:
                    dp[i]=max(dp[i],dp[j]+1)
        mx=-999
        for i in range(N):
            mx=max(dp[i],mx)
        return mx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for itr in range(N):
            A[itr] = int(A[itr])
        
        ob = Solution()
        print(ob.longestSubsequence(N, A))
# } Driver Code Ends