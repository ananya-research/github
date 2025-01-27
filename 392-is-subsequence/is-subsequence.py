class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        c=0
        n=len(t)
        m=len(s)

        l=0
        r=0


        while l<len(s) and r<len(t):
            if s[l]==t[r]:
                l+=1
            r+=1
        
        return l==len(s)
 
            



        