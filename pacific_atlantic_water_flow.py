from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        dirs = ((1,0), (-1,0), (0,1), (0,-1))

        def dfs(r: int, c: int, seen: set):
            if (r, c) in seen:
                return
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # reverse flow: can move from (r,c) to (nr,nc) if neighbor is >=
                if 0 <= nr < m and 0 <= nc < n and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, seen)

        pac, atl = set(), set()

        # Pacific starts: top row + left column
        for c in range(n):
            dfs(0, c, pac)
        for r in range(m):
            dfs(r, 0, pac)

        # Atlantic starts: bottom row + right column
        for c in range(n):
            dfs(m - 1, c, atl)
        for r in range(m):
            dfs(r, n - 1, atl)

        # Cells that both oceans can reach (in reverse) → can flow to both (forward)
        return [list(rc) for rc in (pac & atl)]
