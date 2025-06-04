class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        original_k = sum(1 for x in nums if x == k)
        best_gain = 0

        for val in set(nums):
            if val == k:
                continue

            gain = []
            for x in nums:
                if x == val:
                    gain.append(1)
                elif x == k:
                    gain.append(-1)
                else:
                    gain.append(0)

            # Kadane’s algorithm to find max sum subarray
            curr_sum = 0
            max_sum = 0
            for g in gain:
                curr_sum = max(0, curr_sum + g)
                max_sum = max(max_sum, curr_sum)

            best_gain = max(best_gain, max_sum)

        return original_k + best_gain



       
        