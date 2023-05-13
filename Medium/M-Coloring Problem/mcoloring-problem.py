#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.

def graphColoring(graph, k, V):
    #your code here
    
    def isSafe(graph, color, V, i, j):
        for k in range(V):
            if (graph[i][k]==1 and color[k]==j):
                return False
        return True
    def helper(graph, V, k, i):
        if i==V:
            return True
        for j in range(k):
            if isSafe(graph, color, V, i, j):
                color[i]=j
                if helper(graph, V, k, i+1):
                    return True
                color[i]=-1
        return False
    color=[-1]*V
    return helper(graph, V, k, 0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends