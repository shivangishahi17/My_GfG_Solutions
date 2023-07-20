#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		prefix=1
		suffix=1
		maxProd=float('-inf')
		for i in range(n):
		    if prefix==0:
		        prefix=1
		    if suffix==0:
		        suffix=1
		    prefix=prefix*arr[i]
		    suffix=suffix*arr[n-i-1]
		    maxProd=max(maxProd, max(prefix, suffix))
	    return maxProd
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends