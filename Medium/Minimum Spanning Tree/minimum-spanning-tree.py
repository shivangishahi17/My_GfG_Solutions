#User function Template for python3
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # shradha didi approach
        # T.C.=O(E.logE)
        cost=0
        visited=[False]*V
        heap=[]
        heapq.heappush(heap, (0, 0))
        
        # priority queue(heap) ke khali hone ka mtlb hai non-mst ka khali hona. Sare k sare element non mst 
        # se mst ke andar include ho gye hai.
        while heap:
            wt, node= heapq.heappop(heap)
            if not visited[node]:
                visited[node]=True
                cost+=wt
                for neighbour, edge in adj[node]:
                    if not visited[neighbour]:
                        heapq.heappush(heap, (edge, neighbour))
        return cost
        
        
        
        
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends