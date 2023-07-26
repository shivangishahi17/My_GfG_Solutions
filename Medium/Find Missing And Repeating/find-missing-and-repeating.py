#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        # Naive approach T.C.=O(N) S.C.=O(N)
        temp=[0]*n
        repeating=-1
        missing=-1
        for i in range(n):
            temp[arr[i]-1]+=1
            if temp[arr[i]-1]>1:
                repeating=arr[i]
        for i in range(n):
            if temp[i]==0:
                missing=i+1
                break
        return repeating, missing
        
       
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends