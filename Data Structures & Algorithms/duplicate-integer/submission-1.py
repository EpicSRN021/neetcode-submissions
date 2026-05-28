class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.track = {}
        for i in nums:
            if i not in self.track:
                self.track[i] = 1
            else:
                return True
        return False
        