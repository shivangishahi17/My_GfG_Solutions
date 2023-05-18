#User function Template for python3

#Function to reverse the queue.
def rev(q):
    #add code here
    # base case
    queue=[]
    while q.qsize()!=0:
        queue.append(q.get())
    
    n=len(queue)
    for i in range(n):
        q.put(queue[n-i-1])
    return q

    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends