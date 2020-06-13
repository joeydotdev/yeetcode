"""
max heap based off # of instances a character is seen in str
"""
from heapq import *
import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = collections.Counter(s)
        l = []
        result = []
        heapify(l)
        for k, v in freq.items():
            heappush(l, (-v, k))
        
        for _ in range(len(l)):
            c, v = heappop(l)
            for i in range(-v):
                result.append(c)

        return ''.join(result)