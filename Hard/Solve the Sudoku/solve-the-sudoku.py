#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def isValid(self, row, col, grid, k):
        for i in range(9):
            if grid[i][col]==k:
                return False
            
            if grid[row][i]==k:
                return False
                
            if grid[3*(row//3)+i//3][3*(col//3)+i%3]==k:
                return False
        return True
        
    def SolveSudoku(self,grid):
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==0:
                    for k in range(1, 10):
                        if self.isValid(i, j, grid, k):
                            grid[i][j]=k
                            
                            if self.SolveSudoku(grid)==True:
                                return True
                            else:
                                grid[i][j]=0
                    return False
        return True
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        
        # Your code here
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=' ')
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends