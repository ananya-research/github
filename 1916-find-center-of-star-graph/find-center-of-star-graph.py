

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

       

        n=len(edges)+1

        connected=[0]*(n+1)

        for u,v in edges:
            connected[u]+=1
            connected[v]+=1

        for i in range(1,n+1):
            if connected[i]==n-1:
                return i


        