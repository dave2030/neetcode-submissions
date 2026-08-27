class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minP=prices[0]

        for p in prices:
            maxProfit=max(maxProfit, p-minP)
            minP=min(minP,p)
        return maxProfit