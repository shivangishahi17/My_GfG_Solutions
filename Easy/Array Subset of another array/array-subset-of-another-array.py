#User function Template for python3
    #dict to create count of each element in a1
    #User function Template for python3

def isSubset( a1, a2, n, m):
    if m>n:
        return "No"
    hashmap={}
    for i in range(n):
        if a1[i] in hashmap:
            hashmap[a1[i]]+=1
        else:
            hashmap[a1[i]]=1
            
    for i in range(m):
        if a2[i] not in hashmap or hashmap[a2[i]]==0:
            return "No"
        else:
            hashmap[a2[i]]-=1
    return "Yes"
    
   
    
    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends