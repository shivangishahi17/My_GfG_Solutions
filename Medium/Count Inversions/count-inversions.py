class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def merge(self, arr, low, mid, high):
        temp=[]
        left=low
        right=mid+1
        
        cnt=0
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                cnt+=(mid-left+1)
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1
        
        while right<=high:
            temp.append(arr[right])
            right+=1
        
        for i in range(low, high+1):
            arr[i]=temp[i-low]
        return cnt
        
    def mergeSort(self, arr, low, high):
        cnt=0
        if low>=high:
            return cnt
        mid=(low+high)//2
        cnt+=self.mergeSort(arr, low, mid)
        cnt+=self.mergeSort(arr, mid+1, high)
        cnt+=self.merge(arr, low, mid, high)
        return cnt
        
    def inversionCount(self, arr, n):
        # Your Code Here
        return self.mergeSort(arr, 0, n-1)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends