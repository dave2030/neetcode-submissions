class MinStack:

    def __init__(self):
        self.main=[]
        self.dummy=[]

    def push(self, val: int) -> None:
        self.main.append(val)
        val=min(val,self.dummy[-1]) if self.dummy else val
        self.dummy.append(val)
        

    def pop(self) -> None:
        self.main.pop()
        self.dummy.pop()

    def top(self) -> int:
        return self.main[-1]

    def getMin(self) -> int:
        return self.dummy[-1]
