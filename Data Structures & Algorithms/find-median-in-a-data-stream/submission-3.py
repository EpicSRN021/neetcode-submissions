class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        self.even = True
    def addNum(self, num: int) -> None:
        if not self.lower:
            heapq.heappush(self.lower, -num)
        elif not self.upper:
            if num < -self.lower[0]:
                temp = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, temp)
                heapq.heappush(self.lower, -num)
            else:
                heapq.heappush(self.upper, num)
        elif len(self.lower) == len(self.upper):
            if num <= -self.lower[0]:
                heapq.heappush(self.lower, -num)
            else:
                heapq.heappush(self.upper, num)
                temp = heapq.heappop(self.upper)
                heapq.heappush(self.lower, -temp)
        else:
            if num >= self.upper[0]:
                heapq.heappush(self.upper, num)
            else:
                heapq.heappush(self.lower, -num)
                temp = -heapq.heappop(self.lower)
                heapq.heappush(self.upper, temp)
        self.even = not self.even



    def findMedian(self) -> float:
        if self.even:
            return float((-self.lower[0] + self.upper[0])/2)
        else:
            return float(-self.lower[0])
        