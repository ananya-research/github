class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dir=1  
        i=1
        for t in range(1,time+1):
            i=i+dir
            if i>n:
                dir=-dir
                i=i+dir-1
            elif i<1:
                dir=-dir
                i=i+dir+1
        return i


    
                                                      

        
        