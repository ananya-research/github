class Solution:
    def addDigits(self, num: int) -> int:

        w=str(num)

        while len(w)>1:
            s=0
            for i in w:
                s+=int(i)
            w=str(s)
        
        return int(w)

            
            

        