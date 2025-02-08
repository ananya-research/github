from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        
        if n==1:
            return True
        
        if source==destination:
            return True


        stack=[source]
        seen=set()
        seen.add(source)

        D=defaultdict(list)

        for u,v in edges:
            D[u].append(v)
            D[v].append(u)
            
        
        print(D)

        while stack:
            node=stack.pop()
            for nei in D[node]:
                if nei not in seen:
                    seen.add(nei)
                    stack.append(nei)
                    if nei==destination:
                        return True

        return False