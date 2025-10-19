class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        queue=deque([s])
        visited={s}
        res=s
        n=len(s)
        if n<1:
            return s

        while queue:
            current=queue.popleft()
            if current<res:
                res=current

            t_list=list(current)

            for i in range(1,n,2):
                t_list[i]=str((int(t_list[i])+a)%10)
            add_curr="".join(t_list)

            if add_curr not in visited:
                visited.add(add_curr)
                queue.append(add_curr)
            
            b_list=list(current)

            rotate_curr=b_list[-b:]+b_list[:-b]

            rotate_curr="".join(rotate_curr)

            if rotate_curr not in visited:
                visited.add(rotate_curr)
                queue.append(rotate_curr)
            
        
        return res



            

            
        