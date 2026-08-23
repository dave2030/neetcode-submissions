class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total=0
        hMap={0:-1}
        for i,n in enumerate(nums):
            total+=n
            if total%k in hMap:
                if i - hMap[total%k]>1:
                    return True
            else:
                hMap[total%k]=i
        return False
