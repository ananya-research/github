class Solution:
    def reverse(self, x: int) -> int:

        MINN=-2**31
        MAXX=(2**31)-1
        print(MINN,MAXX)

        sign=1

        if x<0:
            sign=-1

        

        res=0

        x=abs(x)
       

        while x>0:
            
            div=x%10

            res=res*10+div
            if res>MAXX or res<MINN: return 0
            x=x//10
            
        
        return res*sign


            



        


        return 0
        