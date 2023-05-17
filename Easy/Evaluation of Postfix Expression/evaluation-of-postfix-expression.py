#User function Template for python3

class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        #code here
        stack=[]
        result=0
        for i in S:
            if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                stack.append(int(i))
            else:
                op1=stack.pop()
                op2=stack.pop()
                
                if i=='+':
                    result=op2+op1
                elif i=='-':
                    result=op2-op1
                elif i=='*':
                    result=op2*op1
                elif i=='/':
                    result=op2//op1
                stack.append(result)
        return stack[-1]
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends