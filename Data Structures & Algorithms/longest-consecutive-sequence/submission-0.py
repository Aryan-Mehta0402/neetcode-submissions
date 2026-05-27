class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        HashMap = {}
        for i in range(len(nums)):
            HashMap[nums[i]] = 1 + HashMap.get(nums[i], 0)
        
        arr = []
        for key in HashMap:
            leng = key - 1
            if HashMap.get(leng,0) == 0:
                arr.append(key)
        
        ml = 0
        for e in arr:
            length = 0
            j = e
            while HashMap.get(j,0) != 0:
                length += 1
                j += 1

            if length > ml:
                ml = length
        return ml
        
