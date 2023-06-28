#User function Template for python3


class Solution:
    def kadens(self, arr):
        maxSum=arr[0]
        currSum=arr[0]
        
        for i in range(1, len(arr)):
            currSum=max(arr[i], currSum+arr[i])
            maxSum=max(maxSum, currSum)
        return maxSum
        
    def maximumSumRectangle(self,R,C,M):
        #code here
        maxAns=-99999
        for i in range(C):
            arr=[0]*R
            for j in range(i, C):
                for k in range(R):
                    arr[k]+=M[k][j]
                currSu=self.kadens(arr)
                maxAns=max(maxAns, currSu)
        return maxAns
    
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends