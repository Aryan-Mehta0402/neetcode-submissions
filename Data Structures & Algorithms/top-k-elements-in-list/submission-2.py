import heapq as hp
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = Counter(nums)
        hq = []
        ans = []

        for ke, v in ctr.items():
            hq.append((-v, ke))

        hp.heapify(hq)
        for i in range(k):
            minn = hp.heappop(hq)
            ans.append(minn[1])

        return ans

