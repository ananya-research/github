class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        from collections import Counter

        rows=len(grid)
        cols=len(grid[0])

        count=0
        ans=0

        row_counter=Counter(tuple(row) for row in grid)

        print(row_counter)

        for c in range(rows):
            col=[grid[i][c] for i in range(rows)]
            count+=row_counter[tuple(col)]

        return count


        



                
            


        


                


        