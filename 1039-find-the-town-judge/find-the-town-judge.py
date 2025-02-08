from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        D=defaultdict(list)

        if n==1:
            return 1


        for u,v in trust:
            D[v].append(u)

        # print(D)

        # val=D[1]

        # c=0
        
        # for u,v in D.items():
        #     if D[u]!=val:
        #         return -1
    


        # for i in range(1,n+1):
        #     if i not in D.keys():
        #         return n
        
        # return -1
        # for v in D.keys():
        #     print(D.values())

        for v in D.keys():
            
            f=len(D[v])
            if all(v not in val_list for val_list in D.values()):
                if f==n-1 and v not in D.values():
                    return v
        return -1        