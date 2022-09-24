class Node():
    def __init__(self,val):
        self.val=val
        self.next=None
    
class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.length=0
        

    def get(self, index):
        
        if index < 0 or index >= self.length:
            return -1
        
        if self.head is None:
            return -1
        
        curr=self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=Node(val)
        new_node.next=self.head
        self.head=new_node
        
        self.length += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        
        else:
            n=self.head
            while n.next is not None:
                n=n.next
            n.next=new_node
        self.length += 1

    def addAtIndex(self, index, val):
        if index > self.length:
            return
        
        new_node = Node(val)
        
        if index <= 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

        self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return

        n = self.head
        if index == 0:
            self.head = n.next
        else:
            for i in range(index - 1):
                n = n.next
            n.next = n.next.next

        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)