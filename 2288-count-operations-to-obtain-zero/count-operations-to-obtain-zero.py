class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        c=0
        while num1 and num2:
            if num1>=num2:
                num1-=num2
                num1=abs(num1)
            else:
                num2-=num1
                num2=abs(num2)
            c+=1
        
        return c
        

        