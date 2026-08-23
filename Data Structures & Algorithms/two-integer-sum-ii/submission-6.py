class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        low=0
        high=len(numbers)-1
        while low<high:
            remainder=numbers[low]+numbers[high]
            if remainder==target:
                return [low+1,high+1]
            elif remainder>target:
                high-=1
            elif remainder<target:
                low+=1
        return [low+1,high+1]
        

            
  
            
