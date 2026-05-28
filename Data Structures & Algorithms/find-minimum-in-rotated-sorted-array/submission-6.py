class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right and right - left > 1:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[left]:
                right = mid
            elif nums[left] <= nums[right]:
                return nums[left]
        return min(nums[left], nums[right])