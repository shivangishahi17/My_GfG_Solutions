#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		ans=[]
        xor=nums[0]
        n=len(nums)
        
        for i in range(1,n):
            xor = xor^nums[i]
        
        # Find right most bit
        right_bit = xor & ~(xor-1)
        x=0
        y=0
        
        for i in range(n):
            if nums[i]&right_bit:
                x=x^nums[i]
            else:
                y=y^nums[i]
        
        ans.append(x)
        ans.append(y)
        ans.sort()
        return ans
		
		        
		
		    
	
	    	        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends