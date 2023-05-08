#User function Template for python3
import heapq
class Solution:
    def solve(self, arr, n):
        # code here
        if len(arr)==1:
            return arr[0]
        s1=""
        s2=""
        heap=[]
        for i in range(n):
            heapq.heappush(heap, arr[i])
        
        while len(heap)>0:
            s1+=str(heapq.heappop(heap))
            if len(heap)==0:
                break
            s2+=str(heapq.heappop(heap))
        return int(s1)+int(s2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends