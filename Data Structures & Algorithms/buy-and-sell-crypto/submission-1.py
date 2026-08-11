class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy=0
        sell = buy+1

        for i in range(sell, len(prices)):
            if prices[sell]  > prices[buy]:
                made_profit = prices[sell] - prices[buy]
                profit = max(made_profit, profit)
            else:
                buy=sell
            sell+=1
        return profit


        