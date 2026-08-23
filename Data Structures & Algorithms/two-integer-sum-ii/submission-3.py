class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        low=0
        high=len(numbers)
        for x in range(len(numbers)):
            remainder=target-numbers[x]
            low=x+1
            high=len(numbers)-1
            while low<=high:
                mid=low+ (high-low)//2
                if numbers[mid]==remainder:
                    return [x+1,mid+1]
                elif numbers[mid]<remainder:
                    low=mid+1
                else:
                    high=mid-1
        return res