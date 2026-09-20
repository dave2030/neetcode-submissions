class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for x in range(len(nums)):
            if x!=nums[x]:
                return x
