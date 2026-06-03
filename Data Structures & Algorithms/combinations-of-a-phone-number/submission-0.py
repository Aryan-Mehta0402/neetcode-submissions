class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # n - 2
        maap = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
                ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
                ["t", "u", "v"], ["w", "x", "y", "z"]
            ]

        res = []
        sol = ""

        if digits == "":
            return []
        def bt(n, sol):
            if n == len(digits):
                res.append(sol)
                return
            
            for ch in maap[int(digits[n])-2]:
                sol += ch
                bt(n+1, sol)
                sol = sol[:-1]

        bt(0, sol)
        return res