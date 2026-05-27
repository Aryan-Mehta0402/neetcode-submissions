class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l+(r-l)//2

            if t == nums[m]:
                return m
            if t > nums[m] and t > nums[r]:
                if nums[m] > nums[r]:
                    l = m+1
                else:
                    r = m-1
            elif nums[l] <= nums[m] and nums[l] <= t < nums[m]:
                left = l
                right = m-1
                while(left<=right):
                    mid = left+(right-left)//2
                    if t == nums[mid]:
                        return mid
                    elif t > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
                return -1                        
            elif nums[m] <= nums[r] and nums[m] < t <= nums[r]:
                left = m
                right = r
                while(left<=right):
                    mid = left+(right-left)//2
                    if t == nums[mid]:
                        return mid
                    elif t > nums[mid]:
                        left = mid+1
                    else:
                        right = mid-1
                return -1
            else:
                if nums[m] < nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1