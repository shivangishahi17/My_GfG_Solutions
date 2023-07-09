#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        res=""
        ans=len(s)
        dic={}

        for i in p:
            if i in dic:
                dic[i]=dic[i]+1
            else: 
                dic[i]=1
        
        count=len(dic)
        i=0
        start=0
        j=0
        while j<len(s):
            if s[j] in dic: 
                dic[s[j]]=dic[s[j]]-1
            else: 
                dic[s[j]]=-1
            if dic[s[j]]==0: 
                count=count-1
            if count==0:
                while count==0:
                    if ans>j-i+1:
                        ans=j-i+1
                        start=i
                    if s[i] in dic:
                        dic[s[i]]=dic[s[i]]+1
                    if dic[s[i]]>0:
                        count=count+1
                    i=i+1
            j=j+1

        if ans==len(s): 
            return "-1"
        else: 
            return s[start:start+ans]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        print(ob.smallestWindow(s,p))
# } Driver Code Ends