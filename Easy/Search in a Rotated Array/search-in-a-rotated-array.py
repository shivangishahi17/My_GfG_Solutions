#User function Template for python3

class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        if l>h:
            return -1
     
        mid=(l + h)//2
        if A[mid]==key:
            return mid
        
        if A[l]<=A[mid]:
            if key>=A[l] and key<=A[mid]:
                return self.search(A, l, mid-1, key)
            return self.search(A, mid + 1, h, key)
     
        if key>=A[mid] and key<=A[h]:
            return self.search(A, mid + 1, h, key)
        return self.search(A, l, mid-1, key)
     
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        k = int(input())
        ob=Solution()
        print(ob.search(A, 0, n - 1, k))
# } Driver Code Ends