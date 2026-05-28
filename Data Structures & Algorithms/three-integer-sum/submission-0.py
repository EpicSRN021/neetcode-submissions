class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            num = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == num:
                    print(f' i = {i}, nums[left] = {nums[left]}, nums[right] = {nums[right]}, num = {num}')
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > num:
                    right -= 1
                else:
                    left += 1
        return list(res)
                
                




        