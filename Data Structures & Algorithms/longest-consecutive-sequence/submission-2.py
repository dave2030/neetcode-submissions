class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        maxS=0
        for x in nums:
            conseq=x

            while (conseq+1) in seen:
                conseq+=1
            maxS=max(maxS,conseq-x+1)
        return maxS
