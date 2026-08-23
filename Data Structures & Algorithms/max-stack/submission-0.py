class MaxStack:

    def __init__(self):
        self.maxStack=[]
        self.stack=[]
        self.idx=0
        self.removed=set()
        

    def push(self, x: int) -> None:
        heapq.heappush(self.maxStack,(-x,-self.idx))
        self.stack.append((x,self.idx))
        self.idx+=1

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        num,idx=self.stack.pop()
        self.removed.add(idx)
        return num

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:
            self.stack.pop()
        return self.stack[-1][0]

    def peekMax(self) -> int:
        while self.maxStack and -self.maxStack[0][1] in self.removed:
            heapq.heappop(self.maxStack)
        return -self.maxStack[0][0]
        

    def popMax(self) -> int:
        while self.maxStack and -self.maxStack[0][1] in self.removed:
            heapq.heappop(self.maxStack)
        num,idx=heapq.heappop(self.maxStack)
        self.removed.add(-idx)
        return -num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
