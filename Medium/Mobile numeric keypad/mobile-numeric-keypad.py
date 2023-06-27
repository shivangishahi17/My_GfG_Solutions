#User function Template for python3
class Solution:
    def solve(self, i, j, n, arr, dp):
        if n==1:
            return 1
        
        if dp[arr[i][j]][n]!=-1:
            return dp[arr[i][j]][n]
        
        a=b=c=d=e=0
        a=self.solve(i, j, n-1, arr, dp)
        # row down
        if i+1<4 and arr[i+1][j]!=-1:
            b=self.solve(i+1, j, n-1, arr, dp)
        # row up
        if i-1>=0 and arr[i-1][j]!=-1:
            c=self.solve(i-1, j, n-1, arr, dp)
        # col left
        if j-1>=0 and arr[i][j-1]!=-1:
            d=self.solve(i, j-1, n-1, arr, dp)
        # col right
        if j+1<3 and arr[i][j+1]!=-1:
            e=self.solve(i, j+1, n-1, arr, dp)
                
        dp[arr[i][j]][n]=a+b+c+d+e
        return dp[arr[i][j]][n]
            
	def getCount(self, N):
		# code here
		i=0
		j=0
		res=0
		dp=[[-1 for i in range(N+1)] for i in range(10)]
		arr=[
		   [1, 2, 3],
		   [4, 5, 6],
		   [7, 8, 9],
		   [-1, 0, -1]
		   ]
		for i in range(4):
		    for j in range(3):
		        if arr[i][j]!=-1:
		            res+=self.solve(i, j, N, arr, dp)
	    return res
		          


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.getCount(N)
		print(ans)

# } Driver Code Ends