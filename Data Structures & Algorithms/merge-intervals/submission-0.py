class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        curr = intervals[0]
        res = []
        nums = intervals
        for i in range(1, len(nums)):
            if curr[1] < nums[i][0]:
                res.append(curr)
                curr = nums[i]
            if curr[1] >= nums[i][0]:
                curr = [curr[0], max(curr[1], nums[i][1])]
        res.append(curr)
        return res
            
        
