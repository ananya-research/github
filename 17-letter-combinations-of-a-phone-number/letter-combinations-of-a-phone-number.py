class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        sol=[]

        if digits=="":
            return []

        n=len(digits)
        hmap={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}

        def backtrack(i):

            if i==n:
                res.append("".join(sol))
                return
            else:
                for letter in hmap[digits[i]]:
                    sol.append(letter)
                    backtrack(i+1)
                    sol.pop()

        backtrack(0)
        return res














































        
        # ans=[]  
        # sol=[]
        # n=len(digits)

        # if digits=="":
        #     return []

        # hmap={'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9':'wxyz'}
        
        # def backtrack(i=0):
        #     if i==n:
        #         ans.append("".join(sol))
        #         return
        #     for letter in hmap[digits[i]]:

        #         sol.append(letter)
        #         backtrack(i+1)
        #         sol.pop()

        # backtrack(0)
        # return ans

            
        
        
        