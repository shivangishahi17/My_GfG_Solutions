from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self, v, adj, visited, parent):
        visited[v]=True
        for neighbour in adj[v]:
            if not visited[neighbour]:
                if self.dfs(neighbour, adj, visited, v):
                    return True
            else:
                if parent!=neighbour:
                    return True
        return False
            
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited=[False]*V
		for i in range(V):
		    if not visited[i]:
		        if self.dfs(i, adj, visited, -1):
		            return True
		return False
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends