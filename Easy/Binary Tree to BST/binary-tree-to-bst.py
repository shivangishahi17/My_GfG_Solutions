#User function Template for python3

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def inorder_bt(self, root):
        if root is None:
            return None
        self.inorder_bt(root.left)
        self.arr.append(root.data)
        self.inorder_bt(root.right)
    def inorder_bst(self, root, i):
        if root is None:
            return None
        self.inorder_bst(root.left, i)
        root.data=self.arr[i[0]]
        i[0]+=1
        self.inorder_bst(root.right, i)
        
    def binaryTreeToBST(self, root):
        # code here
        self.arr=[]
        self.inorder_bt(root)
        self.arr.sort()
        i=[0]
        self.inorder_bst(root, i)
        return root
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

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

def printInorder(root): 
    if root is None: 
        return
    printInorder(root.left) 
    print (root.data, end=' ')  
    printInorder(root.right) 

if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        Solution().binaryTreeToBST(root)
        printInorder(root)
        print()
# } Driver Code Ends