class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for idx, i in enumerate(nums):
            if target - i in s:
                print(s)
                return sorted([s[target - i], idx])
            s[i] = idx
        