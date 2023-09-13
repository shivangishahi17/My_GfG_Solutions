#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        dict={}
        count=0
        for i in range(n):
            if k-arr[i] in dict:
                count+=dict[k-arr[i]]
            if arr[i] not in dict:
                dict[arr[i]]=1
            else:
                dict[arr[i]]+=1
        return count
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends