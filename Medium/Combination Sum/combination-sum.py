#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

#User function Template for python3

class Solution:
    def helper(self, arr, target, i, ans, temp):
        # Base case
        if i==len(arr):
            if target==0:
                ans.append(temp[:])
            return
            
        if arr[i]<=target:
            # taking
            temp.append(arr[i])
            self.helper(arr, target-arr[i], i, ans, temp)
            temp.pop()
        # not taking
        self.helper(arr, target, i+1, ans, temp)
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
    
        # code here
        A=list(sorted(set(A)))
        ans=[]
        temp=[]
        self.helper(A, B, 0, ans, temp)
        return ans
        
        

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