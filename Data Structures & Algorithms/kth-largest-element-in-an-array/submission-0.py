import heapq as hp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maintain a min heap of size k
        arr = []

        for i in range(len(nums)):
            hp.heappush(arr, nums[i])
            if len(arr) > k:
                hp.heappop(arr)
        return arr[0]