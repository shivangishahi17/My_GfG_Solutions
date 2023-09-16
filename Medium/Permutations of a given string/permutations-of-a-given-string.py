#User function Template for python3

class Solution:
    def permute(self, arr, ans, ind):
        if ind==len(arr):
            if "".join(arr) not in ans:
                ans.append("".join(arr))
            return
        
        for i in range(ind, len(arr)):
            arr[i], arr[ind]=arr[ind], arr[i]
            self.permute(arr, ans, ind+1)
            arr[i], arr[ind]=arr[ind], arr[i]
                
        
    def find_permutation(self, S):
        # Code here
        # T.C.=O(N)*N!=O(N) for loop and N! for generating permutation
        # S.C.=O(1) apart from auxiliaary space of recursion depth Here O(N) is recursion space and O(N!)
        # space for returning the answer
        ind=0
        arr=list(S)
        ans=[]
        self.permute(arr, ans, ind)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends