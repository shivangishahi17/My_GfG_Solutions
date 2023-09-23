#User function Template for python3

def Search(arr,n,k):
    #code here
    low=0
    high=n-1
    
    while low<=high:
        mid=(low+high)//2
        
        if arr[mid]==k:
            return mid
        
        # Check for left sorted
        if arr[low]<=arr[mid]:
            # target lies within the left half.
            if arr[low]<=k and k<=arr[mid]:
                # eliminate right half.
                high=mid-1
            else:
                # eliminate left half.
                low=mid+1

        # Check for right sorted
        else:
            if arr[mid]<=k and k<=arr[high]:
                # eliminate left half because target lies on right half.
                low=mid+1
            else:
                # eliminate right half.
                high=mid-1
    return -1    
                
                
                
            
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs=int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())

        print(Search(arr,n,k))

# } Driver Code Ends