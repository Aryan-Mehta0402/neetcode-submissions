class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        MySet = set()
        for num in nums:
            if(num in MySet):
                return True
            else:
                MySet.add(num)
        return False
