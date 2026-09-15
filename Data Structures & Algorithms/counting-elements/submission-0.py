class Solution:
    def countElements(self, arr: List[int]) -> int:
        count=0
        for x in range(len(arr)-1):
            if arr[x]==arr[x+1]-1:
                count+=1
        
        return count
