class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0 
        for sell in prices : 
            currentprofit = sell - minBuy 
            maxP = max(currentprofit,maxP)
            minBuy = min(minBuy, sell)
        return maxP
            
                


        