class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = [-1, float('inf')] # i, price
        sell = [-1, -1] # i, price
        for i, p in enumerate(prices):
            if p < buy[1]:
                buy[0] = i
                buy[1] = p
            
            else:
                sell[0] = i 
                sell[1] = p
                profit = max(profit, sell[1] - buy[1])

        return profit