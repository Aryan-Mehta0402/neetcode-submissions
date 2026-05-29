import heapq as hp

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k   

        hp.heapify(self.nums)    

        while len(nums) > k:
            hp.heappop(self.nums)

    def add(self, val: int) -> int:
        hp.heappush(self.nums, val)

        if len(self.nums) > self.k:
            hp.heappop(self.nums)
        return self.nums[0]
        
