#User function Template for python3

class Solution:
    def lcs(self, s1, s2):
        n=len(s1)
        m=len(s2)
        
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if i!=j and s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
        return dp[i][j]

	def LongestRepeatingSubsequence(self, str):
		# Code here
		return self.lcs(str, str)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends