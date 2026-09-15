class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter=set(arr)
        count=0
        for x in arr:
            if (x+1) in counter:
                count+=1
        
        return count
