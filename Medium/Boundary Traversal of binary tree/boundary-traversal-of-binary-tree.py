#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def leftTree(self, root, ans):
        if root is None:
            return
        if root.left:
            ans.append(root.data)
            self.leftTree(root.left, ans)
        elif root.right:
            ans.append(root.data)
            self.leftTree(root.right, ans)
    def leafNode(self, root, ans):
        if root is None:
            return
        self.leafNode(root.left, ans)
        if root.left==None and root.right==None:
            ans.append(root.data)
        self.leafNode(root.right, ans)
    
    def rightTree(self, root, ans):
        if root is None:
            return
        if root.right:
            self.rightTree(root.right, ans)
            ans.append(root.data)
        elif root.left:
            self.rightTree(root.left, ans)
            ans.append(root.data)
    def printBoundaryView(self, root):
        # Code here
        ans = []
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.data]
        ans.append(root.data)
        self.leftTree(root.left, ans)
        self.leafNode(root, ans)
        self.rightTree(root.right, ans)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends