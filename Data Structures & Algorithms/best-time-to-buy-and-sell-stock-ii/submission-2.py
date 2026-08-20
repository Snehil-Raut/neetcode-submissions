class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0
        
        left=0
        right=left+1
        max_profit = 0

        while right < len(prices):
            profit_made = prices[right] - prices[left]

            if profit_made > 0:
                max_profit += profit_made
                left+=1
                right+=1
            else:
                left+=1
                right+=1
        
        return max_profit
