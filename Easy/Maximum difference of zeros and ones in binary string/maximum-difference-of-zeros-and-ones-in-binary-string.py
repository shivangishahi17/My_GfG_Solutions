#User function Template for python3
class Solution:
	def maxSubstring(self, S):
		# code here
		if '0' not in S:
		    return -1
		    
		n=len(S)
		countZero=0
		countOne=0
		maxDiff=0
		
		for i in range(n):
		    if S[i]=='0':
		        countZero+=1
		    else:
		        countOne+=1
		    maxDiff=max(maxDiff, countZero-countOne)
		    
		    if countOne>countZero:
		        countZero=countOne=0
	    return maxDiff


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends