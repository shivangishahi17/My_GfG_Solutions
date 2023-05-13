#User function Template for python3

class Solution:
    def allPalindromicPerms(self, S):
        # code here 
        def helper(index, s, temp, ans):
            if index == len(s):
                ans.append([ele for ele in temp])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    temp.append(s[index:i+1])
                    helper(i+1, s, temp, ans)
                    temp.pop()
        def isPalindrome(s, start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        ans = []
        temp = []
        helper(0, S, temp, ans)
        return ans
        
        
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        allPart = ob.allPalindromicPerms(S)
        for i in range(len(allPart)): 
            for j in range(len(allPart[i])): 
                print(allPart[i][j], end = " ") 
            print() 
# } Driver Code Ends