class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [] 
        row  = len(grid)
        col = len(grid[0])
        vis_A = set()
        vis_P = set()
        
        # start traversing from edges and mark all reachable cell
        def dfs(i, j, vis):
            if (i, j) in vis:
                return
            vis.add((i, j))

            dr = [0, 0 , -1, 1]
            dc = [ 1, -1, 0, 0]

            for k in range(4):
                if (i + dr[k] < 0 or j + dc[k] < 0 or i + dr[k] >= row or           
                    j + dc[k] >=  col or grid[i + dr[k]][j + dc[k]] < grid[i][j]):
                    continue
                dfs(i + dr[k], j + dc[k], vis)

        # traverse for all atlantic borders -> r = row - 1 or c = c - 1
        for i in range(col):
            dfs(row - 1, i, vis_A)

        for i in range(row):
            dfs(i, col - 1, vis_A)  
        # traverse for all pacific borders - > r = 0 or c = 0
        for i in range(col):
            dfs(0, i, vis_P)

        for i in range(row):
            dfs(i, 0, vis_P)  

        for i in range(row):
            for j in range(col):
                if (i, j) in vis_P and (i, j) in vis_A:
                    ans.append([i, j])

        return ans