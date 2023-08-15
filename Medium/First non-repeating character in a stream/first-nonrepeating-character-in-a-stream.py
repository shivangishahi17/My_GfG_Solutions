#User function Template for python3
from collections import OrderedDict
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		s=''
        d=OrderedDict()
        for i in A:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            for k,v in d.items():
                if v==1:
                    s+=k
                    break
            if v>1:
                s+="#"
        return s
		    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends