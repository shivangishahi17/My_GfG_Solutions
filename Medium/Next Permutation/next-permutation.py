#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        n=len(arr)
        ind=-1
        for i in range(n-2, -1, -1):
            if arr[i]<arr[i+1]:
                ind=i
                break
        if ind==-1:
            arr.reverse()
            return arr
        for i in range(n-1, ind, -1):
            if arr[i]>arr[ind]:
                arr[i], arr[ind]=arr[ind], arr[i]
                break
        arr[ind+1:]=reversed(arr[ind+1:])
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends