class Solution:
    def dfs(self, node, adj, color, newColor):
        color[node]=newColor
        
        for neighbour in adj[node]:
            if color[neighbour]==-1:
                if not self.dfs(neighbour, adj, color, not newColor):
                    return False
            elif color[neighbour]==color[node]:
                return False
        return True
        
	def isBipartite(self, V, adj):
		#code here
		color=[-1]*V
		
		for i in range(V):
		    if color[i]==-1:
		        if not self.dfs(i, adj, color, 0):
		            return False
	    return True


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends