#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		dict={}
        for i,j in enumerate(arr): #0,15, 1,2, 2,45, 3,12, 4,7
            dict[i+1] = j #dict[1]= 15, dict[2]=2
            
        lst=[]
        for i,j in dict.items():
            if i == j:
                lst.append(i)
            
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends