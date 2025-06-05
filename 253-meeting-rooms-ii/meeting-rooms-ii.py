class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort meetings by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Min-heap to store end times of meetings in rooms
        heap = []

        for interval in intervals:
            start, end = interval

            # Step 3: If the room due to free earliest is free before the meeting starts, reuse it
            if heap and heap[0] <= start:
                heapq.heappop(heap)  # free that room

            # Step 4: Allocate a room (either reused or new)
            heapq.heappush(heap, end)

        # Step 5: Heap size tells the minimum number of rooms needed
        return len(heap)
