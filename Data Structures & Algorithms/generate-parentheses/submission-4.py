class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # right count has to be always <= left and thats it
        res = []
        sol = ""

        def rec(l, r):
            nonlocal sol
            if l == n:
                ans = sol + ")"*(n-r)
                res.append(ans)
                return

            if r > l:
                return 

            sol += "("
            rec(l+1, r)
            sol = sol[:-1]

            sol += ")"
            rec(l, r+1)
            sol = sol[:-1]

        rec(0, 0)
        return res
            
