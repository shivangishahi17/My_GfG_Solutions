#User function Template for python3
import heapq
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        heap=[]
        for i in range(len(arr)):
            heapq.heappush(heap, arr[i])
        for i in range(k-1):
            heapq.heappop(heap)
        return heap[0]
            
        #Transform list x(here array) into a heap, in-place, in linear time. heapq modules provide min-heap 
        # implementation
        # for i in range(len(arr)):
        #     heapq.heapify(arr) # smallest element of array will come at 0th index {3, 4, 10,...}
        # for i in range(k-1): # i=0, 1
        #     # pop and return the smallest item from the array
        #     heapq.heappop(arr)
        # return arr[0]


# def kthSmallest(self,arr, l, r, k):
#         l=[]
#         for i in arr:
#             heapq.heappush(l,1*i)
#         i=0
#         while i<k-1:
#             heapq.heappop(l)
#             i+=1
        # return abs(heapq.heappop(l))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends