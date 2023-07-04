#User function Template for python3

class Solution:
    def isPalindrome(self, S, start, end):
        while start<end:
            if S[start]!=S[end]:
                return False
            start+=1
            end-=1
        return True
    def longestPalin(self, S):
        # code here
        n=len(S)
        maxLen=1
        start=0
        for i in range(n):
            for j in range(i+1, n):
                if (j-i+1>maxLen and self.isPalindrome(S, i, j)):
                    maxLen=j-i+1
                    start=i
        return S[start:start+maxLen]
                
            
     
        #return maxLength
            
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends