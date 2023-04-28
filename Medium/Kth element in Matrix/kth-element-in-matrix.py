#User function Template for python3
def countSmallerThanEqualToMid(row, mid):
    low=0
    high=len(row)-1
    
    while(low<=high):
        md=(low+high)//2
        if row[md]<=mid:
            low=md+1
        else:
            high=md-1
    return low    
        
        
def kthSmallest(mat, n, k): 
    # Your code goes here
    low=mat[0][0]
    high=mat[-1][-1]
    
    while(low<=high):
        mid=(low+high)//2
        
        count=0
        for i in range(n):
            count+=countSmallerThanEqualToMid(mat[i], mid)
        if count<k:
            low=mid+1
        else:
            high=mid-1
    return low
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Driver Code 

def main():
    T=int(input())
    while(T>0):
        n = int(input())
        mat=[[0 for j in range(n)] for i in range(n)]
        line1=[int(x) for x in input().strip().split()]
        k = int(input())

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1


if __name__=="__main__":
    main()




# } Driver Code Ends