#User function Template for python3

class Solution:
    def isSafe(self, row, col, temp, n):
        # row and col
        for i in range(col, -1, -1):
            if temp[row][i]==1:
                return False
        x=row-1
        y=col-1
        while x>=0 and y>=0:
            if temp[x][y]==1:
                return False
            x-=1
            y-=1
            
        x=row+1
        y=col-1
            
        while x<n and y>=0:
            if temp[x][y]==1:
                return False
            x+=1
            y-=1
        return True
            
    def helper(self, ans, temp, col, n):
        if col==n:
            board=[]
            for i in range(n):
                for j in range(n):
                    if temp[j][i]==1:
                        board.append(j+1)
            ans.append(board)
            return
        for row in range(n):
            if self.isSafe(row, col, temp, n):
                temp[row][col]=1
                self.helper(ans, temp, col+1, n)
                temp[row][col]=0
        
    def nQueen(self, n):
        # code here
        
        ans=[]
        temp=[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(0)
            temp.append(row)
        self.helper(ans, temp, 0, n)
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