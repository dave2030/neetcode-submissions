class MinStack:

    def __init__(self):
        self.ms=[]
        self.st=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ms: self.ms.append(val)
        else: self.ms.append(min(val,self.ms[-1]))

    def pop(self) -> None:
        self.ms.pop()
        self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.ms[-1]
