#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        if(sum(a)%k!=0):return False
        target=sum(a)//k
        used=[False for i in range(len(a))]
        
        def backtrack(index,k,subsetSum):
            if(k==0):
                return True
            if(subsetSum==target):
                return backtrack(0,k-1,0)
            for j in range(index,len(a)):
                if(used[j]==True or subsetSum+a[j]>target):
                    continue
                used[j]=True
                if(backtrack(index+1,k,subsetSum+a[j])):
                    return True
                used[j]=False
            return False
        return backtrack(0,k,0)


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