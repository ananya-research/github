from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # rows=len(grid)
        # cols=len(grid[0])

        # c=0

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j]==2:
        #             if grid[i-1][j]==1:
        #                 grid[i-1][j]=2
        #             if grid[i][j-1]==1:
        #                 grid[i][j-1]=2
        #             if grid[i][j+1]==1:
        #                 grid[i][j+1]=2
        #             if grid[i+1][j]==1:
        #                 grid[i+1][j]=2
        #             c+=1
        #         else:
        #             return -1

        # return c



        rows=len(grid)
        cols=len(grid[0])

        num_fresh=0

        q=deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    num_fresh+=1

        if num_fresh==0:
            return 0

        
        minutes=-1

        while q:
            q_size=len(q)
            minutes+=1

            for _ in range(q_size):
                i,j=q.popleft()

                for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==1:
                        grid[r][c]=2
                        num_fresh-=1
                        q.append((r,c))
        
        if num_fresh==0:
            return minutes
        else:
            return -1




    




                    






        