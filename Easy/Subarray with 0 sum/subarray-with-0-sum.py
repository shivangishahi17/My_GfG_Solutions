#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        #The idea is to iterate through the array and for every element arr[i], calculate the sum of elements 
        # from 0 to i (this can simply be done as sum += arr[i]). If the current sum has been seen before, then 
        # there is a zero-sum array. Hashing is used to store the sum values so that sum can be stored quickly 
        # and find out whether the current sum is seen before or not.
        sum=0
        s=set()
        for i in range(n):
            sum+=arr[i]
            if sum==0 or sum in s:
                return True
            s.add(sum)
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends