class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for ind,val in enumerate(nums):
            if target-val in dct:
                return [dct[target-val],ind]
            dct[val]=ind
        return []
        