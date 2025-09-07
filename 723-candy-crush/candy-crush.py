class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        n=len(board)
        m=len(board[0])

        while True:
            crush=False   
            for r in range(n):
                c=0
                while c<m-2:                    
                        v=abs(board[r][c])
                        if v!=0 and abs(board[r][c+1])==v and abs(board[r][c+2])==v:
                            crush=True
                            k=c
                            while k<m and abs(board[r][k])==v:
                                board[r][k]=-v
                                k+=1
                            c=k
                        else:
                            c+=1
            for c in range(m):
                r=0
                while r<n-2:
                    v=abs(board[r][c])
                    if v!=0 and abs(board[r+1][c])==v and abs(board[r+2][c])==v:
                        crush=True
                        k=r
                        while k<n and abs(board[k][c])==v:
                            board[k][c]=-v
                            k+=1
                        r=k
                    else:
                        r+=1
            if not crush:
                break
            for c in range(m):
                write=n-1
                for r in range(n-1, -1, -1):
                    if board[r][c]>0:
                        board[write][c]=board[r][c]
                        write-=1
                for r in range(write, -1, -1):
                    board[r][c]=0

        return board


                                        
            