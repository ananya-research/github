class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        max_dist = 0
        prev = -1  # index of the last person seen

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    # Leading zeros case: from 0 to first 1
                    max_dist = i
                else:
                    # Middle case: distance to closest person is half the gap
                    max_dist = max(max_dist, (i - prev) // 2)
                prev = i

        # Trailing zeros case: distance from last person to end
        max_dist = max(max_dist, len(seats) - 1 - prev)

        return max_dist
        