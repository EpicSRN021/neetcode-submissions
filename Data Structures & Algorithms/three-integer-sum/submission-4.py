class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]].append(i)
            else:
                mp[nums[i]] = [i]
        s = set()
        res = []
        print(mp)
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if i1 == i2:
                    continue
                curr = num1 + num2
                diff = curr * -1
                tempi = None
                if diff in mp:
                    if diff == num2 and diff == num1:
                        if len(mp[diff]) <= 2:
                            continue
                        for i in mp[diff]:
                            if i != i1 and i!= i2:
                                tempi = i
                    elif diff == num2:
                        if len(mp[diff]) == 1:
                            continue
                        for i in mp[diff]:
                            if i!= i2:
                                tempi = i
                    elif diff == num1:
                        if len(mp[diff]) == 1:
                            continue
                        for i in mp[diff]:
                            if i!= i1:
                                tempi = i
                    tempi = mp[diff][0]
                    if (tuple(sorted([num1, num2, diff]))) in s:
                        continue
                    s.add(tuple(sorted([num1, num2, diff])))
                    res.append([num1, num2, diff])
        return res

