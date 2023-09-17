#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
	    if N==0 or N==1:
	        return N
	    
	    count=0
	    for i in range(N-1):
	        if A[i]!=A[i+1]:
	            A[count]=A[i]
	            count+=1
	    A[count]=A[N-1]
	    return count+1
	        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends