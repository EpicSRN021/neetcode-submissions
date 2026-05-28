class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = 101
        for i in prices:
            if i < low:
                low = i
                continue
            if i - low > res:
                res = i - low
        return res
        