class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        for ind,val in enumerate(nums):
            if target-val in dct:
                return [dct[target-val],ind]
            else:
                dct[val]=ind
        return [-1,-1]
            