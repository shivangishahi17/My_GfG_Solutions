#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		curr_prod=1
		max_prod=arr[0]
		
		for i in range(n):
		    curr_prod*=arr[i]
		    max_prod=max(curr_prod, max_prod)
		    
		    if(curr_prod==0):
		        curr_prod=1
        
        curr_prod=1
        # Traverse from right
        for i in range(n-1, -1, -1):
            curr_prod*=arr[i]
            max_prod=max(curr_prod, max_prod)
            
            if(curr_prod==0):
                curr_prod=1
        return max_prod

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