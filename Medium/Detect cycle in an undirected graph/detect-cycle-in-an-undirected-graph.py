from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
    def defect(self, src, adj, vis, parent):
        vis[src]=1
        for neighbour in adj[src]:
            if not vis[neighbour]:
                vis[neighbour]=1
                if self.defect(neighbour, adj, vis, src):
                    return True
            else:
                if parent!=neighbour:
                    return True
        return False
        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis=[0]*V
        for i in range(0, V):
            if not vis[i]:
                if self.defect(i, adj, vis, -1):
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