#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        ans=0
        i = 0
        stack = [str[i]]
        i += 1
        while i < len(str):
            while i < len(str) and stack and stack[-1] != str[i]:
                stack.pop()
                i += 1
            if not stack:
                ans += 1
            while i < len(str) and (not stack or stack[-1] == str[i]):
                stack.append(str[i])
                i += 1
        if not stack:
            return ans
        return -1
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends