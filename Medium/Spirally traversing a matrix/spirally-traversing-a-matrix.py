#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        res=[]
        # index of first column
        left=0
        # index of first row
        top=0
        # index of last column
        right=c-1
        # index of last row
        bottom=r-1
        
        while(top<=bottom and left<=right):
            # Traverse right
            # print first row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top+=1
            
            # Traverse down
            # print last column
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right-=1
            
            # Traverse left
            if top<=bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom-=1
            
            # Traverse up
            if left<=right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left+=1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends