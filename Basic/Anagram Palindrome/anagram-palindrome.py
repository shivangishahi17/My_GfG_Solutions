#User function Template for python3

class Solution:

    def isPossible(self, S):

        # code here
        dic={}
        for i in S:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        count=0
        for j in dic.values():
            if j%2==1:
                count+=1
        if count>1:
            return 0
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends