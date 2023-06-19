#User function Template for python3

class Solution:
    def countWays(self,n,k):
        #code here.
        mod=10**9+7
        if n==0:
            return 0
        if n==1:
            return k
        same = k%mod
        diff = (k*(k-1))%mod
        
        for i in range(3, n+1):
            prev = diff%mod
            diff = ((same+diff)*(k-1))%mod
            same = prev%mod
        return (same+diff)%mod
        
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    ob = Solution()
    ans=ob.countWays(n,k)
    print(ans)

# } Driver Code Ends