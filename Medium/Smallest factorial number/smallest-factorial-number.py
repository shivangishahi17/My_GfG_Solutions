#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        low=0
        high=5*n
        ans=low
        while low<=high:
            mid=(low+high)//2
            zeros=self.find_no_of_zeros_factorial(mid)
            if zeros>=n:
                ans=mid
                # min ans
                high=mid-1
            else:
                low=mid+1
        return ans
    def find_no_of_zeros_factorial(self, x): 
        denom=5
        zeros=0
        while(x>=denom):
            zeros+=(x//denom)
            denom*=5
        return zeros

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends