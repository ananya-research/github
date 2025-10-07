from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n                 # default -1 for rain days, will set for sunny days
        last_rain = {}                 # lake -> last day index it rained (when it became full)
        sunny_days = []                # sorted list of indices i where rains[i] == 0

        def find_first_greater(lst, x):
            """Return the index in lst of the first element > x, or len(lst) if none.
               Implemented with binary search (no library)."""
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        for day, lake in enumerate(rains):
            if lake == 0:
                # mark sunny day placeholder; default drying any lake (1) if unused
                ans[day] = 1
                # keep sunny_days sorted by appending (we'll maintain sortedness because day increases)
                sunny_days.append(day)
            else:
                # it's raining on `lake`
                # if lake was full already (rained before), we must dry it between last_rain[lake] and now
                if lake in last_rain:
                    prev_day = last_rain[lake]
                    # find earliest sunny day strictly after prev_day
                    idx = find_first_greater(sunny_days, prev_day)
                    if idx == len(sunny_days):
                        # no available sunny day to dry this lake -> impossible
                        return []
                    # use sunny_days[idx] to dry this lake
                    dry_day = sunny_days.pop(idx)   # remove that sunny day
                    ans[dry_day] = lake             # record that we dried `lake` that day
                # now this lake becomes full at `day`
                last_rain[lake] = day
                ans[day] = -1

        return ans
