class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for num in prices[1:]:
            max_profit = max(max_profit, num-min_price)
            min_price = min(min_price, num)
        return max_profit


        