class Node:
    def __init__(self,data,prev=None,next=None):
        self.prev=prev
        self.next=next
        self.data=data
class Sll:
    def __init__(self):
        self.__head=None
        self.__size=0
    def size(self):
        return self.__size
    def isEmpty(self):
        return self.__size==0
    
    def append(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
        else:
            trav=self.__head
            while trav.next is not None:
              trav=trav.next
            trav.next=newNode
        self.__size+=1
    
    def __str__(self):
        l=[]
        trav=self.__head
        while trav is not None:
            l.append(str(trav.data))
            trav=trav.next
        return '--->'.join(l)
    
    def addFirst(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
        else:
            newNode.next=self.__head
            self.__head=newNode
        self.__size+=1

    def addAt(self,data,index):
        if (index<0 or index>self.size()-1):
            raise Exception("Index out of bound")
        
        elif(index==0):
            self.addFirst()

        elif(index==self.__size-1):
            self.append()
        i=0
        trav=self.__head
        while i!=index:
            i+=1
            trav=trav.next
        newNode=Node(data)
        newNode.next=trav.next
        trav.next=newNode
        self.__size+=1
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List Empty")
        else:
            temp=self.__head
            self.__head=temp.next
            del temp
        self.__size-=1
    def removeLast(self):
        if self.isEmpty():
            raise Exception("List Empty")
        elif (self.size==1):
            self.removeFirst()
        else:
            i=0
            trav=self.__head
            while i!=self.__size-2:
                i+=1
                trav=trav.next
                temp=trav.next
                trav.next=None
                del temp
            self.__size-=1

    def getHead(self):
        return self.__head
    
    def removeAt(self,index):
        if (index<0 or index>self.size()-1):
            raise Exception("Index out of bound")
        
        elif(index==0):
            self.removeFirst()

        elif(index==self.__size-1):
            self.removeLast()
        else:
            i=0
            trav=self.__head
            while(i!=index-1):
                i+=1
                trav=trav.next
            temp=trav.next
            trav.next=trav.next.next
            temp.next=None
            del temp
        self.__size-=1
    def mid(self):
        slow=self.__head
        fast=self.__head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    def search(self,element):
        i=0
        trav=self.__head
        while (trav.next is not None):
            trav=trav.next
            i+=1
            if(trav.data==element):
             return i
        return -1
    def reverse(self):
        prev=None
        curr=self.__head
        while curr is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.__head=prev
    
    def mergeTwoSorted(self, other):
        merged_list = Sll()
        trav1, trav2 = self.__head, other.__head
        while trav1 is not None and trav2 is not None:
            if trav1.data <= trav2.data:
                merged_list.append(trav1.data)
                trav1 = trav1.next
            else:
                merged_list.append(trav2.data)
                trav2 = trav2.next
        while trav1 is not None:
            merged_list.append(trav1.data)
            trav1 = trav1.next
        while trav2 is not None:
            merged_list.append(trav2.data)
            trav2 = trav2.next
        return merged_list
    
    def rotateByK(self, k):
        if self.isEmpty() or k == 0 or k % self.__size == 0:
            return
        
        k = k % self.__size  
        tail = self.__head
        new_tail = None
        count = 1
        
        
        while tail.next is not None:
            if count == self.__size - k:
                new_tail = tail
            tail = tail.next
            count += 1
        tail.next = self.__head
        self.__head = new_tail.next
        new_tail.next = None

    def splitByIndex(self, index):
        if index < 0 or index > self.__size:
            raise Exception("Index out of bound")
        
        if index == 0:
            second_list = Sll()
            second_list.__head = self.__head
            second_list.__size = self.__size
            self.__head = None
            self.__size = 0
            return self, second_list

        if index == self.__size:
            second_list = Sll()
            return self, second_list

        first_list = Sll()
        second_list = Sll()

        trav = self.__head
        first_list.__head = trav
        for i in range(1, index):
            trav = trav.next

        second_list.__head = trav.next
        trav.next = None

        first_list.__size = index
        second_list.__size = self.__size - index

        self.__head = None
        self.__size = 0

        return first_list, second_list
    def interleave(self, other):
        interleaved_list = Sll()
        trav1, trav2 = self.__head, other.__head

        while trav1 is not None or trav2 is not None:
            if trav1 is not None:
                interleaved_list.append(trav1.data)
                trav1 = trav1.next
            if trav2 is not None:
                interleaved_list.append(trav2.data)
                trav2 = trav2.next

        return interleaved_list
                                               


# Usage example
l=Sll()
print(l.size())
print(l.isEmpty())
l.append(1)
l.append(2)
print(l)
print(l.size())
l.addFirst(3)
print(l)
print(l.size())
l.addAt(3,1)
print(l)
print(l.size())
l.removeFirst()
print(l)
print(l.size())
l.removeLast()
print(l)
print(l.size())
l.append(5)
l.append(6)
l.append(7)
print(l)
l.removeAt(1)
print(l)
print(l.size())
print(l.mid())
print(l.search(5))
l.reverse()
l.append(9)
l.append(10)
l.append(11)
l.append(12)
print(l)

l2=Sll()
l2.append(3)
l2.append(4)
l2.append(8)
l2.append(9)
l2.append(89)

l3=Sll()
l3.append(1)
l3.append(2)
l3.append(3)
l3.append(4)
l3.append(5)

print(l)
print(l2)
print(l3)
print(l3.mergeTwoSorted(l2))

l.rotateByK(2)
print(l)
print('********')
print(l2)
print('********')
print(l2.splitByIndex(3))
print(l.interleave(l2))



        


    
    


    

    