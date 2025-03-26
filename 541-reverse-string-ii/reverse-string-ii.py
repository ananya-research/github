class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        l=list(s)
        n=len(s)
        
        for i in range(0,n,2*k):         
            l[i:i+k]=reversed(l[i:i+k])
            

        return "".join(l)
                

        