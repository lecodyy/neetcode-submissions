class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        maxProfit = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            currentProfit = prices[i] - minBuy
            if currentProfit > 0:
                maxProfit = max(maxProfit, currentProfit)
            
        return maxProfit

        



        