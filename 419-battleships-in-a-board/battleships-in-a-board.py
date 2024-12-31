class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        rows=len(board)
        cols=len(board[0])

        battleships=0

        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j]!='X':
                return
            else:
                board[i][j]='.'
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='X':
                    battleships+=1
                    dfs(i,j)


        return battleships





        