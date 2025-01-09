class Solution:
    def isHappy(self, n: int) -> bool:

        s=0

        seen=set()

        w=str(n)

        

        while w!="1":
            if w in seen:
                return False
            s=0
            for i in w:
                s+=int(i)**2
            seen.add(w)
            w=str(s)
            
        
        if w=="1":
            return True
