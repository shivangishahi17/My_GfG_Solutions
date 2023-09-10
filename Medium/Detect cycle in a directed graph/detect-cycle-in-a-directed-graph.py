#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        indegree=[0]*V
        for i in range(V):
            for it in adj[i]:
                indegree[it]+=1
        
        queue=[]
        for i in range(V):
            if indegree[i]==0:
                queue.append(i)
        
        count=0    
        while queue:
            node=queue.pop(0)
            count+=1
            
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it]==0:
                    queue.append(it)
        
        if count==V:
            return False
        return True
            


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