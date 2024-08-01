# leetcode id-deepali0402
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:

    def __init__(self):
        self.head=Node()
        

    def get(self, index: int) -> int:
        curr=self.head
        for i in range(index+1):
            if curr:
                curr=curr.next
            else:
                return -1
        return curr.val if curr else -1


        

    def addAtHead(self, val: int) -> None:
        newnode=Node(val,self.head.next)
        self.head.next=newnode
        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        curr=self.head
        for i in range(index):
            if curr.next:
                curr=curr.next
            else:
                return
        newnode=Node(val,curr.next)
        curr.next=newnode
        

    def deleteAtIndex(self, index: int) -> None:
        curr=self.head
        for i in range(index):
            if curr.next:
                curr=curr.next
            else:
                return
        if curr.next:
            curr.next=curr.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)