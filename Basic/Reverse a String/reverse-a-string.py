#User function Template for python3

class Solution:
    def reverse(self, s):
        start=0
        end=len(s)-1
        while start<end:
            s[start], s[end]=s[end], s[start]
            start+=1
            end-=1
        return "".join(s)
        
    def reverseWord(self, str: str) -> str:
        #your code here
        s=list(str)
        return self.reverse(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends