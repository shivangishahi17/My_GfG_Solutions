class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
        #Brute Force T.C.=O(Nlog N)+O(2*N), S.C.=O(N)
		n=len(Intervals)
		Intervals.sort()
		res=[]
        for i in range(n):
            start=Intervals[i][0]
            end=Intervals[i][1]
            if len(res)!=0 and end<=res[-1][1]:
                continue
            for j in range(i+1, n):
                if Intervals[j][0]<=end:
                    end=max(end, Intervals[j][1])
                else:
                    break
            res.append([start, end])
        return res
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends