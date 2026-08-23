class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxL=max(piles)
        start=1
        minK=float("inf")
        while start<=maxL:
            k=start + (maxL-start)//2
            sumP=0
            for p in piles:
                sumP+= math.ceil(p/k)
            if sumP<=h:
                minK=k
                maxL=k-1
            else:
                start=k+1
        return minK