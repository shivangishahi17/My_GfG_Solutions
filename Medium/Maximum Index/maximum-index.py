#User function Template for python3
class Solution:

	def maxIndexDiff(self,arr,n):
		#code here
		ans=0
		i=0
		j=n-1
		while(i<=j):
		    if arr[i]<=arr[j]:
		        ans=max(ans, j-i)
		        i+=1
		        j=n-1
	        else:
	            j-=1
	    return ans


#{ 
 # Driver Code Starts
if __name__ == "__main__":
	t = int(input())
	while(t>0):
		num = int(input())
		arr = [int(x) for x in input().strip().split()]
		ob = Solution()
		print(ob.maxIndexDiff(arr,num))
		t-=1
# } Driver Code Ends