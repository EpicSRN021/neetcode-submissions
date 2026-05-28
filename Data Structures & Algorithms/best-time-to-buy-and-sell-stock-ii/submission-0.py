class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        curr = prices[0]
        for price in prices:
            if price <= curr:
                curr = price
            else:
                total += price - curr
                curr = price
        return total