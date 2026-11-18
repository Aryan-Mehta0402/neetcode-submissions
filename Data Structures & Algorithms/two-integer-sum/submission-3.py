class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store all numbers in a dict which retains its index
        # then loop thru the set and search for complement in O(1)

        mapp = defaultdict(int)
        for i in range(len(nums)):
            mapp[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in mapp:
                if  i == mapp[target - nums[i]]:
                    continue
                return sorted([i, mapp[target - nums[i]]])

