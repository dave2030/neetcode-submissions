class MyHashMap:

    def __init__(self):
        self.hMap={}

    def put(self, key: int, value: int) -> None:
        self.hMap[key]=value
            

    def get(self, key: int) -> int:
        return self.hMap[key] if key in self.hMap else -1
        

    def remove(self, key: int) -> None:
        del self.hMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)