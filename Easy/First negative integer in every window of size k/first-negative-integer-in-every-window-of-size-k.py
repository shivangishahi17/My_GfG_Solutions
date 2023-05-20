#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    q=[]
    ans=[]
    start=0
    end=0
    while end<N:
        if A[end]<0:
            q.append(A[end])
            
        if (end-start+1)<K:
            end+=1
            
        elif (end-start+1==K):
            if len(q)==0:
                ans.append(0)
            else:
                ans.append(q[0])
                if q[0]==A[start]:
                    q.pop(0)
            start+=1
            end+=1
    return ans
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends