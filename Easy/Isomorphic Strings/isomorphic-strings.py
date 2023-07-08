#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        n=len(str1)
        m=len(str2)
        
        if m!=n:
            return False
            
        dict1={}
        dict2={}
        
        for i in range(n):
            c1=str1[i]
            c2=str2[i]
            
            if ((c1 in dict1 and dict1[c1]!=c2) or (c2 in dict2 and dict2[c2]!=c1)):
                return False
            dict1[c1]=c2
            dict2[c2]=c1
        return True
        

            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends