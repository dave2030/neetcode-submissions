import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        res=1
        while low<=high:
            k=(low+high)//2
            hours=0
            for pile in piles:
                hours += math.ceil(pile/k)
            if hours>h:
                low=k+1
            else:
                high=k-1
                
        return low

        
