#User function Template for python3

class Solution:
    def countSmallerThanMid(self, row, mid):
        low=0
        high=len(row)-1
        
        while(low<=high):
            md=(low+high)//2
            
            if row[md]<=mid:
                low=md+1
            else:
                high=md-1
        return low
        
    def median(self, matrix, R, C):
    	#code here 
    	low=1
    	high=1e9
    	
    	while(low<=high):
    	    mid=(low+high)//2
    	    count=0
    	    for i in range(R):
    	        count+=self.countSmallerThanMid(matrix[i], mid)
    	    if count<=((R*C)//2):
    	        low=mid+1
    	    else:
    	        high=mid-1
        return int(low)
    	    
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends