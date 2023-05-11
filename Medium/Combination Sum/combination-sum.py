#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


# } Driver Code Ends
#User function Template for python3

class Solution:
    def helper(self, arr, target, ans, temp):
        # Base case
        if target<0:
            return
        if target==0:
            ans.append(temp[:])
            return
        
        for i in range(len(arr)):
            if arr[i]>target:
                break
            if i>0 and arr[i]==arr[i-1]:
                continue
            # taking
            temp.append(arr[i])
            self.helper(arr[i:], target-arr[i], ans, temp)
            temp.pop()
    
    #Function to return a list of indexes denoting the required 
    #combinations whose sum is equal to given number.
    def combinationalSum(self,A, B):
    
        # code here
        A.sort()
        ans=[]
        temp=[]
        self.helper(A, B, ans, temp)
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