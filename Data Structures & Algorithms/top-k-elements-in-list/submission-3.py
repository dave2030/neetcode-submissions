class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap={}
        heap=[]
        for x in nums:
            hMap[x]=hMap.get(x,0)+1
        for key,v in hMap.items():
            heapq.heappush(heap,(-v,key))
        
        res=[]
        while len(res)!=k and heap:
            print(heap)
            _,val=heapq.heappop(heap)
            res.append(val)
        return res



