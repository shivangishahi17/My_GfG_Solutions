#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def topo(self, node, adj, visited, stack):
        visited[node]=1
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.topo(neighbour, adj, visited, stack)
        stack.append(node)
        
    def dfs(self, node, adj, visited):
        visited[node]=1
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj, visited)
                
    def kosaraju(self, V, adj):
        # code here
        stack=[]
        visited=[0]*V
        for i in range(V):
            if not visited[i]:
                self.topo(i, adj, visited, stack)
        
        adjT=[[] for i in range(V)]
        for i in range(V):
            for j in adj[i]:
                adjT[j].append(i)
        
        visited=[0]*V        
        scc=0
        while stack:
            node=stack.pop()
            if not visited[node]:
                scc+=1
                self.dfs(node, adjT, visited)
        return scc
        
        
        
                
                
    
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
# } Driver Code Ends