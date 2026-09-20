class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for x in range(n):
            if x!=nums[x]:
                return x
        return n