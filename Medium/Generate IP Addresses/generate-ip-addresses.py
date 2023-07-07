#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def valid(self, str):
        if len(str)==0 or len(str)>3 or (str[0]=='0' and len(str)>1) or int(str)>255:
            return False
        else:
            return True
    def genIp(self, s):
        #Code here
        n=len(s)
        if n>12:
            return ['-1']
        
        ans=[]
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    s1=s[0:i]
                    s2=s[i:j]
                    s3=s[j:k]
                    s4=s[k:]
                    if self.valid(s1) and self.valid(s2) and self.valid(s3) and self.valid(s4):
                        ans.append(s1+"."+s2+"."+s3+"."+s4)
        return ans       


#{ 
 # Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends