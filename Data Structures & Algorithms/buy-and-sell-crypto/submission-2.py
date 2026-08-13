class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            # profit = sell - buy
            profit = prices[i] - minBuy
            if profit > 0:
                # there was a profit
                bestProfit = max(bestProfit, profit)
            else:
                # BROKIE
                pass
        return bestProfit



        