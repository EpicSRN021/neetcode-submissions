class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        temp = 0
        for i in nums:
            if temp + i < 0:
                if temp + i > res:
                    res = temp + i
                temp = 0
            elif temp + i < temp:
                if temp > res:
                    res = temp
                temp = temp + i
            else:
                if temp + i > res:
                    res = temp + i
                temp = temp + i
        return res
        