import heapq as hp
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        hq = []
        ans = []

        for ke, v in ctr.items():
            hp.heappush(hq, (v, ke))
            if len(hq) > k:
                hp.heappop(hq)

        return [num for freq, num in hq]

