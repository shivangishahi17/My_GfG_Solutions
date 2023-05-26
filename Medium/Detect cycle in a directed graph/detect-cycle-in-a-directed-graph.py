#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def dfs(self, node, adj, visited, recSt):
        visited[node]=True
        recSt[node]=True
        for neighbour in adj[node]:
            if not visited[neighbour]:
                if self.dfs(neighbour, adj, visited, recSt):
                    return True
            elif recSt[neighbour]:
                return True
        recSt[node]=False
        return False
            
            
    def isCyclic(self, V, adj):
        # code here
        visited=[False]*V
        recSt=[False]*V
        for i in range(V):
            if not visited[i]:
                if self.dfs(i, adj, visited, recSt):
                    return True
        return False
        
        
        
                
                
    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends