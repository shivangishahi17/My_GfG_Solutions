#User function Template for python3

def findElement( arr, n):
    greater = [0]*n
    smaller = [0]*n
    
    greater[0] = arr[0]
    for i in range(1, n):
        greater[i] = max(arr[i], greater[i-1])
    
    smaller[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        smaller[i] = min(smaller[i+1], arr[i])
        
    for i in range(1, n-1):
        if greater[i] <= arr[i] and smaller[i] >= arr[i]:
            return arr[i]
    
    return -1
        
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends