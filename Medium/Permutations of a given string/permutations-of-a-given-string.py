#User function Template for python3

class Solution:

    def find_permutation(self, S):
        # Code here
        def solve(arr, ans, idx):
            if idx==len(S):
                if "".join(arr[:]) not in ans:
                    ans.append("".join(arr[:]))
            for i in range(idx, len(S)):
                arr[idx], arr[i]=arr[i], arr[idx]
                solve(arr, ans, idx+1)
                arr[idx], arr[i]=arr[i], arr[idx]
        ans=[]
        arr=list(S)
        solve(arr, ans, 0)
        ans.sort()
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
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends