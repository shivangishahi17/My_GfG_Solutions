#User function Template for python3


class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
        dp=[0]*(n)
        
        dp[0]=arr[0]
        dp[1]=arr[0]+arr[1]
        dp[2]=max(arr[1]+arr[2], arr[0]+arr[2], arr[0]+arr[1])
        
        for i in range(3, n):
            dp[i]=max(arr[i-1]+arr[i]+dp[i-3], dp[i-2]+arr[i], dp[i-1])
        return dp[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends