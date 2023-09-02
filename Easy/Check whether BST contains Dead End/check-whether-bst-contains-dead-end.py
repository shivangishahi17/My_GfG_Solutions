# Your task is to complete this function
# function should return true/false or 1/0
def storeNodes(root, leafNodes, allNodes):
    if root is None:
        return
    
    allNodes.add(root.data)
    if root.left is None and root.right is None:
        leafNodes.add(root.data)
    
    storeNodes(root.left, leafNodes, allNodes)
    storeNodes(root.right, leafNodes, allNodes)
    
def isdeadEnd(root):
    # Code here
    allNodes=set()
    leafNodes=set()
    
    if root is None:
        return False
    
    allNodes.add(0)
    storeNodes(root, leafNodes, allNodes) 
    
    for i in leafNodes:
        if i-1 in allNodes and i+1 in allNodes:
            return True
    return False
 
    
 
   
    
    
        
        


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        elif root.data == node.data:
            return
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def traverseInorder(root):
    if root is not None:
        traverseInorder(root.left)
        print(root.data, end=" ")
        traverseInorder(root.right)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        root = None
        for j in arr:
            if root is None:
                root = Node(j)
            else:
                insert(root, Node(j))
        if isdeadEnd(root):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends