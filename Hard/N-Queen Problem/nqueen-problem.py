#User function Template for python3

class Solution:
    def isSafe(self, row, col, board, n):
        duprow=row
        dupcol=col
        
        while row>=0 and col>=0:
            if board[row][col]==1:
                return False
            row-=1
            col-=1
        
        col=dupcol
        row=duprow
        while col>=0:
            if board[row][col]==1:
                return False
            col-=1
        
        row=duprow
        col=dupcol
        while row<n and col>=0:
            if board[row][col]==1:
                return False
            row+=1
            col-=1
        return True
        
    def helper(self, col, board, ans, n, temp):
        if col==n:
            ans.append(temp[:])
            return 
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col]=1
                temp.append(row+1)
                self.helper(col+1, board, ans, n, temp)
                temp.pop()
                board[row][col]=0
                
    def nQueen(self, n):
        # code here
        ans=[]
        board=[[0 for i in range(n)] for j in range(n)]
        self.helper(0, board, ans, n, [])
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends