class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        zero_i = None
        product = 1
        for idx, i in enumerate(nums):
            if i == 0:
                zeros += 1
                zero_i = idx
                continue
            product *= i
        if zeros > 1:
            return len(nums) * [0]
        if zero_i is not None:
            final = len(nums) * [0]
            final[zero_i] = product
            return final
        final = len(nums) * [product]
        for idx, i in enumerate(nums):
            final[idx] = int(product/i)
        return final
        