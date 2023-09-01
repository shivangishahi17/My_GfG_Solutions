class Solution:
    def solve(self, nums, start, end):
        if start>end:
            return
        mid=(start+end)//2
        self.ans.append(nums[mid])
        self.solve(nums, start, mid-1)
        self.solve(nums, mid+1, end)
	def sortedArrayToBST(self, nums):
	    # code here
	    n=len(nums)
	    self.ans=[]
	    self.solve(nums, 0, n-1)
	    return self.ans


#{ 
 # Driver Code Starts

T=int(input())
for i in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	obj = Solution()
	ans = obj.sortedArrayToBST(nums)
	for _ in ans:
		print(_, end = " ")
	print()

# } Driver Code Ends