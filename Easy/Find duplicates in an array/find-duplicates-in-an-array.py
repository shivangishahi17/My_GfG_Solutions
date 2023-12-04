class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	res=[]
    	freq=[0]*n
    	for i in arr:
    	    freq[i]+=1
    	
    	for i in range(n):    
        	if freq[i]>1:
        	        res.append(i)
    	if len(res)>0:
    	    return res
    	else:
    	    return [-1]
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends