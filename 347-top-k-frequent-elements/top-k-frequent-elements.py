from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k==len(nums):
            return nums
        

        count=Counter(nums)
        print(count)

        return heapq.nlargest(k, count.keys(), key=count.get)

        