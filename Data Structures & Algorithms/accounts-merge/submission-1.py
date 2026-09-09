from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # if an edge with same name and email id exist then there trees 
        # should be merged, but before that we need to sort? no
        # we iterate twice first to check if any edge is shared
        # adn 2nd time to add them as a tree

        M = defaultdict(set) # makes the forest
        pairs = set()
        n = len(accounts)
        name_map = defaultdict(set) # to keep list of equivalent names
        count = 0 # if names appear multiple times then we need to make diff keys

        for i in range(n):
            original_name = accounts[i][0]
            k = len(accounts[i])

            merge_names = set()

            # Find all trees that this account connects to
            for j in range(1, k):
                email = accounts[i][j]

                for nm in name_map[original_name]:
                    if (nm, email) in pairs:
                        merge_names.add(nm)

            # No existing tree -> create a new tree
            if len(merge_names) == 0:
                name = original_name + "$" * count
                name_map[original_name].add(name)
                count += 1

                for j in range(1, k):
                    M[name].add(accounts[i][j])
                    pairs.add((name, accounts[i][j]))

            # Existing tree(s) -> merge into one tree
            else:
                name = next(iter(merge_names))

                # If this account connects multiple trees,
                # merge those trees into `name`
                for other in merge_names:
                    if other == name:
                        continue

                    for email in M[other]:
                        M[name].add(email)
                        pairs.add((name, email))

                    del M[other]

                # Add current account's emails
                for j in range(1, k):
                    email = accounts[i][j]
                    M[name].add(email)
                    pairs.add((name, email))

        ans = []

        for node in M:
            res = []

            idx = node.find("$")
            if idx == -1:
                idx = len(node)

            res.append(node[:idx])

            for email in sorted(M[node]):
                res.append(email)

            ans.append(res)

        return ans