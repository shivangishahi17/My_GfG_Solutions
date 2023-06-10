#User function Template for python3
class Solution:
	def maxSumIS(self, Arr, n):
		# code here
		lis=[1]*n
		sumlis=Arr[:]
		for i in range(1, n):
		    for j in range(0, i):
		        if Arr[i]>Arr[j] and lis[i]<lis[j]+1:
		            lis[i]=lis[j]+1
		            sumlis[i]=max(sumlis[i], Arr[i]+sumlis[j])
	    return max(sumlis)


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