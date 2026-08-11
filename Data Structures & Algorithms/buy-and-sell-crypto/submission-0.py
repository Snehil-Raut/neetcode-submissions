class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i=0

        while i < (len(prices)):
           
            j=i+1
            
            while j < len(prices):
                
                made_profit = prices[j] - prices[i]
              
                if made_profit <= 0:
                    j += 1
                elif(made_profit > 0):
                    profit = max(profit, made_profit)

                    j+=1
            i+=1
                
        return profit

        