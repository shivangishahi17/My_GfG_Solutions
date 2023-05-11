#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        ans=[]
        def isSafe(m, visited, n, scrx, scry):
            if(scrx>=0 and scry>=0 and scrx<n and scry<n and m[scrx][scry]==1 and visited[scrx][scry]!=1):
                return True
            else:
                return False
       
        def helper(m, visited, temp, n, scrx, scry):
            if scrx==n-1 and scry==n-1:
                ans.append(temp)
                return
            visited[scrx][scry]=1
            
            if isSafe(m, visited, n, scrx+1, scry):
                helper(m, visited, temp+"D", n, scrx+1, scry)
            
            if isSafe(m, visited, n, scrx, scry-1):
                helper(m, visited, temp+"L", n, scrx, scry-1)
                
            if isSafe(m, visited, n, scrx, scry+1):
                helper(m, visited, temp+"R", n, scrx, scry+1)
                
            if isSafe(m, visited, n, scrx-1, scry):
                helper(m, visited, temp+"U", n, scrx-1, scry)
            
            visited[scrx][scry]=0
        if m[0][0]==0:
            return [-1]
        visited=[]
        for i in range(n):
            col=[]
            for j in range(n):
                col.append(0)
            visited.append(col)
        helper(m, visited, "", n, 0, 0)
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