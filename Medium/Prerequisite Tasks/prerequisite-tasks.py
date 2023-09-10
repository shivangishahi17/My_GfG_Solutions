#User function Template for python3

class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        adj=[[] for i in range(N)]
        for it in prerequisites:
            adj[it[0]].append(it[1])
        
        indegree=[0]*N
        for i in range(N):
            for it in adj[i]:
                indegree[it]+=1
        
        queue=[]
        for i in range(N):
            if indegree[i]==0:
                queue.append(i)
        
        topo=[]  
        while queue:
            node=queue.pop(0)
            topo.append(node)
            
            for it in adj[node]:
                indegree[it]-=1
                if indegree[it]==0:
                    queue.append(it)
        
        if len(topo)==N:
            return True
        return False
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends