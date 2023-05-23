#User function Template for python3

class Solution:
    
    #Function to return the adjacency list for each vertex.
    def printGraph(self, V, adj):
        # code here
        ans=[]
        for i in range(V):
            temp=[]
            temp.append(i)
            for j in adj[i]:
                temp.append(j)
            ans.append(temp)
        return ans
            


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
		ans = obj.printGraph(V, adj)
		for i in range(len(ans)):
		    for j in range(len(ans[i])-1):
		        print(ans[i][j], end = "-> ")
		    print(ans[i][len(ans[i])-1]);

# } Driver Code Ends