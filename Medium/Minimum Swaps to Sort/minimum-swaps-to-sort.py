

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
        count=0
        list=[]
        for i,j in enumerate(nums): #[(0,2),(1,8),(2,5),(3,4)]=(index no, value)
            list.append([j,i]) #[[2,0],[8,1],[5,2],[4,3]]
        list.sort(key=lambda x:x[0]) #[[2,0],[4,3],[5,2],[8,1]]
        
        i=0
        while(i<len(nums)):
            if i!=list[i][1]:
                index=list[i][1] #3
                list[i],list[index]=list[index],list[i] #[4,3],[8,1]=[8,1],[4,3]
                count+=1 #1
                i-=1 #0
            i+=1 #2
        return count

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends