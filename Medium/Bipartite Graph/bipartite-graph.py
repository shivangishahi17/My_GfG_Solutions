class Solution:
    def bfs(self, start, V, adj, color):
        queue=[]
        queue.append(start)
        color[start]=0
        
        while queue:
            node=queue.pop(0)
            for i in adj[node]:
                if color[i]==-1:
                    color[i]=not color[node]
                    queue.append(i)
                elif color[i]==color[node]:
                    return False
        return True
	def isBipartite(self, V, adj):
		#code here
		queue=[]
		queue.append(0)
		color=[-1]*V
		for i in range(V):
		    color[i]=-1
		
		for i in range(V):
		    if color[i]==-1:
		        if self.bfs(i, V, adj, color)==False:
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