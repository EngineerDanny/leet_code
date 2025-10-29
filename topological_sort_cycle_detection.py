from typing import List

class SolutionDFS:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph: b -> a
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)

        state = [0] * numCourses  # 0=unvisited, 1=visiting, 2=done

        def dfs(u: int) -> bool:
            if state[u] == 1:  # back-edge → cycle
                return False
            if state[u] == 2:
                return True
            state[u] = 1
            for v in g[u]:
                if not dfs(v):
                    return False
            state[u] = 2
            return True

        for c in range(numCourses):
            if state[c] == 0 and not dfs(c):
                return False
        return True
