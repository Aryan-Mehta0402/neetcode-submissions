class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        ans = ""

        if len(digits) == 0:
            return []

        mapp = {2: "abc", 3: "def", 4: "ghi", 
                5: "jkl", 6: "mno", 7: "pqrs",
                8: "tuv", 9: "wxyz"}

        def rec(i, ans):
            if i == len(digits):
                res.append(ans)
                return
            
            for ch in mapp[int(digits[i])]:
                rec(i+1, ans + ch)
            
        rec(0, ans)
        return res