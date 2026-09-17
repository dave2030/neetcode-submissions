class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cur=0
        dct={0:1}
        res=0
        for x in nums:
            cur+=x
            remain = cur % k 
            if remain in dct:
                res+=dct[remain]
            dct[remain]=1 + dct.get(remain,0)
        print(dct.items())
        return res

