from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        pad = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        out, path = [], []

        def dfs(i: int) -> None:
            if i == len(digits):
                out.append("".join(path))
                return
            for ch in pad[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()  # backtrack

        dfs(0)
        return out
