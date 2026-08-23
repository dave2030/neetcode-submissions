class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val=prices[0]
        maxP=0
        for x in range(1,len(prices)):
            if prices[x]>val:
                maxP=max(maxP,prices[x]-val)
            else:
                val=prices[x]
        return maxP