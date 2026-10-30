import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        
        prev = None
        res = ""
        heap = []
        for c in freq:
            heap.append((-freq[c], c))
        heapq.heapify(heap)

        while heap:
            cur = heapq.heappop(heap)
            count, c = cur
            count += 1
            res += c
            if prev is not None:
                heapq.heappush(heap, prev)
            if count != 0:
                prev = (count, c)
            else:
                prev = None
        if prev is not None:
            return ""
        return res

            


        