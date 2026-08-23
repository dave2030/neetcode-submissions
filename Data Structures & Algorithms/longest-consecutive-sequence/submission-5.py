class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        count=0
        maxC=0
        for x in s:
            if x-1 not in s:
                count=1
                while x+count in s:
                    count+=1
                maxC=max(maxC,count)
        return maxC