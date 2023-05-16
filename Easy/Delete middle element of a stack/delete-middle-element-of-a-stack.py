#User function Template for python3

class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # code here:
        if sizeOfStack == 0:
            return s
        k = sizeOfStack//2 + 1
        self.solve(s,k)
    
    def solve(self,s,k):
        if k == 1:
            s.pop()
        else:
            temp = s.pop()
            self.solve(s,k-1)
            s.append(temp)
            return s
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    t=int(input())
    while(t>0):
        sizeOfStack=int(input())
        myStack=[int(x) for x in input().strip().split()]
        ob = Solution()
        ob.deleteMid(myStack,sizeOfStack)
        while(len(myStack)>0):
            print(myStack[-1],end=" ")
            myStack.pop()
        print()
        t-=1


if __name__=="__main__":
    main()
    
    
# } Driver Code Ends