#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def solve(self, a, b, c, i, j, k, dp):
        if i==len(a) and j==len(b) and k==len(c):
            return 1
            
        if dp[i][j]!=-1:
            return dp[i][j]
        
        res1, res2=0, 0    
        if i<len(a) and a[i]==c[k]:
            res1=self.solve(a, b, c, i+1, j, k+1, dp)
        if j<len(b) and b[j]==c[k]:
            res2=self.solve(a, b, c, i, j+1, k+1, dp)
            
        dp[i][j]=res1+res2
        return dp[i][j]
            
    def isInterleave(self, A, B, C):
        # Code here
        i=0
        j=0
        k=0
        
        if len(A)+len(B)!=len(C):
            return 0
        
        dp=[[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]
        return self.solve(A, B, C, i, j, k, dp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends