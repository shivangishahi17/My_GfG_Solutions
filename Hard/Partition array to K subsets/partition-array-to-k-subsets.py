#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        n = len(a)
        target = sum(a)/k
        subSets = [0]*k
        
       
        def recurse(i):
            if i == n:    
                return True

            for j in range(k):
                if subSets[j] +a[i] <= target:
                    subSets[j] += a[i]

                    if recurse(i + 1):
                        return True

                    subSets[j] -= a[i]

                    if subSets[j] == 0:
                        break
                        
            return False
        
        return recurse(0)


#{ 
 # Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends