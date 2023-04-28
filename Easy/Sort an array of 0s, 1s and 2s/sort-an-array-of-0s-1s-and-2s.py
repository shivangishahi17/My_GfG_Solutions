#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        count0=0
        count1=0
        count2=0
        
        for i in range(n):
            if arr[i]==0:
                count0+=1
            elif arr[i]==1:
                count1+=1
            else:
                count2+=1
        
        i=0
        while(count0>0):
            arr[i]=0
            i+=1
            count0-=1
            
        while(count1>0):
            arr[i]=1
            i+=1
            count1-=1
            
        while(count2>0):
            arr[i]=2
            i+=1
            count2-=1
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends