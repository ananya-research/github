class Solution:
    def superPow(self, a: int, b: List[int]) -> int:

        
        # p="".join(map(str, b))
        # p=int(p)
        # print(p)
        
        # def helper(a,p):

        #     a=a%1337

        #     if a==0:
        #         return 0

        #     if p==0:
        #         return 1
            
            

        #     res=helper(a*a,p//2)%1337
        #     return (a*res)%1337 if p%2 else res%1337

        # res=helper(a,p)%1337
        # return res
            
        p=int("".join(map(str,b)))
        return pow(a,p,1337)