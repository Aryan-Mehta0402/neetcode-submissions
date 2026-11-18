class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        m = len(nums) // 2
        L, R = nums[:m], nums[m:]
        L, R = self.sortArray(L), self.sortArray(R)
        nl, nr = len(L), len(R)
        l, r, i = 0, 0, 0
        sorted_arr = [0] * len(nums)

        while l < nl and r < nr:
            if L[l] < R[r]:
                sorted_arr[i] = L[l]
                l += 1
            else:
                sorted_arr[i] = R[r]
                r += 1
            i += 1

        while l < nl:
            sorted_arr[i] = L[l]
            l+=1
            i+=1
        
        while r < nr:
            sorted_arr[i] = R[r]
            r+=1
            i+=1

        return sorted_arr