#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        low=0
        high=n-1
        ans=float('inf')
        # step 1:Eliminate the left half and take the smallest in the left half
        # step 2:Eliminate the right half and take the smallest in the right half
        
        while low<=high:
            mid=(low+high)//2
            # Eliminate left half
            if arr[low]<=arr[mid]:
                ans=min(ans, arr[low])
                # Eliminate left
                low=mid+1
            else:
                # Eliminate right half
                ans=min(ans, arr[mid])
                # Eliminate right
                high=mid-1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends