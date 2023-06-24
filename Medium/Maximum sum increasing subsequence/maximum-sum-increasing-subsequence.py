#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		dp=[0 for i in range(n)]
		for i in range(n):
		    dp[i]=Arr[i]
		    
		for i in range(n):
		    for j in range(0, i):
		        if Arr[j]<Arr[i]:
		            dp[i]=max(dp[i], dp[j]+Arr[i])
        
        ma=0
        for i in range(n):
            ma=max(ma, dp[i])
        return ma

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxSumIS(Arr,n)
		print(ans)

# } Driver Code Ends