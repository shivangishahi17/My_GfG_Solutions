#User function Template for python3
import math
class Solution:
    def divide(self, a, b):
        #code here
        dividend=abs(a)
        divisor=abs(b)
        c=0
        p=math.floor(math.log2(dividend))+1
        
        while(divisor<=dividend):
            if((divisor<<p)<=dividend):
                c+=1<<p
                dividend-=(divisor<<p)
            p-=1
        
        if(a<0 and b>0) or (a>0 and b<0):
            return -c
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        inp = list(map(int,input().split())) 
        
        a=inp[0]
        b=inp[1]
        
        ob=Solution()
        
        print(ob.divide(a,b))
        
# } Driver Code Ends