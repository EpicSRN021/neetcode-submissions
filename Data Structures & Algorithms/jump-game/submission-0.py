class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums = nums[::-1]
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(1, len(nums)):
            for j in range(1, nums[i]+1):
                if dp[i-j] == True:
                    dp[i] = True
                    break
        return dp[-1]
                
                