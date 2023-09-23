#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        low=0
        high=N-1
        mid=0
        while(low<=high):
            mid=(low+high)//2
            
            if Arr[mid]==k:
                return mid
            if Arr[mid]<k:
                low=mid+1
            if Arr[mid]>k:
                high=mid-1
        else:
            return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends