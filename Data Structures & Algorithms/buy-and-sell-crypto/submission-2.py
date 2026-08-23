class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        p1=p2=0
        minPrice=float("inf")
        while p1<len(prices):
            minPrice=min(minPrice,prices[p1])
            profit=max(profit,prices[p1]-minPrice)
            p1+=1
        return profit
            
