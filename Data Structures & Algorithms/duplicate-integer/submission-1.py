class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        print(nums)
        if len(nums) == 0 :
            return False
        prev = nums[0]
        for i in range(len(nums)-1):
            if(nums[i+1] == prev):
                return True
            else:
                prev = nums[i+1]
        return False