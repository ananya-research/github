class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res=[]
        sol=[]

        def backtrack(openn, closse):
            if len(sol)==2*n:
                res.append(''.join(sol))
                return
            
            if openn<n:
                sol.append('(')
                backtrack(openn+1, closse)
                sol.pop()
            
            if openn>closse:
                sol.append(')')
                backtrack(openn, closse+1)
                sol.pop()
        
        backtrack(0,0)
        return res
            

        

        
        