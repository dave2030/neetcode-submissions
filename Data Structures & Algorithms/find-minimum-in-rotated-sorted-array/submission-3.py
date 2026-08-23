class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        res=float("inf")
        if nums[low]<nums[high]:
            return nums[low]
        while low<=high:
            mid=low + (high-low)//2
            res=min(res,nums[mid])
            if nums[mid]<=nums[high]:
                high=mid-1
            else:
                low=mid+1
        return res