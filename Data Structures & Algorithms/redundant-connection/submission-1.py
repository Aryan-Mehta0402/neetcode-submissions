class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [x for x in range(len(edges)+1)]
        rank = [0] * (len(edges) + 1)

        def fp(u):
            if u == parent[u]:
                return u
            # path compression
            parent[u] = fp(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = fp(u), fp(v)
            if pu == pv:
                return False
            ru, rv = rank[pu], rank[pv]
            if ru > rv:
                parent[pv] = pu
                rank[pu] = max(rank[pu], 1 + rank[pv])
            else:
                parent[pu] = pv
                rank[pv] = max(rank[pv], 1 + rank[pu])
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]