class Solution:
    def minChanges(self, s: str) -> int:
        if len(set(s))==1:
            return 0
        #print(set(s))
        n=len(s)
        #print(n)
        j=1
        i=0
        c=0
        while j+2<=n+1 and i+2<=n+1:
            if s[i]!=s[j]:
                c+=1
            j+=2
            i+=2
        return c



        