#User function Template for python3

class Solution:
    def wordBreak(self, n, dict, s):
        # code here
        dic=set()
        for word in dict:
            dic.add(word)
        ans=[]
        
        def find(s, dic, i, res, par_ans):
            if i>=len(s):
                if not par_ans:
                    ans.append(' '.join(res))
                return
            par_ans+=s[i]
            if par_ans in dic:
                res.append(par_ans)
                find(s, dic, i+1, res, '')
                res.pop()
            find(s, dic, i+1, res, par_ans)
                
        find(s, dic, 0, [], '')
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        dicti = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.wordBreak(n, dicti, s)
        if(len(ans) == 0):
            print("Empty")
        else:
            ans.sort()
            for it in (ans):
                print("("+it,end = ")")
            print()
# } Driver Code Ends