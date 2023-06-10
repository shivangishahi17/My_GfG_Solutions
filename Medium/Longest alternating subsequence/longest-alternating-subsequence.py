#User function Template for python3

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
        n=len(nums)
        ma=1
        mi=1
        for i in range(1, n):
            if nums[i]>nums[i-1]:
                ma=mi+1
            elif nums[i]<nums[i-1]:
                mi=ma+1
            else:
                continue
        return max(ma, mi)
            
                        
                    

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.AlternatingaMaxLength(nums)
		print(ans)

# } Driver Code Ends