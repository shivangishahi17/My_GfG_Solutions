'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        start=0
        extraFuel=0
        requiredFuel=0
        for i in range(start, n):
            extraFuel+=lis[i][0]-lis[i][1]
            if extraFuel<0:
                requiredFuel+=extraFuel
                # because we are starting again from new position
                extraFuel=0
                start=i+1
        return start if extraFuel+requiredFuel>=0 else -1
        
        
       
        
         

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(Solution().tour(lis, n))
    # Contributed by: Harshit Sidhwa
# } Driver Code Ends