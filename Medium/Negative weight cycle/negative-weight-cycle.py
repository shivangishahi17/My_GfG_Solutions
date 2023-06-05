#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		if n==1:
		    return 0
		dist=[float("inf")]*n
		dist[edges[0][0]]=0
		for i in range(n-1):
		    for i in edges:
		        if dist[i[1]]> dist[i[0]]+i[2]:
		            dist[i[1]]=dist[i[0]]+i[2]
	    for i in edges:
	        if dist[i[1]]>dist[i[0]]+i[2]:
	            return 1
	    return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends