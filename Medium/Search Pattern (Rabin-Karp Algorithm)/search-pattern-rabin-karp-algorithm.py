#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        m=len(patt)
        n=len(s)
        res=[]
        
        for i in range(n):
            if s[i:i+m]==patt:
                res.append(i+1)
        if len(res)==0:
            return [-1]
        return res
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends