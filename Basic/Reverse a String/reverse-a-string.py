#User function Template for python3

def reverseWord(s):
    #your code here
    s=list(s)
    i=0
    j=len(s)-1
    while i<=j:
        s[i], s[j]=s[j], s[i]
        i+=1
        j-=1
    return "".join(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends