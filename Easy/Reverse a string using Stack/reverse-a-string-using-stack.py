#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    stack1=[]
    stack2=[]
    for i in S:
        stack1.append(i)
    for i in range(len(stack1)):
        stack2.append(stack1.pop())
    return "".join(stack2)
    #Add code here
      

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends