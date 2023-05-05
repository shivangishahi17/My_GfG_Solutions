#User function Template for python3

from typing import List

class Solution:
    def reverse(self,st): 
        #code here
        if len(st)==1:
            return st
        temp=st[-1]
        st.pop()
        self.reverse(st)
            
        self.insertAtBottom(st, temp)
        return st
    
    def insertAtBottom(self, st, temp):
        if len(st)==0:
            st.append(temp)
        else:
            a=st[-1]
            st.pop()
            self.insertAtBottom(st, temp)
                    
            st.append(a)
            return st
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            ans=(ob.reverse(arr))
            for el in ans:
                print(el,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends