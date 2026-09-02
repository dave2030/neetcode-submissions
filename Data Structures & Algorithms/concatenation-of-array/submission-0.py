class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0 for x in range(len(nums)*2)]
        for x in range(len(nums)):
            ans[x]=nums[x]
            ans[x+len(nums)]=nums[x]
        return ans