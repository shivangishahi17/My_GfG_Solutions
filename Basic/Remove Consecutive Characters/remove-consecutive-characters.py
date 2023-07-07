#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        stack=[]
        for i in S:
            if len(stack)>0 and stack[-1]==i:
                stack.pop()
            stack.append(i)
        return "".join(stack)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends