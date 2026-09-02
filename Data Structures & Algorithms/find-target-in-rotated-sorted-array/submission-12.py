class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l
        l, r = 0, len(nums) - 1

        if t > nums[r]:
            r = pivot - 1
            while l <= r:
                m = (l+r)//2
                if nums[m] == t:
                    return m
                elif nums[m] > t:
                    r = m - 1
                else:
                    l = m + 1
            return -1
        else:
            l = pivot
            while l <= r:
                m = (l+r)//2
                if nums[m] == t:
                    return m
                elif nums[m] > t:
                    r = m - 1
                else:
                    l = m + 1
            return -1
