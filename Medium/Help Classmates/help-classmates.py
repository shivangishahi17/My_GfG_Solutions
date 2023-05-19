#User function Template for python3

class Solution:
    def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        stack=[]
        ans=[]
        for i in range(n-1, -1, -1):
            while(len(stack)>0 and stack[-1]>=arr[i]):
                stack.pop()
            if len(stack)>0:
                ans.append(stack[-1])
            else:
                ans.append(-1)
            stack.append(arr[i])
        return ans[::-1]
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends