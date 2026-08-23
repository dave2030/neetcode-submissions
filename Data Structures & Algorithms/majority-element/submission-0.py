class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check=len(nums)//2
        hMap={}
        for x in nums:
            hMap[x]=1+hMap.get(x,0)
            if hMap[x]>check:
                return x
        
        