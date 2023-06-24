#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        arr.sort()
 
        # dp[i] denotes the maximum disjoint
        # pair sum we can achieve using first
        # i elements
        dp = [0] * N
     
        # if no element then dp value will be 0
        dp[0] = 0
     
        for i in range(1, N):
         
            # first give previous value to
            # dp[i] i.e. no pairing with
            # (i-1)th element
            dp[i] = dp[i-1]
     
            # if current and previous element
            # can form a pair
            if (arr[i] - arr[i-1] < K):
             
                # update dp[i] by choosing
                # maximum between pairing
                # and not pairing
                if (i >= 2):
                    dp[i] = max(dp[i], dp[i-2] + arr[i] + arr[i-1]);
                else:
                    dp[i] = max(dp[i], arr[i] + arr[i-1]);
             
        # last index will have the result
        return dp[N - 1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends