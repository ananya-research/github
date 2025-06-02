class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: enqueue all gates (cells with value 0)
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        # Step 2: BFS from all gates simultaneously
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                # If the neighbor is in bounds and is an empty room
                if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2**31 - 1:
                    rooms[nx][ny] = rooms[x][y] + 1
                    queue.append((nx, ny))