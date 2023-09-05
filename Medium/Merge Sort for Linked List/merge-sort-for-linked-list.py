#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        # Base condition
        if head is None or head.next is None:
            return head
       
        curr=head
        slow=head
        fast= head 
        while fast and fast.next:
            curr=slow
            slow=slow.next
            fast=fast.next.next
        
        mid=slow
        # 
        curr.next=None
        
        left=self.mergeSort(head)
        right=self.mergeSort(mid)
        return self.merge(left, right)
        
    def merge(self, left, right):
        dummy=Node(0)
        prev=dummy
        while left and right:
            if left.data<=right.data:
                prev.next=left
                left=left.next
            else:
                prev.next=right
                right=right.next
            prev=prev.next
        if left:
            prev.next=left
        if right:
            prev.next=right
        
        return dummy.next

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list

        printList(Solution().mergeSort(p.head))

# } Driver Code Ends