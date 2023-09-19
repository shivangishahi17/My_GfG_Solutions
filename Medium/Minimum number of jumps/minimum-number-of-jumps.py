#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if len(arr)<=1: 
            return 0 
  
        # Return -1 if not possible to jump 
        if arr[0]==0:  
            return -1 
  
        # initialization 
        maxReach=arr[0] 
        step=arr[0]
        jump=1
  
  
        # Start traversing array 
        for i in range(1, len(arr)):

            # Check if we have reached the end of the array 
            if  i==len(arr)-1: 
                return jump 
  
            # updating maxReach 
            maxReach=max(maxReach, i+arr[i])
  
            # we use a step to get to the current index 
            step-=1
  
            # If no further steps left 
            if  step==0: 
                # we must have used a jump 
                jump+=1 
                   
                #Check if the current index/position  or lesser index 
                #is the maximum reach point from the previous indexes 
                if i>=maxReach: 
                   return -1
  
                #re-initialize the steps to the amount 
                #of steps to reach maxReach from position i. 
                step=maxReach-i 
  
        return -1    
        
            
        

# if n <= 1, then return 0, because that is the destination
# If arr[0] == 0 then return -1 as answer (no jumps are possible)
# Now, Initialize maxrange and steps with arr[0], and jumps with 1 (as 1 jump will be required)
# Now, starting iteration from index 1, the above values are updated as follows:
# First we test whether we have reached the end of the array, in that case we just need to return the jump variable
# if (i == arr.length - 1) return jump;
# Next we update the maxrange. This is equal to the maximum of maxrange and i+arr[i](the number of steps we can take from the current position).
# maxrange = max(maxrange,i+arr[i]);
# We used up a step to get to the current index, so steps has to be decreased.
# step--;
# If no more steps are remaining (i.e. steps=0, then we must have used a jump. Therefore 
# increase jump. Since we know that it is possible to reach maxrange, we again initialize 
# the steps to the number of steps to reach maxReach from position i. But before re-initializing 
# step, we also check whether a step is becoming zero or negative. In this case, 
# It is not possible to reach further.
# if (step == 0) {
#     jump++;
#     if(i>=maxReach)
#       return -1;
#     step = maxReach - i;
# }
# Print the returned value

        
        
#         jumps =  jumps taken, this will be our answer
# maxrange = maximum range upto which we can jump
# steps = to store steps that we can take for a particular jump

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends