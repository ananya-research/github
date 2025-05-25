class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # p_que=deque()
        # p_seen=set()

        # a_que=deque()
        # a_seen=set()

        # rows=len(heights)
        # cols=len(heights[0])

        # for i in range(cols):
        #     p_que.append((0,i))
        #     p_seen.add((0,i))
        
        # for i in range(1,rows):
        #     p_que.append((i,0))
        #     p_seen.add((i,0))

        # for j in range(rows):
        #     a_que.append((j,cols-1))
        #     a_seen.add((j,cols-1))
        
        # for j in range(cols-1):
        #     a_que.append((rows-1,j))
        #     a_seen.add((rows-1,j))

        # def get_coords(que, seen):
        #     coords=set()

        #     while que:
        #         i,j=que.popleft()
        #         coords.add((i,j))
        #         for i_off, j_off in [(0,1), (0,-1), (1,0), (-1,0)]:
        #             r=i+i_off
        #             c=j+j_off
        #             if 0<=r<rows and 0<=c<cols and heights[i][j]<=heights[r][c] and (r,c) not in seen:
        #                 seen.add((r,c))
        #                 que.append((r,c))
                    
        # get_coords(p_que,p_seen)
        # get_coords(a_que,a_seen)

        # return list(p_seen.intersection(a_seen))


        p_que=[]
        p_seen=set()

        a_que=[]
        a_seen=set()

        rows=len(heights)
        cols=len(heights[0])

        for i in range(cols):
            p_que.append((0,i))
            p_seen.add((0,i))
        
        for i in range(1,rows):
            p_que.append((i,0))
            p_seen.add((i,0))

        for j in range(rows):
            a_que.append((j,cols-1))
            a_seen.add((j,cols-1))
        
        for j in range(cols-1):
            a_que.append((rows-1,j))
            a_seen.add((rows-1,j))

        def get_coords(que, seen):
            coords=set()

            while que:
                i,j=que.pop()
                coords.add((i,j))
                for i_off, j_off in [(0,1), (0,-1), (1,0), (-1,0)]:
                    r=i+i_off
                    c=j+j_off
                    if 0<=r<rows and 0<=c<cols and heights[i][j]<=heights[r][c] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
                    
        get_coords(p_que,p_seen)
        get_coords(a_que,a_seen)

        return list(p_seen.intersection(a_seen))
                    

        
       


        