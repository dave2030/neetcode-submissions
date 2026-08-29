class HitCounter:

    def __init__(self):
        self.hitCounter=[]

    def hit(self, timestamp: int) -> None:
        self.hitCounter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        if self.hitCounter:
            while self.hitCounter and timestamp - self.hitCounter[0] >0:
                if timestamp -self.hitCounter[0] >= 300:
                    del self.hitCounter[0]
                else:
                    break
        return len(self.hitCounter)




# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
