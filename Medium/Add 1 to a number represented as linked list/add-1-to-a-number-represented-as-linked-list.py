#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def reverse(self, head):
        curr=head
        prev=None
        
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            
        return prev
            
    def addOne(self,head):
        #Returns new head of linked List.
        carry=0
        curr1=self.reverse(head)
        curr=curr1
        prev=None
        
        while curr:
            sum=0
            if prev==None:
                sum=curr.data+carry+1
            else:
                sum=curr.data+carry
                
            carry=sum//10
            curr.data=(sum%10)
            prev=curr
            curr=curr.next
        
        if carry==1:
            new_node=Node(1)
            prev.next=new_node
            
        return self.reverse(curr1)   
            
        


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
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends