#User function Template for python3
class Solution:
    def checkPalindrome(self, str):
        str1=list(str)
        left=0
        right=len(str)-1
        
        while left<right:
            if str1[left]!=str1[right]:
                return 0
            left+=1
            right-=1
        return 1
        
	def isPalindrome(self, S):
		# code here
		return self.checkPalindrome(S)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends