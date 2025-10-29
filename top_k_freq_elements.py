from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # 1) Frequency map (no Counter)
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    # 2) Buckets: index = frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, f in freq.items():
        buckets[f].append(num)

    # 3) Gather from highest frequency down
    ans = []
    for f in range(len(nums), 0, -1):
        for num in buckets[f]:
            ans.append(num)
            if len(ans) == k:
                return ans
    return ans  # in case k == 0 (not typical on LC)
