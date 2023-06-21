#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        #code here
        arr=[]
        for i in Parr:
            arr.append([i.a, i.b])
        arr.sort(key=lambda i:i[1])
        i=0
        j=1
        ans=1
        while j<n:
            if arr[i][1]<arr[j][0]:
                ans+=1
                i=j
                j+=1
            else:
                j+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))
        obj=Solution()
        print(obj.maxChainLen(Parr, n))
# } Driver Code Ends