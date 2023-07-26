#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        charCount = dict()
        # initially setting c to "a"
        c = "a"
        # iterating over str1 and str2
        for i in range(len(str1)):
            # if str1[i] is a key in charCount
            if str1[i] in charCount:
                c = charCount[str1[i]]
                if c != str2[i]:
                    return False
            # if str2[i] is not a value in charCount
            elif str2[i] not in charCount.values():
                charCount[str1[i]] = str2[i]
            else:
                return False
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