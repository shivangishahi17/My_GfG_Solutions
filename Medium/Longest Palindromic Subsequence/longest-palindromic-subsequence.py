#User function Template for python3

class Solution:
    def lcs(self, s1, s2):
        n=len(s1)
        m=len(s2)
        
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        return dp[n][m]

    def longestPalinSubseq(self, S):
        # code here
        S1=S[::-1]
        return self.lcs(S, S1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends