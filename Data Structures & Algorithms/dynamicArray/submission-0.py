class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap=capacity
        self.arr=[0] * self.cap
        self.length=0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i]=n

    def pushback(self, n: int) -> None:
        if self.length==self.cap:
            self.resize()
        self.arr[self.length]=n
        self.length+=1

    def popback(self) -> int:
        self.length-=1
        return self.arr[self.length]

    def resize(self) -> None:
        self.cap*=2
        newArr = [0] * self.cap
        for i,v in enumerate(self.arr):
            newArr[i]=v
        self.arr=newArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.cap
