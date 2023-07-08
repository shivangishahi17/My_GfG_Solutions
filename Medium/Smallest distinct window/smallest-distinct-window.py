#User function Template for python3
from collections import defaultdict
class Solution:
    def findSubString(self, str):
        # Your code goes here
        s=set() #(A,B,C)
        for ch in str:
            s.add(ch)
        
        distinctChar=len(s)
        dict=defaultdict(int)
        start=0
        minLen=len(str)
        
        for end in range(len(str)):
            dict[str[end]]+=1
            if len(dict)==distinctChar:
                while dict[str[start]]>1:
                    dict[str[start]]-=1
                    start+=1
                minLen=min(minLen, end-start+1)
        return minLen
        
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	str = input()
    	ob=Solution()
    	print(ob.findSubString(str))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends