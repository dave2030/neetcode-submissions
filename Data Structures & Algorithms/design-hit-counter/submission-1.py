class HitCounter:

    def __init__(self):
        self.hitCounter=collections.deque()

    def hit(self, timestamp: int) -> None:
        self.hitCounter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        while self.hitCounter:
            diff = timestamp - self.hitCounter[0]
            if diff >= 300:
                self.hitCounter.popleft()
            else:
                break
        return len(self.hitCounter)




# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
