#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        minSum=A[0]
        currSum=A[0]
        for i in range(1, N):
            currSum=min(A[i], currSum+A[i])
            minSum=min(minSum, currSum)
        return minSum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends