class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        count = 0
        while count < index:
            current = current.next
            count += 1
        return current.val
    
    def addAtHead(self, val: int) -> None:
        add = ListNode(val)
        self.head, add.next = add, self.head 
        self.length += 1
        
    def addAtTail(self, val: int) -> None:
        add = ListNode(val)
        if not self.head:
            self.head = add
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next =add
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length: 
            self.addAtTail(val)
            return
        add = ListNode(val)
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
        add.next , current.next = current.next, add
        self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        count = 0
        while count < index - 1:
            current = current.next
            count += 1
        current.next = current.next.next
        self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
