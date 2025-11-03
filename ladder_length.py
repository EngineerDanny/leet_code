from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        words = set(wordList)
        words.add(beginWord)

        buckets = defaultdict(list)               # pattern -> words matching it
        for w in words:
            for i in range(L):
                buckets[w[:i] + '*' + w[i+1:]].append(w)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, dist = q.popleft()
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                for nei in buckets[key]:
                    if nei == endWord:
                        return dist + 1
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, dist + 1))
                buckets[key] = []                 # important: avoid re-scanning
        return 0
