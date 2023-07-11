#User function Template for python3

def rotate(matrix): 
    #code here
    # Step:1-> Transpose of a matrix
    
    
    # Step:2-> Reverse every row of a matrix
    n=len(matrix)
    for i in range(n):
        start=0
        end=n-1
        while start<=end:
            matrix[i][start], matrix[i][end]=matrix[i][end], matrix[i][start]
            start+=1
            end-=1
    
    for i in range(n-1):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
     

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends