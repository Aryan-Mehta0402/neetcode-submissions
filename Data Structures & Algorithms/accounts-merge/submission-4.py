from collections import defaultdict

class Solution:
    def accountsMerge(self, acc: List[List[str]]) -> List[List[str]]:
        par = {}  # email -> account index
        n = len(acc)

        # Initially, every account is its own parent
        node_parents = [x for x in range(n)]

        def find(x):
            while x != node_parents[x]:
                node_parents[x] = node_parents[node_parents[x]]
                x = node_parents[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                node_parents[py] = px

        # Decide which accounts/groups to merge
        for i in range(n):
            k = len(acc[i])

            for j in range(1, k):
                email = acc[i][j]

                if email in par:
                    union(i, par[email])
                else:
                    par[email] = i

        # Map root account -> all emails belonging to that group
        M = defaultdict(list)

        for email, account in par.items():
            root = find(account)
            M[root].append(email)

        # Construct answer
        ans = []

        for root, emails in M.items():
            emails.sort()
            ans.append([acc[root][0]] + emails)

        return ans

