#User function Template for python3

class Solution:
    def findMinLen(self, arr, n):
        minLength=len(arr[0])
        for i in range(1, n):
            minLength=min(minLength, len(arr[i]))
        return minLength
        
        
    def longestCommonPrefix(self, arr, n):
        # code here
        minLen=self.findMinLen(arr, n)
        res=''
        for i in range(minLen):
            currChar=arr[0][i]
            for j in range(1, n):
                if arr[j][i]!=currChar:
                    if res=='':
                       return -1
                    else:
                        return res
            res+=currChar
        return res
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends