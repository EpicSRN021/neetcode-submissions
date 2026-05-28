class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key in freq:
            bucket[freq[key]].append(key)
        res = []
        for i in range(len(nums), -1 ,-1):
            for num in bucket[i]:
                if len(res) == k:
                    return res
                res.append(num)
        return res
        


            
        