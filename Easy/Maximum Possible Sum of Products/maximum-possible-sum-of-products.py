#User function Template for python3

class Solution:

    def MaxSum(self, A, B, N):
        # code here
        A.sort()
        B.sort()
        sum=0
        maxi=0
        for i in range(N):
            sum+=A[i]*B[i]
        maxi=max(maxi, sum)
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())

        A = [int(x) for x in input().split()]
        B = [int(x) for x in input().split()]

        solObj = Solution()

        print(solObj.MaxSum(A, B, N))
# } Driver Code Ends