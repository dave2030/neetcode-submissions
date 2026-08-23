class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount=0
        hSet=set(nums)
        p1=0
        while p1<len(nums):
            if nums[p1]-1 not in hSet:
                count=1
                while nums[p1] + count in hSet:
                    count+=1
                maxCount=max(maxCount,count)
            p1+=1
        return maxCount



            