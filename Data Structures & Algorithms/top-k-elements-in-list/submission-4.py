class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets=[[] for x in range(len(nums))]
        count={}
        for x in nums:
            count[x]= 1 + count.get(x,0)
        for x in count:
            buckets[count[x]-1].append(x)
        res=[]
        for x in range(len(buckets)-1,-1,-1):
            for y in buckets[x]:
                if len(res)<k:
                    res.append(y)
                else:
                    return res
        return res




