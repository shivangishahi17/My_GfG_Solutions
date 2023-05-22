#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        # slow_p=head
        # fast_p=head
        # #loop till fast_p doesn't reach end of linked list and fast_p.next is not None yani last lode pe nhi aa 
        # #jate
        # while fast_p and fast_p.next:
        #     slow_p=slow_p.next
        #     fast_p=fast_p.next.next
            
        #     if(slow_p==fast_p):
        #         return True
        # return False
        dict={}
        while head:
            if head not in dict:
                dict[head]=1
            else:
                return True
            head=head.next
        return False
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    #connects last node to node at position pos from begining.
    def loopHere(self,pos):
        if pos==0:
            return
        
        walk = self.head
        for i in range(1,pos):
            walk = walk.next
        
        self.tail.next = walk

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        
        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))
        
        LL.loopHere(int(input()))
        
        print(Solution().detectLoop(LL.head))
# } Driver Code Ends