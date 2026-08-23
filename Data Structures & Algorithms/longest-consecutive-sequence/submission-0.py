class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cSet=set(nums)
        maxC=0
        for x in range(len(nums)):
            c=1
            prev=nums[x]-1
            while prev in cSet:
                c+=1
                prev-=1
            maxC=max(maxC,c)
        return maxC
        