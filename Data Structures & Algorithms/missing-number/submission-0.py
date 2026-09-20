class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for x in range(len(nums)):
            if x!=nums[x]:
                return x
            