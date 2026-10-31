class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        
        profit=0

        while buy < len(prices):
            sell= buy+1
            while sell < len(prices):
                profit_made = prices[sell] - prices[buy]
                if profit_made > 0:
                    profit = max(profit, profit_made)
                    sell+=1
                else:
                    sell +=1
            
            buy+=1

        return profit



            




        