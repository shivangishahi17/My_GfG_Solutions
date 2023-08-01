#User function Template for python3

class Solution:
    def isPalindrome(self, str, start, end):
        while start<=end:
            if str[start]!=str[end]:
                return False
            start+=1
            end-=1
        return True
    
    def func(self, ind, str, path, ans):
        if ind==len(str):
            ans.append([ele for ele in path])
            return 
            
        for i in range(ind, len(str)):
            if self.isPalindrome(str, ind, i):
                path.append(str[ind:i+1])
                self.func(i+1, str, path, ans)
                path.pop()
                
    def allPalindromicPerms(self, S):
        # code here 
        ans=[]
        path=[]
        self.func(0, S, path, ans)
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