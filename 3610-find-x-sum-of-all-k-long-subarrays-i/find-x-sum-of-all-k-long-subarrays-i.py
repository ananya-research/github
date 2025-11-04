from typing import List
from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)

            # build a max-heap using negative frequencies and negative values
            heap = [(-count, -val) for val, count in freq.items()]
            heapq.heapify(heap)

            # pop top x frequent (and larger) elements
            top_vals = set()
            for _ in range(min(x, len(heap))):
                count, val = heapq.heappop(heap)
                top_vals.add(-val)  # remember we negated it

            # sum only numbers that are in the selected top x elements
            total = sum(num for num in sub if num in top_vals)
            ans.append(total)

        return ans
