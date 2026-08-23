class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        minP=float("inf")
        for x in range(len(prices)):
            if prices[x]<minP:
                minP=prices[x]
            maxP=max(maxP,prices[x]-minP)
        return maxP