import heapq as hp
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        nums = sorted(set(nums), key=counts.get, reverse=True)
        ans = [nums[0]]
        l = 1
        for i in range(1, len(nums)):
            if l < k:
                if nums[i] != ans[-1]:
                    ans.append(nums[i])
                    l += 1
            else:
                return ans
        return ans

