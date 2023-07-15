#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        left=[0]*n
        right=[0]*n
        
        left[0]=1
        right[n-1]=1
        
        for i in range(1, n):
            left[i]=left[i-1]*nums[i-1]
        
        for i in range(n-2, -1, -1):
            right[i]=right[i+1]*nums[i+1]
            
        for i in range(n):
            nums[i]=left[i]*right[i]
        return nums


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends