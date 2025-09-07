class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        rows=len(boxGrid)
        cols=len(boxGrid[0])

        for r in range(rows):
            i=cols-1
            for c in reversed(range(cols)):
                if boxGrid[r][c]=='#':
                    boxGrid[r][c], boxGrid[r][i]=boxGrid[r][i], boxGrid[r][c]
                    i-=1
                elif boxGrid[r][c]=="*":
                    i=c-1
            
        ans=[[0 for _ in range(rows)] for _ in range(cols)]

        for r in range(rows):
            for c in range(cols):
                ans[c][rows-1-r]=boxGrid[r][c]
            
        return ans
                

        