class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
#         n=len(grid)
#         m=len(grid[0])

#         def dfs(i,j):
#             if i<0 or i>=n or j<0 or j>=m or grid[i][j]!='1':
#                 return
#             else:
#                 grid[i][j]='0'
#                 dfs(i,j+1)
#                 dfs(i,j-1)
#                 dfs(i-1,j)
#                 dfs(i+1,j)



#         num_of_islands=0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j]=='1':
#                     num_of_islands+=1
#                     dfs(i,j)
                    
#         return num_of_islands
    
    
    
    
    
    
        # row=len(grid)
        # col=len(grid[0])
        
        # num_of_islands=0
        
        # def dfs(a,b):
            
        #     if a<0 or a>=row or b<0 or b>=col or grid[a][b]!='1':
        #         return
        #     else:
        #         grid[a][b]='0'
        #         dfs(a-1,b)
        #         dfs(a+1,b)
        #         dfs(a,b-1)
        #         dfs(a,b+1)
        
        # for i in range(row):
        #     for j in range(col):
            
        #         if grid[i][j]=='1'
        #             num_of_islands+=1
        #             dfs(i,j)
                
                    
        # return num_of_islands




                    





        # n=len(grid)
        # m=len(grid[0])

        # num=0

        # def dfs(i,j):

        #     if i<0 or i>=n or j<0 or j>=m or grid[i][j]!='1':
        #         return
        #     else:
        #         grid[i][j]='0'
        #         dfs(i+1,j)
        #         dfs(i-1,j)
        #         dfs(i,j+1)
        #         dfs(i,j-1)


        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j]=='1':
        #             dfs(i,j)
        #             num+=1
        
        # return num




        n=len(grid)
        m=len(grid[0])

        num_of_islands=0

        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]!='1':
                return 
            else:
                grid[i][j]='0'
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)



        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    num_of_islands+=1
                    dfs(i,j)

        return num_of_islands

































        
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        