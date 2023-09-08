#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    ans=''
    ch=arr[0]
    counter=0
    for i in range(0, len(arr)):
        if arr[i]==ch:
            counter+=1
        else:
            ans+=ch
            ans+=str(counter)
            ch=arr[i]
            counter=1
    if counter!=0:
        ans+=ch
        ans+=str(counter)
    return ans


#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends