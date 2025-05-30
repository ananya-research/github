class Solution:
    def isPalindrome(self, x: int) -> bool:
        # m=str(x)
        # if m==(m[::-1]):
        #     print(m[::-1])
        #     return True
        # return False

        s=str(x)
        n=len(s)

        l=0
        r=n-1

        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True

    
        