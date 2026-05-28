class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf = []
        pref = []
        prod = 1
        for num in nums:
            pref.append(prod)
            prod = num * prod
        rev = nums[::-1]
        prod = 1
        for num in rev:
            suf.append(prod)
            prod = num * prod
        suf = suf[::-1]
        res = []
        print(pref)
        print(suf)
        for num in range(len(nums)):
            res.append(pref[num] * suf[num])
        return res
