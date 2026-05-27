class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort then numbers inplace
        nums.sort()
        ans = []
        for i in range(len(nums)):
            target = -1*nums[i]
            index_t = i

            l, r = 0, len(nums) - 1

            sum = 0
            while l < r:
                sum = nums[l] + nums[r]

                if l == index_t:
                    l+=1
                    continue
                if r == index_t:
                    r-=1
                    continue

                if sum < target:
                    l+=1
                elif sum > target:
                    r-=1
                else:
                    l1 = [nums[l], nums[r], -1*target]
                    l1.sort()
                    ans.append(l1)
                    l+=1
                    r-=1
        ans = list(set(tuple(x) for x in ans))                    
        return ans



