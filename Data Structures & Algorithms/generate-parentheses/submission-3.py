class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(op, cl, sol):
            if op == n:
                res.append(sol + ")" * (n - cl))
                return

            if op == cl:
                backtrack(op + 1, cl, sol + "(")
                return

            backtrack(op + 1, cl, sol + "(")
            backtrack(op, cl + 1, sol + ")")

        backtrack(1, 0, "(")
        return res

            
