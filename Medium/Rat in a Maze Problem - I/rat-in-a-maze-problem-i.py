#User function Template for python3

class Solution:
    def solve(self, i, j, m, n, ans, move, vis):
        if i==n-1 and j==n-1:
            ans.append(move)
            return
        
        if i+1<n and not vis[i+1][j] and m[i+1][j]==1:
            vis[i][j]=1
            self.solve(i+1, j, m, n, ans, move+"D", vis)
            vis[i][j]=0
            
        if j-1>=0 and not vis[i][j-1] and m[i][j-1]==1:
            vis[i][j]=1
            self.solve(i, j-1, m, n, ans, move+"L", vis)
            vis[i][j]=0
            
        if j+1<n and not vis[i][j+1] and m[i][j+1]==1:
            vis[i][j]=1
            self.solve(i, j+1, m, n, ans, move+"R", vis)
            vis[i][j]=0
        
        
        if i-1>=0 and not vis[i-1][j] and m[i-1][j]==1:
            vis[i][j]=1
            self.solve(i-1, j, m, n, ans, move+"U", vis)
            vis[i][j]=0
            
    def findPath(self, m, n):
        # code here
        ans=[]
        move=""
        vis=[[0 for i in range(n)] for j in range(n)]
        if m[0][0]==0:
            return []
        if m[0][0]==1:
            self.solve(0, 0, m, n, ans, "", vis)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends