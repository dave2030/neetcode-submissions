class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=collections.defaultdict(list)
        for x in nums:
            res[x]=1+res.get(x,0)
        h=[]
        for x,y in res.items():
            heapq.heappush(h,(-y,x))
        result=[]
        while k>0:
            _,e=heapq.heappop(h)
            result.append(e)
            k-=1
        return result


        return sortedL