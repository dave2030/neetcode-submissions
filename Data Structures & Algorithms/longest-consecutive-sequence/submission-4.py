class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxCount=0
        hSet=set(nums)
        for x in nums:
            if x - 1 not in nums:
                count=1
                while x+count in hSet:
                    count+=1
                maxCount=max(maxCount,count)
        return maxCount



            