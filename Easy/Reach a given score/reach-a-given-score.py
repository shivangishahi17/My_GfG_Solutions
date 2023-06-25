#User function Template for python3

def count(n):
    #your code here

    dp = [0 for i in range(n+1)]
 
    # Base case (If given value is 0)
    dp[0] = 1
 
    # One by one consider given 3 moves and update the
    # table[] values after the index greater than or equal
    # to the value of the picked move.
    for i in range(3, n+1):
        dp[i] += dp[i-3]
    for i in range(5, n+1):
        dp[i] += dp[i-5]
    for i in range(10, n+1):
        dp[i] += dp[i-10]
 
    return dp[n]
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends