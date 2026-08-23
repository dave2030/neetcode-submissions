class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        h=[]
        res=[]
        for x in nums:
            dct[x]=dct.get(x,0)+1
        for key,val in dct.items():
            heapq.heappush(h,(-val,key))
        while k>0:
            _,v=heapq.heappop(h)
            res.append(v)
            k-=1
        return res