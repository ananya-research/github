class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Precompute consecutive 1's to the left and up for each cell
        left = [[0]*n for _ in range(m)]
        up = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = 1 + (left[i][j-1] if j > 0 else 0)
                    up[i][j] = 1 + (up[i-1][j] if i > 0 else 0)

        max_side = 0
        # Try all possible bottom-right corners
        for i in range(m):
            for j in range(n):
                small = min(left[i][j], up[i][j])
                while small > 0:
                    # Check top border and left border for sufficient streak of 1s
                    if left[i - small + 1][j] >= small and up[i][j - small + 1] >= small:
                        max_side = max(max_side, small)
                        break
                    small -= 1

        return max_side * max_side
        