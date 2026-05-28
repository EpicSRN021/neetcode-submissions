class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        m = 1
        for i in s:
            if i - 1 in s:
                continue
            temp = 1
            while True:
                i = i + 1
                if i not in s:
                    if temp > m:
                        m = temp
                    break
                temp += 1
        return m