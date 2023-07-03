#User function Template for python3

class Solution:
        
    def minSwap (self,arr, n, k) : 
        #Complete the function
        count1=0
        for i in range(n):
            if arr[i]<=k:
                count1+=1
                
        count2=0
        for i in range(count1):
            if arr[i]<=k:
                count2+=1
        
        ans=count2        
        i=0
        j=count1
        while j<n:
            if arr[i]<=k:
                count2-=1
            if arr[j]<=k:
                count2+=1
                
            i+=1
            j+=1
            ans=max(ans, count2)
            
        return count1-ans
            
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends