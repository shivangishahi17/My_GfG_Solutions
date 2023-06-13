class Solution:
        
    def dfs(self, image, i, j, n, m, color, newColor):
        if i<0 or j<0 or i>=n or j>=m or image[i][j]!=color:
            return
        
        image[i][j]=newColor
        self.dfs(image, i-1, j, n, m, color, newColor)
        self.dfs(image, i+1, j, n, m, color, newColor)
        self.dfs(image, i, j-1, n, m, color, newColor)
        self.dfs(image, i, j+1, n, m, color, newColor)
            
        
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		n=len(image)
		m=len(image[0])

		color=image[sr][sc]
		
		if color!=newColor:
		    self.dfs(image, sr, sc, n, m, color, newColor)
		
	    return image	


# ////////////////////////////////////

       

#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends