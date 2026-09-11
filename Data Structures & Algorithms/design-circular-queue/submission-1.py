class Node:
    def __init__(self,prev,next,val):
        self.prev=prev
        self.next=next
        self.val=val

class MyCircularQueue:

    def __init__(self, k: int):
        self.cap=k
        self.left=Node(None,None,0)
        self.right=Node(self.left,None,0)
        self.left.next=self.right
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        insrt=Node(self.right.prev,self.right,value)
        self.right.prev.next=insrt
        self.right.prev=insrt
        self.cap-=1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next=self.left.next.next
        self.left.next.prev=self.left
        self.cap+=1
        return True

        
    
        

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.next.val
        

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.prev.val
        

    def isEmpty(self) -> bool:
        return True if self.left.next==self.right else False
        

    def isFull(self) -> bool:
        return True if self.cap==0 else False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()