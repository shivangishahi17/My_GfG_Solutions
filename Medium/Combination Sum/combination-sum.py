#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def findCombination(self, ind, arr, target, ds, ans):
        if ind==len(arr):
            if target==0:
                ans.append(ds[:])
            return
        
        # pickup the element
        if arr[ind]<=target:
            ds.append(arr[ind])
            self.findCombination(ind, arr, target-arr[ind], ds, ans)
            ds.pop()
        # not pick
        self.findCombination(ind+1, arr, target, ds, ans)
    def combinationalSum(self,A, B):
        A=list(sorted(set(A)))
        ds=[]
        ans=[]
        self.findCombination(0, A, B, ds, ans)
        return ans
        # code here

#{ 
 # Driver Code Starts.


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        ob = Solution()
        result = ob.combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

# } Driver Code Ends